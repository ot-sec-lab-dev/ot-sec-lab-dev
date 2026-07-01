\# TheHive + Cortex — Phase 3 ✅ Deployed



\*\*Status:\*\* Live and operational on the same Hetzner Cloud VPS as MISP (port 8443 to avoid conflict).



\## Infrastructure



| Item | Value |

|---|---|

| Provider | Hetzner Cloud |

| Server | Same CX33 as MISP (4 vCPU, 8 GB RAM, 80 GB NVMe) |

| Location | Falkenstein, Germany |

| OS | Ubuntu 26.04 LTS |

| URL | https://<server-ip>:8443/thehive |



\## Deployment notes



TheHive's official testing environment (`github.com/StrangeBeeCorp/docker`) was used — it ships a 14-day Platinum trial license and pre-loads sample data (cases, alerts, observables, MITRE ATT\&CK taxonomies, Cortex analyzers).



\### Key issues resolved during deployment



\*\*1. Elasticsearch refused to start as root\*\*

The `UID` variable in `.env` was overridden by Bash's read-only `UID=0` (root). Fixed by passing it explicitly at runtime:

```bash

env UID=1000 GID=1000 docker compose up -d

```



\*\*2. Port 443 conflict with MISP\*\*

Both MISP and TheHive's nginx tried to bind port 443. Fixed by changing TheHive's nginx port in `docker-compose.yml`:

```yaml

ports:

&#x20; - '8443:443'

```



\*\*3. Init scripts pointed to wrong port\*\*

`test\_init\_cortex.sh` and `test\_init\_thehive.sh` had hardcoded `https://127.0.0.1/cortex` and `https://127.0.0.1/thehive`. Fixed with:

```bash

sed -i 's|https://127.0.0.1/cortex|https://127.0.0.1:8443/cortex|g' ./scripts/test\_init\_cortex.sh

sed -i 's|https://127.0.0.1/thehive|https://127.0.0.1:8443/thehive|g' ./scripts/test\_init\_thehive.sh

```



\*\*4. Missing `jq` dependency\*\*

```bash

apt install -y jq

```



\## Deployment steps



```bash

git clone https://github.com/StrangeBeeCorp/docker.git thehive-docker

cd thehive-docker/testing

bash ./scripts/init.sh          # accept default hostname, generate self-signed certs

chown -R 1000:1000 elasticsearch thehive cortex cassandra

env UID=1000 GID=1000 docker compose up -d

apt install -y jq

\# Apply port fixes to init scripts (see above)

bash ./scripts/test\_init\_applications.sh

```



\## Access



| App | URL | User | Password |

|---|---|---|---|

| TheHive | https://\\<ip\\>:8443/thehive | `admin@thehive.local` | `secret` |

| TheHive (org) | https://\\<ip\\>:8443/thehive | `thehive@thehive.local` | `thehive1234` |

| Cortex | https://\\<ip\\>:8443/cortex | `admin` | `thehive1234` |



\## What's configured



\- TheHive initialized with demo organization, sample cases, alerts, and observables

\- Cortex initialized with multiple analyzers enabled (Abuse Finder, MaxMind GeoIP, URLScan, etc.)

\- TheHive integrated with Cortex for automated analysis



\## Next steps



\- \[ ] Create a TheHive alert from a MISP event via n8n automation

\- \[ ] Run a Cortex analyzer on an observable (IP from Feodo Tracker IOCs)

\- \[ ] Move on to \[Phase 4 — OpenCTI](../04-opencti/SETUP.md)

