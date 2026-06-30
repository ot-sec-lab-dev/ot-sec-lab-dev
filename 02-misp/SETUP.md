\# MISP — Phase 2 ✅ Deployed



\*\*Status:\*\* Live and operational on a dedicated Hetzner Cloud VPS.



\## Why a separate VPS



MISP's Docker stack (MariaDB, Redis/Valkey, MISP core, MISP modules) needs more headroom than was safely available on the primary working machine. Rather than risk degrading a corporate laptop's performance, this phase runs on a small dedicated cloud server — isolated, disposable, and reproducible.



\## Infrastructure



| Item | Value |

|---|---|

| Provider | Hetzner Cloud |

| Server type | CX33 |

| Specs | 4 vCPU, 8 GB RAM, 80 GB NVMe |

| Location | Falkenstein, Germany |

| OS | Ubuntu 26.04 LTS |

| Cost | \~€10/month (billed hourly, stoppable anytime) |



\## Deployment steps



```bash

\# On the server, as root

apt update \&\& apt upgrade -y

curl -fsSL https://get.docker.com -o get-docker.sh \&\& sh get-docker.sh



git clone https://github.com/MISP/misp-docker.git

cd misp-docker

cp template.env .env

\# Edit .env: BASE\_URL, ADMIN\_EMAIL, ADMIN\_PASSWORD, ADMIN\_ORG,

\# MYSQL\_PASSWORD, MYSQL\_ROOT\_PASSWORD, REDIS\_PASSWORD



docker compose pull

docker compose up -d

docker compose ps   # confirm all services report "healthy"

```



First boot takes a few minutes for MariaDB initialization and the MISP install scripts to run.



\## Access



\- URL: `https://<server-ip>` (self-signed cert — browser warning expected on first visit)

\- Login with the `ADMIN\_EMAIL` / `ADMIN\_PASSWORD` set during configuration



\## What's configured



\- Admin account and organization (`OT-SEC-LAB`) created

\- API authentication key generated (for future n8n / OpenCTI integration)



\## Next steps



\- \[ ] Enable ICS-relevant taxonomies (`mitre-attack-ics`) under Sync Actions → Taxonomies

\- \[ ] Build an n8n workflow that pushes Feodo Tracker IOCs into MISP via its REST API, using the Phase 1 collector as the source

\- \[ ] Move on to \[Phase 3 — TheHive](../03-thehive/SETUP.md) once this integration is documented



\## Resource note



This VPS is dedicated to MISP for now. When Phase 3 (TheHive) starts, it will get the same treatment — either a second server, or this one upgraded, depending on cost vs. complexity trade-offs at that point.

