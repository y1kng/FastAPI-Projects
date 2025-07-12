from fastapi import APIRouter, HTTPException     # 1️⃣ not "HttpException" , is "HTTPException"  2️⃣ not "RouterAPI", is "APIRouter"
from typing import List

from .models import Todo
from .db import get_all_todos, get_some_todos, want_add_something, want_update_something, want_del_something  # not "get_some_todos()", just "get_some_todos"

router = APIRouter()      # not "route", is "router"

@router.get("/todos", response_model=List[Todo])    # not "@route.xx", is "@router.xx"  (Apply globally in this file)
def call_get_all():
    return get_all_todos()

@router.get("/todos/{todo_id}", response_model=Todo)
def call_getsome(todo_id: int):
    wyk = get_some_todos(todo_id)
    if wyk is None:
        raise HTTPException(status_code=404, detail="Can't find what u want")  # not "message=", is "detail="
    return wyk

@router.post("/todos", response_model=Todo)
def call_addsome(todo: Todo):
    want_add_something(todo)   # Call directly, no need to assign (like no ly = xxx())
    return todo

@router.put("/todos/{todo_id}", response_model=Todo)
def call_update(todo_id: int, new_todo: Todo):
    ydy = want_update_something(todo_id, new_todo)
    if not ydy:
        raise HTTPException(status_code=404, detail="Update failed")
    return new_todo 

@router.delete("/todos/{todo_id}")
def call_del(todo_id: int):
    lcc = want_del_something(todo_id)
    if not lcc:
        raise HTTPException(status_code=404, detail="The item u were tryna delete does not exist")
    return {"James": "Mission Accomplished!"}  # Should use "message", this time i use "James" just for test purpose 