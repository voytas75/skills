# Example: bound a CSV export feature

**Input:** Add CSV export to the task list. Keep storage and the existing API unchanged.
Context: the list already loads task titles and statuses. Size: small.

- **Recommended slice:** Add an Export CSV button that downloads the currently
  loaded task titles and statuses using a focused CSV serializer.
- **Why this now:** One useful interface seam without server or storage changes.
- **Do now:** Add `csv-export.ts`, connect one button, and add serializer tests.
- **Do later:** Export all pages, background jobs, configurable columns.
- **Acceptance checks:** Run the project's serializer test target; comma, quote,
  newline, and empty-value fixtures must pass. In a browser smoke check, export
  two loaded tasks and inspect the header, row count, and escaped values. Verify
  dangerous spreadsheet formula prefixes are handled by the agreed safe policy.
  These are proposed checks, not results of a test run.
- **Rollback:** Revert the button, serializer, and focused tests together.
- **Anti-goals:** No API change, storage migration, or automatic background export.
- **Open questions:** Confirm the spreadsheet-safe escaping policy before coding.
