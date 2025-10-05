from typing import List          
from .models import Todo

todo_list: List[Todo] = []   # in-memory list storing Todos

def get_all_todos() -> List[Todo]:  # Return all Todo items
    return todo_list

def get_some_todos(todo_id: int) -> Todo | None:  # Return a single Todo item by ID, or None if not found
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    return None

def want_add_something(todo: Todo) -> None:  # Add a new Todo item to the list
    todo_list.append(todo)            

def want_update_something(todo_id: int, new_todo: Todo) -> bool:  # Update an existing Todo item by ID
    for i, j in enumerate(todo_list):           
        if j.id == todo_id:
            todo_list[i] = new_todo         
            return True
    return False

def want_del_something(todo_id: int) -> bool:   # Delete a Todo item by ID
    for i, j in enumerate(todo_list):
        if j.id == todo_id:
            del todo_list[i]         
            return True
    return False


