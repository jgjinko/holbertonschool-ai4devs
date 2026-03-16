# Monolithic Architecture - StockSync

- **Client Dashboard**: Centralized web interface for interacting with real-time inventory, heatmaps, and KPI widgets.
- **Auth & Identity Manager**: Manages multi-factor authentication (MFA) and secures sensitive third-party API credentials.
- **Multi-Channel Sync Engine**: Core logic facilitating sub-15-second inventory updates across Shopify, Amazon, and TikTok Shop.
- **Geographic Intelligence Module**: Processes customer shipping data for spatial visualization and Mapbox heatmap rendering.
- **Predictive Analytics Engine**: Interfaces with AI models to calculate sales velocity and generate restocking forecasts.
- **Order & Returns Reconciler**: Aggregates sales data against platform fees and COGS to determine net profitability.
- **Notification & Alert Service**: Dispatches automated purchase order drafts and low-stock triggers via SendGrid or Twilio.
- **PostgreSQL Database**: Centralized relational data store acting as the "Source of Truth" for SKU and transaction history.