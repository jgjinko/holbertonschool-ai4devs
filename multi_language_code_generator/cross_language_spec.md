# Cross-Language Specification - Weighted Inventory Sales Forecaster

## Algorithm Description
This algorithm calculates the **Estimated Days of Stock (EDS)** for a given product. It uses a weighted moving average of sales over the last 30 days to determine daily velocity, then divides current inventory by that velocity to predict when a restock is required.

### Logic
1.  **Velocity_Recent**: Calculate average sales per day over the last 7 days.
2.  **Velocity_Monthly**: Calculate average sales per day over the last 30 days.
3.  **Weighted_Velocity**: Compute $(0.7 \times Velocity\_Recent) + (0.3 \times Velocity\_Monthly)$.
4.  **EDS**: $Current\_Stock / Weighted\_Velocity$.

---

## Input Format (JSON)
The algorithm expects a standardized object containing sales history and current stock:
```json
{
  "product_id": "SKU-12345",
  "current_stock": 150,
  "sales_history": [
    {"date": "2026-04-01", "units_sold": 12},
    {"date": "2026-04-02", "units_sold": 8}
  ]
}