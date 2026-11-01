# Reproducibility and Artifact Specification {#sec:reproducibility}

The consumer installs its full public Region Intel commit through a frozen Bun
lockfile. Shared algorithms and publication methods remain in that dependency.
A sibling source checkout is not required for normal consumer commands.
Native manuscript rendering additionally requires the pinned external
docxology/template checkout and its prepared Python/native tools.

~~~sh
bun install --frozen-lockfile
bun run validate
bun run manuscript:check
bun run manuscript:render
bun run manuscript:validate-render
bun run manuscript:bundle
bun run manuscript:validate-render -- --bundle
~~~

The documented environment selects the template root and interpreter explicitly.
The shared adapter rejects a wrong repository, commit or modified tracked
source. It records actual template, Python, Matplotlib, Pandoc and TeX versions;
the completed native packet is also checked with qpdf and pdftotext.
The template's combined writers generate the manuscript; regional code does
not silently substitute a separate direct-Pandoc rendering path.

The accepted seed, effective configuration, package/lock, numbered sources,
bibliography, claim ledger and cover bytes bind the manuscript fingerprint.
That fingerprint also binds the shared adapter/projection/figure source and
pinned web-asset inventory. The article-level CSV and profile JSON are exact
derived tables. PDF, SVG and PNG variants preserve the distinction between
measured counts and explanatory diagrams.

A complete HTML edition includes its assets and figure directory. Copying only
the HTML entry point omits font, mathematics and image dependencies. The review
validator checks bounded regular files, exact member inventory, current source
projection, output hashes and pinned template asset hashes. These checks are
consistent with the W3C emphasis on version and preservation metadata
[@dwbp2017], but successful replay is not a proof of semantic correctness.

The reproducibility record distinguishes computational repeatability, native
rendering and substantive acceptance. Bitwise PDF identity across different
native toolchains is not promised: versions, timestamps and font machinery
can affect serialization. Rebuilding a changed candidate requires renewed
source, figure, page and applicable independent review. Previous failed work
and the last complete packet remain available rather than being overwritten
with a partial artifact.

Data and source are available in the public Davis repository. Raw source
acquisition and operational diagnostics remain local. A public digest identifies
omitted evidence; it is not a replacement for that evidence and does not allow
a reader to reconstruct it.

Before committing, the operator stages the intended public files and checks the
index. After committing, the second command compares the current commit with
public input and complete packet bytes:

```sh
# After staging, before committing
bun run publication:check -- --staged

# After committing
bun run publication:check
```

This shared preflight rejects missing, ignored, linked or changed required Git
members. It does not stage files, publish a release or certify source
interpretation.
