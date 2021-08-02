from fastapi import FastAPI, Response
import uvicorn
import os
import sys
from fastapi.responses import StreamingResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#@app.get("/items/{id}", response_class=HTMLResponse)
#async def read_item(request: Request, id: str):
#    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.get("/video/{file_path}")
def main(file_path: str):
    PATH = 'video'
    vid_path = os.path.join(PATH, file_path)
    def iterfile():  
        with open(vid_path, mode="rb") as file:  
            yield from file 
    return StreamingResponse(iterfile(), media_type="video/mp4")

@app.get("/file/{file_path}", response_class=FileResponse)
async def main(file_path: str):
    PATH = 'file'
    return os.path.join(PATH, file_path)

if __name__=="__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=1234, debug=True, reload=True)