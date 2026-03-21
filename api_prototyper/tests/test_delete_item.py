import pytest

def test_delete_inventory_item(client):
    """Test removing a SKU and verifying its deletion."""
    # Ensure item exists before deletion
    sku_to_delete = "TEMP-SKU-99"
    client.post("/inventory", json={"sku": sku_to_delete, "name": "Temporary Item"})
    
    # Delete the item
    delete_res = client.delete(f"/inventory/{sku_to_delete}")
    assert delete_res.status_code == 204
    
    # Confirm 404 on subsequent lookup
    verify_res = client.get(f"/inventory/{sku_to_delete}")
    assert verify_res.status_code == 404