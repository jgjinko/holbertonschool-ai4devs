# Cross-Language Specification - Weighted Inventory Sales Forecaster

## 1. Algorithm Description
This algorithm calculates the **Estimated Days of Stock (EDS)** for a specific product. It uses a weighted moving average of sales data from the last 30 days to determine current sales velocity, then divides the current inventory by that velocity to predict the stock exhaustion date.

### Calculation Logic
1.  **Recent Velocity** ($V_{recent}$): The average units sold per day over the last **7 days**.
2.  **Monthly Velocity** ($V_{monthly}$): The average units sold per day over the last **30 days**.
3.  **Weighted Velocity** ($V_{weighted}$): A blend of both averages to account for recent trends: 
    $$V_{weighted} = (0.7 \times V_{recent}) + (0.3 \times V_{monthly})$$
4.  **Estimated Days of Stock (EDS)**: 
    $$EDS = \frac{Current\_Stock}{V_{weighted}}$$

---

## 2. Input Format (JSON)
The algorithm expects a JSON object containing the product identifier, current physical stock, and a chronological list of sales entries.

```json
{
  "product_id": "SKU-99887",
  "current_stock": 150,
  "sales_history": [
    {"date": "2026-04-01", "units_sold": 12},
    {"date": "2026-04-02", "units_sold": 8},
    {"date": "2026-04-03", "units_sold": 10}
  ]
}