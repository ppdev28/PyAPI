from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.routes.items import router as items_router

app = FastAPI(title="API CRUD Sencilla")


@app.get("/")
def home() -> dict[str, str]:
    return {"mensaje": "API CRUD activa"}


app.include_router(items_router)

Instrumentator().instrument(app).expose(app, include_in_schema=False)
