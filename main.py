
import logging

from config import settings
from fastapi import FastAPI
from utils.log import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
