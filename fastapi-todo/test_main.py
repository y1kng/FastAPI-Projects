from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)                                                  

def test_a_post():
    new_todo = {
        "id": 1,                    
        "title": "I like mango",   
        "is_done": True
    }
    res = client.post("/todos", json=new_todo) 
    assert res.status_code == 200
    assert res.json() == new_todo


def test_b_get_all():
    res = client.get("/todos")                                           
    assert res.status_code == 200                    
    assert isinstance(res.json(), list)       
    
def test_c_get_vip():
    res = client.get("/todos/1") 
    assert res.status_code == 200
    assert isinstance(res.json(), dict)   

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