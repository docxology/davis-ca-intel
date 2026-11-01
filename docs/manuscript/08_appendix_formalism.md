# Appendix: Formal Contracts and Worked Records {#sec:appendix}

For this review edition, a claim-evidence entry names captured public file paths
and states both its scope and what is not established. The counts in the Results
table are substituted from validated seed records rather than entered by hand.
The complete file-by-file byte commitments are in `evidence.json`; rendered
members and tool versions are in `review-receipt.json`.

```text
profile: {{PROFILE_ID}}
municipality: {{MUNICIPALITY_CODE}}
source edition:
{{EDITION_ID}}
shared runtime:
{{CORE_PIN}}
manuscript input fingerprint:
{{EVIDENCE_FINGERPRINT}}
```

Three separate acceptance questions remain visible: whether captured inputs
match their declared edition; whether the PDF/HTML render matches the captured
manuscript inputs; and whether reviewers accept the claims and interpretation.
The software checks the first two operational boundaries. It cannot certify the
third by writing a successful receipt or a version number.
