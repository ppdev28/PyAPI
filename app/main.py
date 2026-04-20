from fastapi import FastAPI

from app.api.routes.items import router as items_router

app = FastAPI(title="API CRUD Sencilla")


@app.get("/")
def home() -> dict[str, str]:
    return {"mensaje": "API CRUD activa"}


app.include_router(items_router)
