from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)


def get_token():
    response = client.post("/register", json={"email": "user@example.com", "password": "pass"})
    assert response.status_code == 200
    response = client.post("/token", data={"username": "user@example.com", "password": "pass"})
    assert response.status_code == 200
    return response.json()["access_token"]


def test_create_and_list_tenders():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/tenders", json={"title": "Tender 1"}, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Tender 1"

    response = client.get("/tenders", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
