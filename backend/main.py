from fastapi import FastAPI
from sqlalchemy import text
from database import engine, SessionLocal, Base
import models  # noqa: F401

app = FastAPI()

try:
    Base.metadata.create_all(bind=engine)
except Exception:
    pass  # DB may not be ready at startup; /health will report this

@app.get("/health")
def health():
    try:
        with SessionLocal() as session:
            session.execute(text("SELECT 1"))
        return {"status": "ok", "db": "connected"}
    except Exception:
        return {"status": "degraded", "db": "unreachable"}