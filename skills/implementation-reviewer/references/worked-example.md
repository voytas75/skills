# Example: review an export slice

**Expected source:** Add CSV export for loaded rows; escape commas and quotes;
keep the task-list API unchanged. Acceptance also requires a browser download check.

**Supplied evidence:** A diff adding `csv-export.ts` and a button, a focused test
report covering commas and quotes, and an unrelated sorting change. No browser
check result is supplied. These are fictional teaching inputs, not executed tests.

- **Verdict:** Partially aligned.
- **What matches:** The diff implements the serializer and button. The supplied
  test report covers the two required escaping cases. The API diff is unchanged.
- **What is missing:** No confirmed implementation gap from the supplied evidence.
- **What drifted / widened:** The sorting change is outside the export brief.
- **What is unverified:** The browser download criterion has no result. Absence
  of evidence is not proof that the download is broken.
- **Recommended next action:** Obtain the browser smoke result and isolate the
  unrelated sorting change before accepting the slice.
- **Sources reviewed:** The export brief, supplied diff, and focused test report.
