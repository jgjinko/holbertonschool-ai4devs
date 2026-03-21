import pytest

def test_get_inventory_detail(client):
    """Test retrieving details for a specific existing SKU."""
    # This assumes 'WJK01' exists in the database
    response = client.get("/inventory/WJK01")
    assert response.status_code == 200
    data = response.json()
    assert data["sku"] == "WJK01"
    assert "total_stock" in data