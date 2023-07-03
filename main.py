from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
from uce.ai.openairepaso import Document, inference

app = FastAPI()

class Text(BaseModel):
    content: str

@app.get("/")
def reversat(texto: Text):
    reversa = texto.content[::-1]
    return {"reversa": reversa}



@app.post("/r")
def reversat(texto: Text):
    reversa = texto.content[::-1]
    return {"reversa": reversa}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}