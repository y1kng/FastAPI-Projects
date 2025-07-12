from typing import List          # "typing" Not "type"
from .models import Todo

todo_list: List[Todo] = []

def get_all_todos() -> List[Todo]:
    return todo_list

def get_some_todos(todo_id: int) -> Todo | None:  # Do not forget | None
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    return None

def want_add_something(todo: Todo) -> None:
    todo_list.append(todo)            # No return

def want_update_something(todo_id: int, new_todo: Todo) -> bool:
    for i, j in enumerate(todo_list):           #use i,j,enumerate combo
        if j.id == todo_id:
            todo_list[i] = new_todo         # "j = todo" is not going to work cause its just a copy
            return True
    return False

def want_del_something(todo_id: int) -> bool:
    for i, j in enumerate(todo_list):
        if j.id == todo_id:
            del todo_list[i]         # "del i" is not right, this is not dict, u cannot delete index
            return True
    return False


