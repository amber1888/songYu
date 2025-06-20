
import logging

from fastapi import FastAPI
from utils.log import log_init
from model.manhua import ManHuaModel, SearchTag
from service.jm import ManHuaService

log_init()
logger = logging.getLogger(__name__)
app = FastAPI()

@app.post("/download-album")
async def download_album(album: ManHuaModel):
    return ManHuaService.add(album)

@app.post("/query-album")
async def query_album(album: SearchTag):
    return ManHuaService.search(album)
