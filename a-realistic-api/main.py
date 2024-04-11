import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from views import home

app = fastapi.FastAPI()


def configure():
    configure_routing()


def configure_routing():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(weather_api.router)
    app.include_router(home.router)


if __name__ == "__main__":
    configure()
    uvicorn.run("main:app", reload=True)
else:
    configure()
