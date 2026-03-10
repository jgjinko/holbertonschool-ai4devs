### User Story 1

As a corporate employee, I want to sign in using my company SSO so that I can access the platform securely without managing a new set of credentials.
**Acceptance Criteria**:
- System integrates with corporate identity providers (Okta/Azure AD).
- New user profiles are automatically populated with corporate directory data.
- Access is restricted to active employee email domains.
**Priority**: MVP



### User Story 2

As a corporate employee, I want to set my home location and shift schedule so that the system can accurately match me with colleagues on my route.
**Acceptance Criteria**:
- User can input a precise home address using a map interface.
- User can define recurring weekly "Start" and "End" work times.
- System validates that the location is within a supported geographic region.
**Priority**: MVP


### User Story 3

As a passenger, I want to browse a list of matched drivers on my route so that I can choose the most convenient ride option.
**Acceptance Criteria**:
- System displays drivers within a 2-mile radius of the commute path.
- Matches are ranked by a compatibility score (schedule and proximity).
- Users can view driver vehicle capacity and preference details.
**Priority**: MVP


### User Story 4

As a driver, I want to offer my upcoming commute schedule so that colleagues can request seats in my vehicle.
**Acceptance Criteria**:
- Driver can specify the number of available seats (1–4).
- System allows for one-off or recurring schedule posts.
- Rides are instantly visible to matching passengers in the search results.
**Priority**: MVP


### User Story 5

As a corporate employee, I want to receive push notifications for ride requests and status changes so that I can coordinate my commute in real-time.
**Acceptance Criteria**:
- Drivers get instant alerts for new seat requests.
- Passengers are notified immediately when a request is accepted or declined.
- Reminders are sent 15 minutes prior to the scheduled pickup time.
**Priority**: High


### User Story 6

As a sustainability officer, I want to access a real-time dashboard of $CO_2$ savings so that I can measure and report on the company’s environmental impact.
**Acceptance Criteria**:
- Dashboard displays aggregate metric tons of $CO_2$ saved based on miles shared.
- Data is filterable by month, quarter, and specific office location.
- Metrics are exportable for integration into corporate ESG reports.
**Priority**: High


### User Story 7

As a carpool participant, I want to use in-app messaging to communicate with my group so that we can coordinate pickup logistics without sharing personal phone numbers.
**Acceptance Criteria**:
- Chat channels are created automatically once a ride is confirmed.
- Messaging is restricted to the specific driver and passengers in that carpool.
- Chat history is deleted 24 hours after trip completion for privacy.
**Priority**: High


### User Story 8

As a facility manager, I want to provide reserved parking access via the app so that I can incentivize carpooling and reduce parking infrastructure pressure.
**Acceptance Criteria**:
- System generates a dynamic QR code for confirmed carpoolers for the day.
- QR code integrates with facility gate readers for "Preferred Parking" access.
- Access is automatically revoked if the carpool trip is cancelled.
**Priority**: Medium