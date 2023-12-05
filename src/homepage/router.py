from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix='',
    tags=['home']
)

templates = Jinja2Templates(directory='templates')

@router.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
