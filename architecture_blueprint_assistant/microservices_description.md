# Microservices Architecture - StockSync

- **API Gateway**: Acts as the single entry point for all client requests, handling routing, rate limiting, and security for downstream services.
- **Auth Service**: Manages user identity, Multi-Factor Authentication (MFA), and secures sensitive third-party API credentials.
- **Inventory Sync Service**: Facilitates sub-15-second synchronization between Shopify, Amazon, and TikTok Shop while maintaining a centralized "Source of Truth" for stock.
- **Geographic Intelligence Service**: Processes shipping data into spatial coordinates and interfaces with Mapbox to generate heatmaps and identify "Hot Zones."
- **Predictive Analytics Service**: Analyzes sales velocity and integrates with LLMs (OpenAI/Anthropic) to generate automated restocking forecasts and "Days of Cover" alerts.
- **Order Reconciler Service**: Aggregates multi-channel order data with COGS and platform fees to provide precise profitability and ROI analytics.
- **Notification Service**: Orchestrates the delivery of low-stock triggers and automated purchase order drafts via SendGrid and Twilio.
- **Database-per-Service**: Ensures data isolation and independent scalability by providing each microservice with its own dedicated, private data store.