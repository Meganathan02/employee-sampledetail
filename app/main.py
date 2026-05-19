from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Employee Management API",
    description="CRUD API using FastAPI + MongoDB"
)

app.include_router(router)