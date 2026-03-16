# Data Model
- **User**: id, email, password_hash, mfa_enabled, role, created_at
- **Sales Channel**: id, user_id, platform_name (Shopify/Amazon/TikTok), api_credentials_encrypted, webhook_url, sync_latency_status
- **Product**: id, user_id, base_sku, name, description, category, cogs (Cost of Goods Sold), unit_price
- **Order**: id, channel_id, external_order_id, total_amount, platform_fees, shipping_cost, customer_lat_long, order_timestamp, status
- **Inventory Level**: id, product_id, warehouse_id, quantity_on_hand, safety_stock_threshold, last_sync_time
- **Analytics Snapshot**: id, product_id, sales_velocity_7d, sales_velocity_30d, predicted_stockout_date, days_of_cover