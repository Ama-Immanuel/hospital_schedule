import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.requests import Request

from config import cfg
from routes import route_home

app = FastAPI()
# Load dotenv
app.include_router(route_home)


@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return RedirectResponse('https://fastapi.tiangolo.com')


if __name__ == "__main__":
    uvicorn.run(app, host=cfg.server_host, port=cfg.server_port)
