from typing import Optional
from fastapi import FastAPI, Request, Header, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.post("/upload")
async def upload_file(file: UploadFile):
  print(file.filename)


@app.get("/", response_class=HTMLResponse)
async def movielist(request: Request,
                    hx_request: Optional[str] = Header(None)):
  films = [
    {
      'name': 'Blade Runner',
      'director': 'Ridley Scott'
    },
    {
      'name': 'Pulp Fiction',
      'director': 'Quentin Tarantino'
    },
    {
      'name': 'Mulholland Drive',
      'director': 'David Lynch'
    },
  ]
  context = {"request": request, 'films': films}
  if hx_request:
    return templates.TemplateResponse("partials/table.html", context)
  return templates.TemplateResponse("index.html", context)


# test