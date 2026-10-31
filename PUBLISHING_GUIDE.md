# Remote Radar Showcase — review and publishing guide

**State:** Private review branch. Public release and deployment are NOT authorized.

## Repository layout

- `main`: private placeholder only.
- `review/sanitized-showcase`: isolated showcase code, fictional data, documentation and tests.
- The real `remote-radar-private` repository, its branches, database and Railway deployment are entirely separate.

Do **not** copy the original repository's history, database, files under `/data`, credentials, application answers, exported resumes or browser profiles into this showcase.

## Local evaluation

1. Clone **this showcase repository**, not the private production repository.
2. Switch to `review/sanitized-showcase`.
3. Run `python3 -m unittest discover -s tests -v`.
4. Run `python3 server.py` and visit `http://127.0.0.1:8765`.
5. Try searching, filtering, sorting, shortlisting, flagging needs-review, and resetting.
6. Review on mobile and desktop widths; navigate all controls with a keyboard.

No Node, third-party packages, accounts, tokens or network access are needed for normal local operation.

## Privacy and security checks before release

- Inspect the full proposed Git diff and commit history. Confirm that only **synthetic** companies, roles, scores, and statuses are included.
- Search for secrets, credentials, applicant details, resume content, real contact information, access tokens, production volumes, databases, and private cloud endpoints.
- Confirm that the server's fixed-path whitelist serves only the three public assets, the health endpoint, and fictional `/api/jobs`.
- Confirm non-GET actions return 405 and no outbound application submissions or external API calls exist.
- Review security headers, cross-origin behavior, localStorage use, and HTML escaping.
- Inspect any new media or brand assets for NDA/copyright concerns.
- Confirm there is no production volume, secret, job-search history or active job-feed integration.

**Tests are not a full penetration test.** A browser-based usability and accessibility check and human security review are still required.

## Publishing, only after explicit approval

1. Review the proposed draft pull request, documentation, code and screenshots.
2. Authorize merging it into **this showcase repository**, if appropriate.
3. Authorize changing **this showcase repository only** from Private to Public.
4. If desired, separately approve deployment to an independent free hosting destination; do not share Railway volumes, environment variables, credentials, or application sessions with production.
5. Open the deployed page in an unauthenticated browser to verify it works.
6. Link both the public GitHub repo and the standalone demo from the portfolio and Design Engineer applications.

Do not claim external user counts, measured conversion outcomes, production React/TypeScript expertise, or that the showcase is a full exported copy of the private app.

## Suggested recruiter description

"Remote Radar is an independent job-discovery product I designed and developed using AI-assisted coding with Claude and Codex. This public code sample is a standalone, read-only implementation of its core discovery, search, filtering, shortlist, and review interactions using fictional data."

Keep the private product and its entire Git history unchanged.
