"""Prepare the Davis paper for Template stages from the retained public review inputs."""

import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "docs/manuscript"
REVIEW = ROOT / "review/0.1.0-draft"
OUTPUT = ROOT / "output"
PATTERN = re.compile(r"\{\{([A-Z][A-Z0-9_]*)\}\}")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, description):
    if not condition:
        raise SystemExit(f"Davis review staging refused: {description}")


def main():
    for name in ("manuscript", "figures"):
        require(not (OUTPUT / name).exists(), f"output/{name} already exists")
    receipt = read_json(REVIEW / "review-receipt.json")
    evidence = read_json(REVIEW / "evidence.json")
    require(
        receipt["profileId"] == evidence["profileId"] == "davis-ca"
        and receipt["inputFingerprint"] == evidence["inputFingerprint"],
        "receipt and evidence identities differ",
    )
    for name, facts in evidence["files"].items():
        path = ROOT / name
        require(
            path.is_file() and path.stat().st_size == facts["bytes"] and digest(path) == facts["sha256"],
            f"canonical evidence input changed: {name}",
        )

    sources = sorted(CANONICAL.glob("[0-9][0-9]_*.md"))
    require(len(sources) == 10, "expected ten canonical sections")
    figures = ("architecture.png", "corpus-profile.png", "evidence-boundaries.png")
    numeric_outputs = ("article-sections.csv", "corpus-profile.json")
    members = [
        "evidence.json",
        "graphical_abstract.md",
        *(source.name for source in sources),
        *numeric_outputs,
        *(f"figures/{name}" for name in figures),
    ]
    for name in members:
        require(digest(REVIEW / name) == receipt["files"][name], f"review member changed: {name}")

    # The archived sections are a control for hydration from the selected source.
    hydrated = {}
    for source in sources:
        rendered = PATTERN.sub(lambda match: evidence["variables"][match[1]], source.read_text(encoding="utf-8"))
        require(rendered == (REVIEW / source.name).read_text(encoding="utf-8"), f"projection changed: {source.name}")
        hydrated[source.name] = rendered
    hydrated["00_00_graphical_abstract.md"] = (REVIEW / "graphical_abstract.md").read_text(encoding="utf-8")

    manuscript = OUTPUT / "manuscript"
    manuscript.mkdir(parents=True)
    for name, body in hydrated.items():
        (manuscript / name).write_text(body, encoding="utf-8")
    for name in ("references.bib", "claim_ledger.json"):
        shutil.copyfile(CANONICAL / name, manuscript / name)
    (manuscript / "config.yaml").write_text(
        "# Generated manuscript ordering\n" + (CANONICAL / "config.yaml").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    figure_dir = OUTPUT / "figures"
    figure_dir.mkdir()
    registry = {}
    for body in hydrated.values():
        for caption, name, label in re.findall(r"!\[([^\n]+)\]\(\.\./output/figures/([^/)]+)\)\{#(fig:[^} ]+)", body):
            require(name in figures, f"figure is outside the retained set: {name}")
            registry[label] = {
                "label": label,
                "filename": name,
                "caption": caption,
                "generated_by": f"review/0.1.0-draft/figures/{name}",
                "metadata": {"alt_text": caption},
            }
    require({entry["filename"] for entry in registry.values()} == set(figures), "figure inventory differs")
    for name in figures:
        shutil.copyfile(REVIEW / "figures" / name, figure_dir / name)
    (figure_dir / "figure_registry.json").write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")

    metrics_dir = OUTPUT / "review-evidence"
    metrics_dir.mkdir(exist_ok=True)
    for name in numeric_outputs:
        shutil.copyfile(REVIEW / name, metrics_dir / name)
    selected_counts = {key: int(evidence["variables"][key]) for key in ("SOURCE_COUNT", "MONITOR_COUNT")}
    (metrics_dir / "configuration-counts.json").write_text(json.dumps(selected_counts) + "\n", encoding="utf-8")
    print(f"Verified {len(sources)} hydrated sections and {len(registry)} figures from retained Davis evidence.")


if __name__ == "__main__":
    main()
