from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_auth import router as auth_router
from app.api.routes_health import router as health_router
from app.api.routes_projects import router as projects_router
from app.core.database import Base, engine
import app.models  # noqa: F401


app = FastAPI(title="VYBEFORGE API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(projects_router)


@app.get("/")
def root():
    return {
        "message": "VYBEFORGE API is running",
        "docs": "/docs"
    }
