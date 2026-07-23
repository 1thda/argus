# Argus

Production-style AI incident platform, built as a portfolio project.

**Stack (target):** FastAPI + React + Postgres, Amazon Bedrock (AI incident copilot),
ECS Fargate → EKS migration, Terraform IaC, ArgoCD/Helm, Prometheus/Grafana, GitHub Actions CI/CD.

## Status
🚧 Phase 1 in progress — app skeleton + ECS Fargate via Terraform.

## Structure
backend/ FastAPI service
frontend/ React app
infra/ Terraform


## Local development
### Backend (FastAPI)

### Full stack (backend + Postgres)

```powershell
cd backend
docker-compose up --build
```
Visit `http://localhost:8000/health` — should return `{"status":"ok","db":"connected"}`.

To stop:
```powershell
docker-compose down
```