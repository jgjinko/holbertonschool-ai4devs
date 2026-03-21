import pytest

def test_create_inventory_item(client):
    """Test creating a new SKU in the system."""
    payload = {
        "sku": "TTS-09",
        "name": "TikTok Trend Hoodie",
        "total_stock": 100,
        "channels": [{"platform": "TikTok Shop", "stock": 100}]
    }
    response = client.post("/inventory", json=payload)
    assert response.status_code == 201
    assert response.json()["sku"] == "TTS-09"
    assert response.json()["name"] == "TikTok Trend Hoodie"