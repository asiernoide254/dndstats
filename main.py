from fastapi import FastAPI, staticfiles, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import random

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    resultados = []
    for i in range(6):
        dados = [random.randint(1, 6) for i in range(4)]  # Lanza 4 dados de 6 caras
        dados.remove(min(dados)) # Borra el menor resultado
        resultado = sum(dados)  # Suma los valores restantes de los dados
        resultados.append(resultado)
    return templates.TemplateResponse("index.html", {"request": request, "resultados": resultados})

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")