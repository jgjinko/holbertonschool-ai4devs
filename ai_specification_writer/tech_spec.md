# Technical Specification

## System Components
- **Authentication Service**: Manages secure identity verification by integrating with corporate SSO (Okta/Azure AD) and maintaining the employee-only "walled garden."
- **Matching Engine**: A geo-spatial microservice that processes route polylines and schedule windows to calculate compatibility scores between users.
- **Sustainability Analytics Service**: Aggregates completed trip data to calculate $CO_2$ offsets and generates reporting for corporate ESG dashboards.
- **Notification Service**: Handles real-time push and in-app alerts for trip requests, status updates, and proximity reminders.

## Data Models
- **User**: `id` (UUID), `employee_id` (String), `home_location` (GeoJSON), `office_id` (UUID), `role` (Enum: Driver/Passenger), `preferences` (JSON).
- **Ride**: `id` (UUID), `driver_id` (UUID), `route_polyline` (String), `available_seats` (Int), `departure_time` (DateTime), `status` (Enum), `passenger_ids` (Array).

## API Endpoints
- **POST /api/v1/rides/offer**: Creates a new driver trip. (Params: `start_time`, `available_seats`, `recurring_days`).
- **GET /api/v1/matches**: Returns compatible rides for a passenger. (Params: `user_id`, `radius_miles`, `flex_window_mins`).
- **POST /api/v1/rides/{id}/request**: Sends a seat request to a driver. (Params: `user_id`, `pickup_point`, `message`).
- **GET /api/v1/analytics/impact**: Retrieves CO2 and mileage data. (Params: `org_id`, `timeframe`, `metric_type`).

## System Architecture
```mermaid
graph TD
  A[Mobile App] --> B[API Gateway]
  B --> C[Auth Service - SSO]
  B --> D[Matching Engine - Geo]
  B --> E[Sustainability Service]
  C --> F[Corporate Azure AD/Okta]
  D --> G[(Geo-Spatial DB)]
  E --> H[(Metrics DB)]