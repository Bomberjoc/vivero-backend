from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.routes.plants import router as plants_router
from app.routes.activity_logs import router as activity_logs_router

app = FastAPI(title="Vivero API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

app.include_router(plants_router, prefix="/plants", tags=["Plants"])
app.include_router(activity_logs_router, prefix="/activity-logs", tags=["Activity Logs"])
