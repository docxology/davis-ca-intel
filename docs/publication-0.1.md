# Before a 0.1 publication

The manuscript review target is 0.1.0; the application manifest retains its
existing version. A public review packet is labelled `review-draft`. It does not
reserve a DOI or create a release/tag. The [readiness record](review-readiness.md)
names the actually reviewed packet and the limits of that technical review.

## Technical preflight

```sh
bun install --frozen-lockfile
bun run release:check
```

This checks consumer identity, authored manuscript/evidence contracts and the
exact committed PDF/HTML bundle against current captured inputs. Native
regeneration additionally requires Pandoc, XeLaTeX, qpdf and pdftotext; its tool
versions and hashes are retained. Preserve earlier failures and replace a packet
only through the shared renderer. After any numbered source, seed, policy,
dependency or renderer change, rebuild and inspect the new packet and renew the
applicable independent review. No check changes the acquisition timestamp.

## Publication decisions that remain separate

- The author confirms final authorship, contribution, funding and conflict
  declarations and approves the manuscript text and permitted source use.
- Qualified scientific/legal or editorial assessment, if claimed, has its own
  named review; an automated technical gate or AI-assisted review does not supply it.
- A release freezes actual source/lock and artifact hashes, declares scope and
  license boundaries, and names the intended archive or repository destination.
- Tags, release assets, DOI reservation and publication require the owner's
  explicit publication instruction. Keep draft labels until that disposition.
- After an authorized publication, independently verify the remote record,
  downloadable bytes, checksums and links. Local rendering and Actions success
  do not establish the archive's final state.

No new legal-currency, model-factuality, civic-impact or source-completeness claim
is introduced by labelling this document 0.1. The accepted municipal seed and
its original verification time remain the empirical scope.
