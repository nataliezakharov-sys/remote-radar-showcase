# Remote Radar — interactive portfolio showcase

**Status: Private review candidate. Not cleared for public release.**

A self-contained, read-only demonstration of the UX patterns behind [Remote Radar](https://remote-radar-demo-demo.up.railway.app/), an independent job discovery and application-management product designed and built through AI-assisted coding.

> **This is a standalone portfolio implementation with fictional records, not an export of the private production application.** The real project has additional discovery, eligibility, document, approval, and application workflows. This showcase deliberately includes none of its accounts, secrets, real job history, or production Git history.

## What to try

- Browse fictional opportunities and inspect match explanations.
- Filter by location, search job titles, and sort results.
- Shortlist opportunities and mark them for human review.
- Switch between Discover, Shortlist, Needs review, and Applications.
- Reset the demo. Interactions change only browser-local demo state via `localStorage`.

These are demo interactions. There is **no real ATS, employer data, authentication, application submission, scoring engine, analytics, or email delivery**. All companies, match percentages, job posts, and dates are illustrative.

## Run locally

Requires Python 3.10 or newer. No dependencies, cloud services, accounts, or API keys.

```bash
python3 server.py
# Open http://127.0.0.1:8765
```

Run the security/isolation regression tests:

```bash
python3 -m unittest discover -s tests -v
```

To deploy later as a separate service, use `HOST=0.0.0.0` and the platform-supplied `PORT`. **No deployment is approved yet.** Any new service must have its own isolated environment with no shared private app secrets, database, or production volume.

## My role and use of AI

- **Product direction and UX:** requirements, user journeys, information architecture, interaction states, visual design, and implementation review.
- **AI-assisted implementation:** Claude and Codex to translate specifications into Python and JavaScript features, inspect changes, debug behavior, and iterate through tests and GitHub review.
- **Delivery:** Railway hosting and iterative testing for the private product; a separate, intentionally restricted portfolio demonstration.

This work showcases **AI-assisted product building**. It is not a claim that every line of the original production code was hand-written or that external user adoption has been measured.

## Architecture and isolation

| Component | Portfolio showcase | Private production |
| --- | --- | --- |
| UI | Vanilla JavaScript, HTML and CSS | Larger app with document and review flows |
| Backend | Python standard library; read-only endpoints | Python, SQLite, automation and integrations |
| Data | Fictional hard-coded samples | Restricted persistent database |
| State | Browser-only demo state | Private server-side history |
| Submissions | **Not implemented** | Explicit approval gates, not exposed here |
| External services | **None** | Hosted integrations not exposed here |

## Release checklist

- [ ] Review source and **new** Git history for secrets, personal data, and licensing concerns.
- [ ] Confirm requests cannot reach production or write server-side data.
- [ ] Check keyboard, accessibility, and desktop/mobile browser interactions.
- [ ] Only use NDA-safe images or screenshots.
- [x] Initialize **a separate private GitHub repository** and isolated review branch with a fresh history.
- [ ] Independently approve the code, then give explicit permission before changing visibility.
- [ ] Approve any hosting service and any additional costs before deployment.

No live job applications or external API calls are supported in this showcase. See [PUBLISHING_GUIDE.md](PUBLISHING_GUIDE.md) for review and release instructions.
