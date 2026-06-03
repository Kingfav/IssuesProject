from fastapi import FastAPI
from fastapi.middleware.cors import CORSmiddleware
from app.routes.issues import router as issues_router
from app.middleware.timing import timing_middleware
app = FastAPI(
    title="Issue Tracker API",
    version="0.1.0",
    description="A mini production-style API built with FastAPI",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(issues_router)

app.middleware("http")(timing_middleware)

app.add_middleware(CORSMIDDLEARE,
                   Allow_origins=["*"],
                   Allow_methods=["*"],
                   Allow_credentials=True,
                   Allow_headers=["*"])
