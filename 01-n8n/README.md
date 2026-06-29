\# 01 - n8n IOC Collector (Feodo Tracker)



\## Overview



This module is the first building block of the \*\*OT/ICS Threat Intelligence Lab\*\*.



It demonstrates how to automate the collection of Indicators of Compromise (IOCs) from the public \*\*Feodo Tracker (abuse.ch)\*\* feed using \*\*n8n\*\* running inside Docker.



The workflow serves as the foundation for future integrations with \*\*MISP\*\*, \*\*OpenCTI\*\*, and \*\*TheHive\*\*, enabling automated threat intelligence collection and processing.





\# Phase 1 — n8n IOC Collector



Automated threat intelligence collection using n8n as the orchestration layer. This is the first phase of the OT/ICS threat intelligence lab.



\## What this workflow does



Connects to the \[Feodo Tracker](https://feodotracker.abuse.ch/) public API (abuse.ch) and pulls a live list of botnet C2 servers — IPs associated with active malware families such as Emotet, QakBot, and Cobalt Strike. The data is normalized into a clean, structured format ready for ingestion into MISP (Phase 2).



\## Workflow: IOC Collector - Feodo Tracker



\*\*File:\*\* `ioc-collector-feodo-tracker.json`



\*\*Nodes:\*\*



| Step | Node | Description |

|---|---|---|

| 1 | Manual Trigger | Starts the workflow on demand |

| 2 | HTTP Request | Fetches live C2 IOCs from Feodo Tracker API |

| 3 | Edit Fields | Normalizes output: ip, malware, estado, pais |



\*\*Sample output:\*\*



| ip | malware | estado | pais |

|---|---|---|---|

| 50.16.16.211 | QakBot | online | US |

| 178.62.3.223 | QakBot | offline | GB |

| 27.133.154.218 | QakBot | offline | JP |



\## How to run



\### Prerequisites

\- Docker Desktop running

\- WSL2 enabled



\### Start n8n



```bash

cd 01-n8n

docker compose up -d

```



Access n8n at `http://localhost:5678`



\### Import the workflow



1\. Log in to n8n

2\. Click \*\*+\*\* → \*\*Import from file\*\*

3\. Select `ioc-collector-feodo-tracker.json`

4\. Click \*\*Execute workflow\*\*



\### Stop n8n



```bash

docker compose down

```



\## Next phase



\[Phase 2 — MISP](../02-misp/SETUP.md): IOC sharing and tagging platform. The output of this workflow will be pushed directly into MISP via its API.

