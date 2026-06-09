from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.issues import router as issues_router
from app.middleware.timing import timing_middleware
app = FastAPI(
    title="Issue Tracker API",
    version="0.1.0",
    description="A mini production-style API built with FastAPI",
)


app.mount("/ui", StaticFiles(directory="ui"), name="ui")


@app.get("/")
def home():
    return FileResponse("ui/index.html")


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(issues_router)

app.middleware("http")(timing_middleware)

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_credentials=True,
                   allow_headers=["*"])
