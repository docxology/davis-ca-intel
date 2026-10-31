# Accepted Davis public seed

This directory contains the reviewed public municipal-code projection from
eCode360 `DA4922`: 290 article pages and 2541 sections. The
[edition record](../docs/edition.md) names the exact edition, verification time
and hashes; [publication-input.json](publication-input.json) and
[verification-report.json](verification-report.json) are the source receipts.
These files preserve a recorded source edition, not continuing legal currency.

A fresh clone can publish this seed with `bun run pages:export` followed by
`bun run pages:validate -- .pages`. It does not contain the private retained
HTML/article custody needed for local raw-corpus search or corpus promotion.
Live news, meetings and alerts are collected separately and keep their own clocks.

Refresh only through the shared accepted-corpus methods after successful
[candidate acquisition, verification and promotion](../docs/acquisition.md).
`bun run pages:seed` requires the complete matching hash-bound verification
receipt. Do not copy partial articles, raw HTML, operator diagnostics or another
municipality's seed into this directory. Update edition documentation from the
resulting receipts and validate a fresh Pages export before committing.
