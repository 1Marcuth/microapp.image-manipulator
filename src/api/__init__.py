from fastapi import FastAPI
import asyncio
import uvicorn

from .routers.image_manipulator import image_manipulator_router
from . import settings

class App:
    _app: FastAPI
    _app_is_running: bool

    def __init__(self) -> None:
        self._app = FastAPI()
        self._use_routers()
        self._app_is_running = False

    def _use_routers(self) -> None:
        self._app.include_router(image_manipulator_router)

    def start(self) -> None:
        if self._app_is_running:
            raise Exception("Server is already running!")

        self._app_is_running = True

        uvicorn.run(
            app = self._app,
            port = settings.port,
            host = settings.host
        )

    def stop(self) -> None:
        loop = asyncio.get_event_loop()
        loop.stop()
        self._app_is_running = False