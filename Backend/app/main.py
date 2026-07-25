from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine, Base

# Models
from app.models.student import Student
from app.models.track import Track
from app.models.team import Team
from app.models.team_member import TeamMember
from app.models.admin import Admin

# Routers
from app.routers.student import router as student_router
from app.routers.team import router as team_router
from app.routers.dashboard import router as dashboard_router
from app.routers.admin import router as admin_router
from app.routers.csv import router as csv_router
from app.routers.excel import router as excel_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TeamSync API",
    description="Automated Team Allocation System",
    version="1.0.0"
)

# =========================
# CORS Configuration
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://*.vercel.app",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Root Endpoint
# =========================
@app.get("/")
def home():
    return {
        "message": "🚀 Welcome to TeamSync Backend",
        "status": "Running Successfully"
    }

# =========================
# Routers
# =========================
app.include_router(student_router, prefix="/students", tags=["Students"])
app.include_router(team_router, prefix="/teams", tags=["Teams"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(csv_router, prefix="/csv", tags=["CSV Import"])
app.include_router(excel_router, prefix="/excel", tags=["Excel Export"])
