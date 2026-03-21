import pytest

def test_get_inventory_paginated(client):
    """Test retrieving a paginated list of inventory items."""
    response = client.get("/inventory?limit=5&offset=0")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    assert isinstance(data["items"], list)
    assert len(data["items"]) <= 5