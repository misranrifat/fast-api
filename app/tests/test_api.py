from fastapi.testclient import TestClient
import pytest

from app.main import app

client = TestClient(app)


def create_test_item():
    """Helper function to create a test item and return its ID"""
    response = client.post(
        "/api/v1/items/",
        json={"title": "Test Item", "description": "This is a test item"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    return data["id"]


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI CRUD Demo"}


def test_create_item():
    response = client.post(
        "/api/v1/items/",
        json={"title": "Test Item", "description": "This is a test item"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["description"] == "This is a test item"
    assert "id" in data


def test_read_item():
    item_id = create_test_item()
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["description"] == "This is a test item"
    assert data["id"] == item_id


def test_read_items():
    create_test_item()
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_update_item():
    item_id = create_test_item()
    response = client.put(
        f"/api/v1/items/{item_id}",
        json={"title": "Updated Item", "description": "This is an updated item"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Item"
    assert data["description"] == "This is an updated item"
    assert data["id"] == item_id


def test_delete_item():
    item_id = create_test_item()
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    # Check if the item is actually deleted
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 404


def test_delete_all_items():
    # Create multiple items
    create_test_item()
    create_test_item()
    create_test_item()
    
    # Check that items exist
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    
    # Delete all items
    response = client.delete("/api/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert "deleted_count" in data
    assert data["deleted_count"] > 0
    
    # Verify all items are deleted
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert len(response.json()) == 0 