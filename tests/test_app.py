from app.app import app


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Hello from the Python practice project!"}


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
