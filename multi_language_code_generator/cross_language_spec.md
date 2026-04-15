# Cross-Language Specification - Weighted Inventory Sales Forecaster

## Algorithm
Predicts **Estimated Days of Stock (EDS)** using a weighted velocity:
1. **V_recent**: Avg sales/day (last 7 days).
2. **V_monthly**: Avg sales/day (last 30 days).
3. **V_weighted**: $(0.7 * V\_recent) + (0.3 * V\_monthly)$.
4. **EDS**: $Current\_Stock / V\_weighted$.

## Inputs
```json
{
  "product_id": "SKU-99",
  "current_stock": 100,
  "sales_history": [{"date": "2026-04-01", "units_sold": 10}]
}