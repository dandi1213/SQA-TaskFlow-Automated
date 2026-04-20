import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_task():
    payload = {"title": "Test Task", "description": "Desc", "status": "todo"}
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"

def test_update_task():
    create = client.post("/tasks", json={"title": "Old", "status": "todo"})
    task_id = create.json()["id"]
    update = client.put(f"/tasks/{task_id}", json={"title": "New", "status": "done"})
    assert update.status_code == 200
    assert update.json()["title"] == "New"

def test_delete_task():
    create = client.post("/tasks", json={"title": "To Delete", "status": "todo"})
    task_id = create.json()["id"]
    delete = client.delete(f"/tasks/{task_id}")
    assert delete.status_code == 200
