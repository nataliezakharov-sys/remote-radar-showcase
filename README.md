# Remote Radar — AI-assisted Product Design & Development

A standalone, interactive portfolio showcase of **Remote Radar**, an independent job-discovery and application-management project.

**[Explore the broader Remote Radar demo](https://remote-radar-demo-demo.up.railway.app/)** · This GitHub repository contains a separate, intentionally limited code sample, **not** the source of that hosted demo.

> **Portfolio sample:** Every company, job, match score, date, and application state in this repository is fictional. No employer integrations, personal application records, production credentials, or live submission capabilities are included.

## The problem

Finding suitable remote Product Design roles involves comparing location restrictions, role requirements, and existing applications across fragmented sources. Remote Radar explores how to make that work more structured, explainable, and manageable.

## What I designed and built

- An opportunity-discovery dashboard with clear match and eligibility signals
- Search, sorting, and location filters for evaluating opportunities
- A detailed role panel with evidence behind each illustrative match
- Shortlist and human-review interactions with browser-local state
- Responsive layouts and useful empty, selected, and reset states

The showcase focuses on **interface and interaction patterns**, not an operational applicant tracking system. The sample match scores are illustrative, not calculated by a production matching model.

## My role and process

**Product direction & UX/UI:** I defined the workflow, information architecture, interaction details, visual language, and review criteria.

**AI-assisted engineering:** I used tools including Claude and Codex to translate design requirements into working features, investigate bugs, review code changes, and iterate with tests.

**Testing & iteration:** I reviewed browser behavior, refined responsive controls, and kept potentially consequential actions behind explicit human review in the separate private project.

This project illustrates design-to-code ownership with AI assistance. It is **not** a claim of independently hand-coding every feature, production React/TypeScript proficiency, or measured external adoption.

## Try it locally

Requires Python 3.10 or newer. There are **no third-party dependencies**.

```bash
python3 server.py
```

Visit **http://127.0.0.1:8765** and try searching, sorting, selecting a job, shortlisting, marking it for review, and using **Reset demo**.

Run the regression tests:

```bash
python3 -m unittest discover -s tests -v
```

The five standard-library tests cover sample-data isolation, read-only behavior, allowed routes, health/security headers, and static asset delivery.

## Technical overview

| Layer | Implementation |
| --- | --- |
| Frontend | HTML, CSS, vanilla JavaScript |
| Backend | Python standard library HTTP server |
| Data | Hard-coded fictional job records |
| Interaction state | Browser-local `localStorage` |
| External APIs | None |
| Authentication / payments / job submissions | Not implemented |

The server exposes only the showcase page/assets, `/health`, and the read-only fictional `/api/jobs` endpoint. Write requests are rejected. No production database, private Git history, credentials, or applicant information are used.

### Relationship to the full project

The actual Remote Radar project includes more extensive discovery, eligibility, document, and approval workflows, with a private repository and deployment. This showcase was built separately to demonstrate a subset of its UX and development patterns safely. The source here should not be mistaken for the full implementation or the source running at the hosted demo link.

## Notes

- This is a **portfolio demonstration**, not a live job-search or application service.
- Data, scores, and statuses are **illustrative**, not real-world outcomes.
- A separate deployment would require its own infrastructure and security review. Never connect this showcase to production credentials, data, or volumes.
- For maintainer-only checks, see [PUBLISHING_GUIDE.md](PUBLISHING_GUIDE.md).
