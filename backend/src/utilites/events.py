import typing
import fastapi
from backend.src.database.events import init_db_connection

def execute_backend_server_event_handler(backend_app: fastapi.FastAPI) -> typing.Any:
    async def launch_backend_server_events() -> None:
        await init_db_connection(backend_app=backend_app)

    return launch_backend_server_events
