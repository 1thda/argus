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
Visit `http://127.0.0.1:8000/health` — should return `{"status":"ok"}` (DB fields may show "unreachable" unless Postgres is also running locally).

**With Docker (backend only):**
```powershell
cd backend
docker build -t argus-backend .
docker run -p 8000:8000 argus-backend
```

### Full stack (backend + Postgres)

```powershell
cd backend
docker-compose up --build
```
Visit `http://localhost:8000/health` — should return `{"status":"ok","db":"connected"}`.

To stop:
```powershell
docker-compose down