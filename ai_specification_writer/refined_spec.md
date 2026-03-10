## Product Vision
- **Original**: To transform the daily corporate commute into a sustainable, cost-effective, and community-building experience by leveraging intelligent matching and deep enterprise integration.
- **Refined**: Empower corporate organizations to achieve ESG targets and optimize facility overhead by providing employees with a secure, SSO-integrated carpooling ecosystem that automates $CO_2$ reporting and route matching.

## User Stories
- **Original**: As a passenger, I want to browse a list of matched drivers on my route so that I can choose the most convenient ride option.
- **Refined**: As a passenger, I want to view a ranked list of drivers whose routes intersect with mine within a 2-mile buffer, so I can select a ride that minimizes my total commute time.
- **Original**: As a sustainability officer, I want to access a real-time dashboard of $CO_2$ savings so that I can measure and report on the company’s environmental impact.
- **Refined**: As a sustainability officer, I want to generate verifiable carbon offset reports, calculated using standardized per-mile emission factors, to meet internal and regulatory ESG disclosure requirements.
- **Original**: As a driver, I want to access a digital QR code in the app so that I can unlock reserved carpool parking spaces at the office.
- **Refined**: As a driver, I want to receive a time-bound digital parking pass upon trip confirmation to ensure seamless entry into designated high-occupancy vehicle (HOV) parking zones.

## Data Models
- **Original**: User: id, employee_id, home_location, office_id, role, preferences.
- **Refined**: **User Profile**: { `user_id`: UUID, `hr_system_ref`: String, `home_point`: GeoJSON, `assigned_office`: UUID, `user_type`: Enum(Driver, Rider, Hybrid), `commute_window`: Interval }.
- **Original**: Ride: id, driver_id, route_polyline, available_seats, departure_time, status, passenger_ids.
- **Refined**: **Carpool Trip**: { `trip_id`: UUID, `host_id`: UUID, `encoded_path`: Polyline, `seat_inventory`: Integer, `scheduled_departure`: Timestamp, `lifecycle_state`: Enum(Pending, Active, Completed), `roster`: List[UUID] }.

## APIs
- **Original**: POST /api/v1/rides/offer
- **Refined**: `POST /v1/rides/offers` { `driver_id`: UUID, `start_time`: ISO8601, `capacity`: Int, `is_recurring`: Boolean }
- **Original**: GET /api/v1/matches
- **Refined**: `GET /v1/matches` { `passenger_id`: UUID, `search_radius_miles`: Float, `time_flexibility_mins`: Int }
- **Original**: POST /api/v1/rides/{id}/request
- **Refined**: `POST /v1/rides/{trip_id}/requests` { `requester_id`: UUID, `pickup_coords`: Point, `notes`: String }
- **Original**: GET /api/v1/analytics/impact
- **Refined**: `GET /v1/reports/sustainability` { `org_unit`: UUID, `period_start`: Date, `period_end`: Date, `format`: Enum(JSON, PDF) }