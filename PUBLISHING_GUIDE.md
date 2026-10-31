# Publication checklist — Remote Radar Showcase

The showcase implementation is on the repository's `main` branch. It is an **isolated code sample**, not a production-code export.

## What's already complete

- [x] Standalone repository with **fresh Git history**, separate from the private project
- [x] Fictional records and no live ATS integrations or job submissions
- [x] Five standard-library regression tests passed during preparation
- [x] Source-only review for obvious secrets and personal data in the merged files
- [x] Desktop and mobile layout checked by the project owner
- [x] Responsive dropdown CSS correction merged via PR #2

These checks reduce risk but do not constitute a comprehensive security or accessibility audit.

## Check before changing visibility

- [ ] Review all files and **the entire Git history** for personal data, credentials, proprietary material, or secrets
- [ ] Verify all browser actions work with keyboard, including clear visible focus states
- [ ] Confirm that the source and README are accurate and don't imply measured external user adoption
- [ ] Verify only fictional data is served from `/api/jobs`, and POST/PUT/DELETE requests are blocked
- [ ] Confirm no employer integrations or private production services are called
- [ ] Obtain explicit approval from the repository owner to change visibility to Public

## Make the showcase repository public (owner action)

1. In the **showcase** repository, open **Settings → General**.
2. Find **Danger Zone → Change repository visibility**.
3. Select **Public** and complete the GitHub confirmation steps.
4. In an incognito browser, confirm the README and repository files are visible without signing in.
5. Add the public repository URL to the portfolio and relevant Design Engineer applications.

This release must **not** change the visibility of `remote-radar-private`.

## Optional separate deployment

The locally runnable code is independent of the hosted Remote Radar demo. If a dedicated showcase deployment is desired, it needs separate approval, a separate host/volume, and **no shared environment variables, application credentials, or user data**. Test public access and browser interactions after deployment.

## Short portfolio description

Remote Radar is an independent job-discovery product I designed and developed through AI-assisted coding with Claude and Codex. This standalone code sample demonstrates discovery, filtering, shortlisting, and human-review UX using fictional data.
