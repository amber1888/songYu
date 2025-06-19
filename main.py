
import logging

from pydantic import BaseModel
from config import settings
from fastapi import FastAPI
from jmcomic import *
from jmcomic import jm_log
from utils.log import log_init
from model.manhua import ManHuaModel
from service.jm import ManHuaService

log_init()
logger = logging.getLogger(__name__)
app = FastAPI()

@app.post("/download-album")
async def download_album(album: ManHuaModel):
    return ManHuaService.add(album)
