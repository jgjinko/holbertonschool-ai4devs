# Cross-Language Specification - Weighted Inventory Sales Forecaster

## Algorithm Description
This algorithm calculates the **Estimated Days of Stock (EDS)** for a given product. It uses a weighted moving average of sales over the last 30 days to determine daily velocity, then divides current inventory by that velocity to predict when a restock is required.

**Logic:**
1. Calculate **Velocity_Recent** (Average sales per day over the last 7 days).
2. Calculate **Velocity_Monthly** (Average sales per day over the last 30 days).
3. Compute **Weighted_Velocity = (0.7 * Velocity_Recent) + (0.3 * Velocity_Monthly)**.
4. **EDS = Current_Stock / Weighted_Velocity**.

## Input Format (JSON)
The algorithm expects a standardized object containing sales history and current stock:
```json
{
  "product_id": "string",
  "current_stock": "integer",
  "sales_history": [
    {"date": "YYYY-MM-DD", "units_sold": "integer"}
  ]
}