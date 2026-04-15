# Cross-Language Specification - Log Analyzer

## Algorithm
Parses server log entries to calculate four primary metrics:
- Total number of requests.
- Count of unique IP addresses.
- Error rate percentage (HTTP status 400-599).
- The most frequently requested URL path.

## Inputs
- List of strings following Common Log Format: `[IP] - - [[Date]] "[Method] [Path] [Proto]" [Status] [Size]`

## Outputs
- JSON object with the following schema:
  - `total_requests`: Integer
  - `unique_ips`: Integer
  - `error_rate`: Float (0.0 to 100.0)
  - `top_path`: String or Null

## Edge Cases
- Input is an empty list or file.
- Log entries with malformed syntax or missing status codes.
- Logs containing only 2xx successful responses.
- Logs containing only 5xx server error responses.
- A tie in frequency between two or more URL paths.

## Test Cases
- `log_standard.txt` → 500 requests, 42 unique IPs, 2.5% error rate, top_path: "/home"
- `log_empty.txt` → 0 requests, 0 unique IPs, 0.0% error rate, top_path: null
- `log_critical.txt` → 100 requests, 10 unique IPs, 100.0% error rate, top_path: "/api/v1"
- `log_malformed.txt` → 20 valid requests, 5 invalid lines → 20 requests, 0.0% error rate
- `log_single.txt` → 1 request, 1 unique IP, 0.0% error rate, top_path: "/index.html"