import pytest

# 1. READ (List) - Test pagination and response structure
def test_get_inventory_paginated(client):
    """Verifies that the inventory list returns paginated data."""
    response = client.get("/inventory?limit=5&offset=0")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    assert isinstance(data["items"], list)
    assert len(data["items"]) <= 5

# 2. CREATE - Test adding a new SKU to the system
def test_create_inventory_item(client):
    """Verifies that a new product SKU can be created successfully."""
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

# 3. READ (Detail) - Test fetching a specific existing SKU
def test_get_inventory_detail(client):
    """Verifies that details for a specific SKU are retrieved correctly."""
    # Assumes WJK01 is a pre-existing or seeded SKU
    response = client.get("/inventory/WJK01")
    assert response.status_code == 200
    data = response.json()
    assert data["sku"] == "WJK01"
    assert "total_stock" in data

# 4. UPDATE - Test adjusting stock levels for a SKU
def test_update_inventory_stock(client):
    """Verifies that the total_stock for a SKU can be updated."""
    update_payload = {"total_stock": 250}
    response = client.patch("/inventory/WJK01", json=update_payload)
    assert response.status_code == 200
    
    # Confirm the change persisted via a fresh GET request
    get_res = client.get("/inventory/WJK01")
    assert get_res.json()["total_stock"] == 250

# 5. DELETE - Test removing a SKU and verifying its absence
def test_delete_inventory_item(client):
    """Verifies that a SKU can be deleted and is no longer accessible."""
    # 1. Create a temporary item to ensure there is something to delete
    temp_sku = "TEMP-99"
    client.post("/inventory", json={"sku": temp_sku, "name": "Temp Item"})
    
    # 2. Delete the item
    delete_res = client.delete(f"/inventory/{temp_sku}")
    assert delete_res.status_code == 204
    
    # 3. Verify the item no longer exists (should return 404)
    verify_res = client.get(f"/inventory/{temp_sku}")
    assert verify_res.status_code == 404