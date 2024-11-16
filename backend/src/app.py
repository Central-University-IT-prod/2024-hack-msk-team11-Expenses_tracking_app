from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from backend.src.utilites.events import (
    execute_backend_server_event_handler as db_execute,
)
from backend.src.api.endpoints.events import router as event_router
from backend.src.api.endpoints.obligations import router as obligations_router
from backend.src.api.endpoints.tg import router as tg_router
from backend.src.api.endpoints.users import router as users_router


app = FastAPI(root_path="/api")

app.include_router(router=event_router)
app.include_router(router=obligations_router)
app.include_router(router=tg_router)
app.include_router(router=users_router)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler(
    "startup",
    db_execute(backend_app=app),
)

@app.get('/', response_class=RedirectResponse)
async def redirect_to_index():
    return '/docs'


if __name__ == "__main__":
    uvicorn.run(app=app, port=8000)
