import fastapi
import uvicorn
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

app = fastapi.FastAPI()
templates = Jinja2Templates("templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("home/index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
