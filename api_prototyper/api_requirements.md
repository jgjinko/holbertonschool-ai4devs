# API Requirements – StockSync Core API

## Domain
Multi-channel e-commerce inventory management and geographic business intelligence.

## Target Users
- **Inventory Managers:** To maintain stock accuracy and automate reorder logic.
- **Growth Specialists:** To query geographic sales density for marketing optimization.
- **System Developers:** To integrate third-party webhooks (Shopify, Amazon, TikTok Shop).

## Core Operations
1.  **Connect Sales Channel:** Authorize and link a new API (OAuth for Shopify/Amazon SP-API).
2.  **Sync Unified Inventory:** Retrieve a consolidated list of all SKUs and their total stock.
3.  **Get SKU Detail:** Fetch channel-specific stock breakdown and historical velocity for one SKU.
4.  **Manual Stock Adjustment:** Override stock levels for a specific location or channel.
5.  **Fetch Heatmap Data:** Retrieve sales density coordinates (Lat/Long) for Mapbox visualization.
6.  **Get AI Forecasts:** Calculate "Days of Cover" and "Burn Rate" based on historical trends.
7.  **Retrieve Active Alerts:** Get a list of breached "Safety Stock" thresholds or seasonal spikes.
8.  **Generate Draft PO:** Create an automated Purchase Order based on AI restock suggestions.
9.  **Monitor Sync Health:** Check the real-time heartbeat and latency of connected channel APIs.
10. **Ingest Sales Webhook:** Receive and process real-time sale events from external platforms.

## Data Validation Rules
- **SKU Uniqueness:** Every product SKU must be unique within a single user organization.
- **Quantity Constraints:** Inventory levels must be non-negative integers.
- **Coordinate Integrity:** Geographic data must follow valid WGS84 (Latitude/Longitude) formats.
- **Timestamping:** All sales events must include an ISO 8601 UTC timestamp to prevent sync conflicts.
- **Currency:** All financial data must be converted to a designated base currency (e.g., USD) for BI reporting.

## Non-Functional Requirements
- **Sync Latency:** End-to-end data synchronization across all channels must occur in < 15 seconds.
- **API Performance:** Internal API endpoints must return data in < 200ms for dashboard responsiveness.
- **Authentication:** Strict JWT-based authentication required for all requests; MFA required for credential management.
- **Rate Limiting:** Internal throttling at 5,000 requests/minute per client; must strictly respect third-party API limits (e.g., Amazon’s "leaky bucket" algorithm).
- **Scalability:** Must support high-concurrency event processing (up to 100,000 monthly orders per client).