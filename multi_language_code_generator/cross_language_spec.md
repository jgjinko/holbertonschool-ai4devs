# Cross-Language Specification - Weighted Inventory Sales Forecaster

## Algorithm Description
This algorithm calculates the **Estimated Days of Stock (EDS)** for a given product. It uses a weighted moving average of sales over the last 30 days to determine daily velocity, then divides current inventory by that velocity to predict when a restock is required.

### Logic
1.  **Velocity_Recent**: Calculate average units sold per day over the last 7 days.
2.  **Velocity_Monthly**: Calculate average units sold per day over the last 30 days.
3.  **Weighted_Velocity**: Compute $(0.7 \times Velocity\_Recent) + (0.3 \times Velocity\_Monthly)$.
4.  **EDS Calculation**: $Current\_Stock / Weighted\_Velocity$.

---

## Input Format (JSON)
{
  "product_id": "SKU-99887",
  "daily_velocity": 10.5,
  "estimated_days_remaining": 14,
  "out_of_stock_date": "2026-04-29",
  "status": "OK"
}
{
  "product_id": "SKU-99887",
  "current_stock": 150,
  "sales_history": [
    {"date": "2026-04-01", "units_sold": 12},
    {"date": "2026-04-02", "units_sold": 8},
    {"date": "2026-04-03", "units_sold": 10}
  ]
}