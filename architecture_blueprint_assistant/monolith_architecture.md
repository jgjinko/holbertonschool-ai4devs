graph TD
    A[Client Dashboard / React Frontend] --> B[StockSync Monolith Core]
    
    subgraph "Monolith Internal Modules"
    B --> C[Auth & Identity Manager]
    B --> D[Multi-Channel Sync Engine]
    B --> E[Geographic Intelligence Module]
    B --> F[Predictive Analytics Engine]
    B --> G[Order & Returns Reconciler]
    B --> H[Notification & Alert Service]
    end

    C --> I[(PostgreSQL Database)]
    D --> J[External APIs: Shopify/Amazon/TikTok]
    E --> K[Mapbox / Google Maps API]
    F --> L[AI Integration: OpenAI/Anthropic]