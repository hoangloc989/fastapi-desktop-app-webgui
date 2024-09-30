import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.webgui import GUI, close_application

app = FastAPI()

base_path = os.path.dirname(__file__)  # Regular Python script

# Mounting static files
app.mount("/public", StaticFiles(directory=os.path.join(base_path, "public")), name="public")
templates = Jinja2Templates(directory=os.path.join(base_path, "templates"))

@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    return response

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/navbar", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("navbar.html", {"request": request})

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/features", response_class=HTMLResponse)
async def table(request: Request):
    return templates.TemplateResponse("features.html", {"request": request})

@app.get("/forms", response_class=HTMLResponse)
async def table(request: Request):
    return templates.TemplateResponse("forms.html", {"request": request})

@app.get("/table", response_class=HTMLResponse)
async def table(request: Request):
    return templates.TemplateResponse("table.html", {"request": request})

@app.get("/jumbotron", response_class=HTMLResponse)
async def table(request: Request):
    return templates.TemplateResponse("jumbotron.html", {"request": request})

@app.get("/close")
async def close_server():
    close_application()

def start_fastapi(**kwargs):
    import uvicorn
    uvicorn.run(**kwargs)

if __name__ == "__main__":
    # Default start fastapi
    GUI(
        app=app,
        server="fastapi",    
        server_kwargs={
            "app": "main:app",
            "port": 3000,
        },
        width=1024,
        height=600,
    ).run()