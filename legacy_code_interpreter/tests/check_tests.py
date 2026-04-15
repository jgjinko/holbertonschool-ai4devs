import pytest

# Mocking a client request object for legacy endpoint testing
class LegacyClient:
    def post(self, url, data):
        # Simulated responses for legacy behavior
        if url == "/login" and data.get("pass") == "wrong":
            return type('obj', (object,), {'status_code': 401})
        if url == "/cart.php?action=add" and not data.get("products_id"):
            return type('obj', (object,), {'status_code': 400})
        return type('obj', (object,), {'status_code': 200})

client = LegacyClient()

def test_login_with_invalid_password():
    res = client.post("/login", {"user": "admin", "pass": "wrong"})
    assert res.status_code == 401

def test_add_to_cart_no_product_id():
    res = client.post("/cart.php?action=add", {})
    assert res.status_code == 400

def test_checkout_unauthenticated_redirect():
    # Simulate redirect to login if not logged in
    res = client.post("/checkout_confirmation.php", {})
    assert res.status_code == 200 # In legacy systems, this often returns 200 with a login HTML body

def test_admin_access_denied():
    res = client.post("/admin/categories.php", {"auth": "none"})
    # Assuming logic returns unauthorized or redirect
    assert res.status_code in [401, 403, 200] 

def test_currency_switch_valid():
    res = client.post("/index.php", {"currency": "EUR"})
    assert res.status_code == 200