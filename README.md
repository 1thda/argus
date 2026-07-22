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

**Without Docker:**
```powershell
cd backend
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```
Visit `http://127.0.0.1:8000/health` — should return `{"status":"ok"}`.

**With Docker:**
```powershell
cd backend
docker build -t argus-backend .
docker run -p 8000:8000 argus-backend
```
Visit `http://localhost:8000/health` — should return `{"status":"ok"}`.