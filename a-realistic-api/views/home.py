import fastapi
from starlette.templating import Jinja2Templates
from starlette.requests import Request

router = fastapi.APIRouter()
templates = Jinja2Templates("templates")


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("home/index.html", {"request": request})
