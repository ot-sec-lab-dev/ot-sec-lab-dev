# OT/ICS Cybersecurity & Threat Intelligence Lab

> Practical cybersecurity laboratory focused on Operational Technology (OT), Industrial Control Systems (ICS), threat intelligence, security assessments and automation.

## Overview

This repository documents the development of a practical OT/ICS cybersecurity laboratory and the security capabilities being developed around Sentra OT.

The objective is to combine threat intelligence, incident response, OT security assessment methodologies and automation into reusable technical assets for industrial and critical infrastructure environments.

The lab is designed as a hands-on environment for testing technologies, documenting security workflows and developing practical cybersecurity assessment capabilities.

---

## What This Lab Demonstrates

The project focuses on several areas of OT/ICS cybersecurity:

- OT/ICS threat intelligence
- IOC collection and processing
- Threat intelligence platforms
- Incident response workflows
- OT security assessments
- Risk identification and prioritisation
- Network segmentation review
- OT architecture assessment
- Security maturity and gap analysis
- Security automation
- Cybersecurity reporting and remediation roadmaps

The repository contains both technical laboratory components and reusable assessment/product documentation.

---

## Technology Stack

### Threat Intelligence

- MISP
- OpenCTI
- Feodo Tracker

### Incident Response

- TheHive
- Cortex

### Automation

- n8n

### Infrastructure

- Docker
- PostgreSQL
- Redis
- RabbitMQ
- Elasticsearch

### OT/ICS Security Frameworks

- IEC 62443
- NIST SP 800-82
- MITRE ATT&CK for ICS

---

# Laboratory Components

## 01 — n8n

The automation component of the laboratory.

Current work includes an IOC collection workflow using Feodo Tracker.

The workflow demonstrates how threat intelligence data can be collected and processed automatically as part of an OT/ICS security workflow.

Directory:

```text
01-n8n/