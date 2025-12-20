# Monitoring Stack (Grafana, Prometheus, Loki)
This repository provides a complete **monitoring and logging stack** using **Docker Compose**, suitable for infrastructure and cloud environments.

## 🧱 Stack Overview
- **Grafana** – Metrics & logs visualization
- **Prometheus** – Metrics collection and storage
- **Loki** – Log aggregation system
- **Promtail** – Log collector for Loki

This setup is commonly used for **infrastructure monitoring, observability, and troubleshooting**.
## 📂 Project Structure

  monitoring-stack/
  ├── docker-compose.yml
  ├── prometheus/
  │ └── prometheus.yml
  ├── grafana/
  │ └── provisioning/
  ├── loki/
  │ └── loki-config.yml
  └── promtail/
  └── promtail-config.yml


## 🚀 How to Run
Make sure Docker and Docker Compose are installed.
  docker compose up -d

| Service    | URL                                            |
| ---------- | ---------------------------------------------- |
| Grafana    | [http://localhost:3000](http://localhost:3000) |
| Prometheus | [http://localhost:9090](http://localhost:9090) |
| Loki       | [http://localhost:3100](http://localhost:3100) |

Grafana default login:
  Username: admin
  Password: admin

📊 Features
  Centralized metrics monitoring with Prometheus
  Log aggregation using Loki & Promtail
  Visualization and dashboards via Grafana
  Docker Compose based deployment (easy to setup & maintain)

🎯 Use Cases
  Infrastructure monitoring
  Application observability
  Log analysis and troubleshooting
  Learning and lab environment for DevOps / Cloud Engineers

⚠️ Notes
  This setup is intended for development and learning purposes
  Not hardened for production use
  For production, consider:
  Authentication & security
  Persistent storage
  Alertmanager integration
