# src/main.py

from fastapi import FastAPI
from src.api import roadmap_routes
from src.api import json_extractor_routes # <-- 1. IMPORT THE NEW ROUTER

app = FastAPI(
    title="AI Agent API",
    description="An API for generating learning roadmaps and other AI-powered tools."
)

# Include your existing and new routers
app.include_router(roadmap_routes.router, prefix="/roadmap", tags=["Learning Roadmap"])
app.include_router(json_extractor_routes.router, prefix="/tools", tags=["Content Tools"]) # <-- 2. INCLUDE THE NEW ROUTER

@app.get("/", tags=["Root"])
def read_root():
    """A simple welcome message for the API root."""
    return {"message": "Welcome to the AI Agent API"}