from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Base directory configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Frontend/my-website

# Template configuration
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
templates.env.loader.searchpath.append(os.path.join(BASE_DIR, "components"))  # Add components

# Mount static directories
app.mount("/styles", StaticFiles(directory=os.path.join(BASE_DIR, "styles")), name="styles")
app.mount("/assets", StaticFiles(directory=os.path.join(BASE_DIR, "assets")), name="assets")
app.mount("/scripts", StaticFiles(directory=os.path.join(BASE_DIR, "scripts")), name="scripts")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat")
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})