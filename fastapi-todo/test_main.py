from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)                                                  # NOT: response = TestClient(app)

def test_a_post():
    new_todo = {
        "id": 1,                    #don't forget comma between each dict item!
        "title": "I like mango",   # don't forget "xx" for all keys
        "is_done": True
    }
    res = client.post("/todos", json=new_todo) # need to be json=xxx, don't forget
    assert res.status_code == 200
    assert res.json() == new_todo


def test_b_get_all():
    res = client.get("/todos")                                           # NOT: response = TestClient("todos/")
    assert res.status_code == 200                    # Note: change all "response" to "res" for consistency
    assert isinstance(res.json(), list)         # NOT: assert response.xxxx == isinstance(xxx.json, list)
    
def test_c_get_vip():
    res = client.get("/todos/1") 
    assert res.status_code == 200
    assert isinstance(res.json(), dict)    #isinstance() is func, NOT: response.instance()

    res = client.get("/todos/999")
    assert res.status_code == 404

def test_d_update():
    fresh_todo = {
        "id": 7,
        "title": "Know I can",
        "is_done": True
    }          
    res = client.put("/todos/1", json=fresh_todo)
    assert res.status_code == 200
    assert res.json() == fresh_todo

def test_e_del():
    res = client.delete("/todos/7")
    assert res.status_code == 200
    
    res = client.delete("/todos/7")
    assert res.status_code == 404