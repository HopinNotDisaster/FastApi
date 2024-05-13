from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Book(BaseModel):
    title: str
    info: Union[str, None] = None


books = []
app = FastAPI()


@app.get("/")
def index():
    return {
        "msg": "欢迎来到首页！"
    }


@app.get("/books")
def book_list():
    return {
        "msg": "欢迎来到图书列表页！",
        'books': []
    }


# 在写参数时，先写path参数，再写post和put的参数，最后写query参数。
@app.post("/books")
def create_book(b: Book):
    return {
        "msg": "欢迎创建图书！",
        'data': b
    }


@app.delete("/books/{bid}/")
def delete_book(bid: int):
    return {
        "msg": "删除图书成功！",
    }
