from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse

base_path = "monolith/"
router = APIRouter()


@router.get("/", response_description="API Home")
async def api_home():
    """
    Home route for the API.
    Returns a simple HTML response with a link to the API documentation.
    """
    html_content = None
    with open(base_path + "templates/API.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)
