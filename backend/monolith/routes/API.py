from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse

base_path = "backend/monolith/"
router = APIRouter()


@router.get("/", summary="API Home")
async def api_home():
    """
    Home route for the API. \n
    Returns a simple HTML response with a link to the API documentation.
    and 200 status code. \n
    """
    html_content = None
    with open(base_path + "templates/API.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)
