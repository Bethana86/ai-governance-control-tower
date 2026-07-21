import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api import router_gateway, router_audit, router_telemetry

def create_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="Enterprise Modular Policy & Regulatory Compliance Engine"
    )

    # CORS Setup
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API Routers
    app.include_router(router_gateway.router, prefix=settings.API_PREFIX)
    app.include_router(router_audit.router, prefix=settings.API_PREFIX)
    app.include_router(router_telemetry.router, prefix=settings.API_PREFIX)

    # Root UI Static Files Mount
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @app.get("/", response_class=HTMLResponse)
    async def root_view():
        index_path = os.path.join(workspace_dir, "index.html")
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                return HTMLResponse(content=f.read())
        return HTMLResponse("<h1>Agent Policy and Compliance Tower - Modular App Running</h1>")

    app.mount("/", StaticFiles(directory=workspace_dir, html=True), name="static")

    return app

app = create_application()
