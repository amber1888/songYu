# !/usr/bin/python3
# -*- coding: utf8 -*-

from pydantic import BaseModel


class ManHuaModel(BaseModel):
    album_id: str

class SearchTag(BaseModel):
    tag: str
    page: int = 1
