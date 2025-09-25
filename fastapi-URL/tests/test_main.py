def test_a_post(url_data):
    assert url_data["count_c"] == 0
    assert isinstance(url_data["short_one"], str)
    assert url_data["id"] == 1
    assert isinstance(url_data["created_time"], str)
    
def test_b_get_ori(client, short_code):
    res = client.get(f"/api/original/{short_code}")       
    assert res.status_code == 200
    data = res.json()
    assert data["ori_url"] == "https://www.amazon.com/"
    
    res = client.get("/api/original/7")
    assert res.status_code == 404

def test_c_count(client, short_code):
    res = client.put(f"/api/click/{short_code}")
    assert res.status_code == 200
    data = res.json()
    assert data["count_c"] == 1

    res = client.put("/api/click/3")
    assert res.status_code == 404

def test_d_all_short(client):
    res = client.get("/api/allshort")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    assert all(isinstance(x, str) for x in res.json())
    assert len(res.json()) > 0