import pytest

def test_update_inventory_stock(client):
    """Test updating the stock level for an existing SKU."""
    update_payload = {"total_stock": 250}
    response = client.patch("/inventory/WJK01", json=update_payload)
    assert response.status_code == 200
    
    # Verify the update was applied
    get_response = client.get("/inventory/WJK01")
    assert get_response.json()["total_stock"] == 250