# Sentra OT Assessment V1 — Scoring Model

## Overview

The Sentra OT Security Assessment V1 calculates an OT Risk Score from 0 to 100.

A higher score indicates greater cybersecurity exposure.

The V1 assessment evaluates five areas:

- Architecture
- Network Security
- Identity & Access
- Asset Visibility
- Monitoring

Vulnerability Management, Incident Response and Compliance are not included in V1.

---

## Risk Score

| Score | Risk Level |
|---:|---|
| 0–20 | Excellent |
| 21–40 | Good |
| 41–60 | Needs Improvement |
| 61–80 | High Risk |
| 81–100 | Critical Risk |

---

# 1. Architecture

Maximum weighted score: **25 points**

Maximum raw score: **28 points**

| Rule | Condition | Raw Score |
|---|---|---:|
| ARQ-001 | Purdue Model not implemented | 10 |
| ARQ-002 | No OT DMZ | 8 |
| ARQ-003 | Flat OT network | 10 |

### Weighted Score

```text
Architecture Score = (Raw Score / 28) × 25