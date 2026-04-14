from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "../templates"))

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    resultados = []
    for _ in range(6):
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.remove(min(dados))
        resultados.append(sum(dados))

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"resultados": resultados},
    )