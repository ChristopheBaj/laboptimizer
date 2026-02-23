from fastapi.testclient import TestClient

from app.main import app


def test_health():
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_optimize_random():
    client = TestClient(app)
    r = client.post("/optimize/random")
    assert r.status_code == 200
    data = r.json()
    assert "best_x" in data
    assert "best_y" in data
    assert data["best_y"] >= 0.0
