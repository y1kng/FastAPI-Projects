import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, get_db

POSTGRE_TEST = "postgresql+psycopg://isaactiger@localhost:5432/fastapi_url_test"
engine = create_engine(POSTGRE_TEST)
SessionTest = sessionmaker(bind=engine, autocommit=False, autoflush=False)

@pytest.fixture(scope="module")
def db_session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionTest()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture(scope="module")
def client(db_session):
    def replace_get_db():
        try:
            yield db_session
        finally:
            pass
    app.dependency_overrides[get_db] = replace_get_db
    yield TestClient(app)

@pytest.fixture(scope="module")
def url_data(client):
    uCheck = {
        "ori_url": "https://www.amazon.com/"
    }
    res = client.post("/api/shorten", json=uCheck)
    assert res.status_code == 200
    return res.json()

@pytest.fixture(scope="module")
def short_code(url_data):
    return url_data["short_one"]