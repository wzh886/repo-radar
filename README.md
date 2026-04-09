# repo-radar

**repo-radar** is a compact screening tool for evaluating whether a GitHub repository, issue, or paid task is worth your engineering time.

It is built for a practical question that appears before almost every serious contribution or paid delivery decision:
- Is this repo active enough to matter?
- Is the task clear enough to implement safely?
- Is the likely reward aligned with the work?
- Is this worth forking and investing time in?

---

## Why this project matters
A large amount of engineering time is wasted on low-signal repositories, vague issues, abandoned projects, and underpriced tasks.

`repo-radar` is meant to make that first-pass judgment more systematic.

Instead of relying purely on intuition, the tool aims to help engineers and technical freelancers score signals such as:
- repository freshness
- documentation quality
- issue clarity
- delivery likelihood
- workflow maturity
- likely ROI for taking the task

---

## Current capabilities
- simple repository scoring logic
- lightweight CLI scaffold
- minimal testable package structure

### Current CLI
```bash
repo-radar --has-readme --recently-updated --has-issues --has-ci-hint
```

---

## Roadmap
### v0.1
- [x] basic repository scoring model
- [x] CLI scaffold
- [x] minimal tests

### v0.2
- [ ] score repositories from GitHub metadata automatically
- [ ] summarize freshness and basic activity signals
- [ ] add issue/task screening heuristics
- [ ] output human-readable recommendation summaries

### v0.3
- [ ] compare multiple repositories side by side
- [ ] compute task-risk and reward-fit hints
- [ ] export structured JSON reports
- [ ] support screening for paid GitHub task workflows

### v0.4
- [ ] user-defined weighting models
- [ ] candidate task ranking
- [ ] CLI presets for freelancer / bounty / OSS contribution workflows
- [ ] simple dashboard or report view

---

## Example use cases
- deciding whether a GitHub task is worth taking
- screening repositories before making a fork
- comparing multiple paid tasks for ROI
- building a repeatable repo-evaluation workflow
- reducing time spent on abandoned or low-value projects

---

## Design principles
- **fast triage**: answer “worth it or not?” quickly
- **signal over hype**: reward real project quality indicators
- **scriptable**: useful in automation and CLI workflows
- **extensible**: small base model, room for richer heuristics later

---

## Project status
This repository is intentionally early, but the direction is concrete: a practical tool for technical opportunity evaluation and repository triage.

For engineers who work through GitHub issues, bounties, client repos, or fast-moving open-source tasks, this project aims to become a useful front-door filter.

---

## Tech
- Python 3.11+
- standard library first
- built for scripting and extension
