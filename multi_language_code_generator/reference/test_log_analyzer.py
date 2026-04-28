import unittest
from reference.log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_standard_logs(self):
        logs = [
            '127.0.0.1 - - [15/Apr/2026:12:00:01 +0000] "GET /home HTTP/1.1" 200 512',
            '192.168.1.1 - - [15/Apr/2026:12:00:02 +0000] "GET /home HTTP/1.1" 200 512',
            '127.0.0.1 - - [15/Apr/2026:12:00:03 +0000] "GET /api HTTP/1.1" 404 128'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 3)
        self.assertEqual(result["unique_ips"], 2)
        self.assertEqual(result["top_path"], "/home")
        self.assertAlmostEqual(result["error_rate"], 33.33, places=2)

    def test_empty_input(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertIsNone(result["top_path"])

    def test_all_errors(self):
        logs = ['1.1.1.1 - - [date] "GET /test" 500 0'] * 5
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["error_rate"], 100.0)

    def test_all_success(self):
        logs = ['1.1.1.1 - - [date] "GET /test" 200 0'] * 5
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["error_rate"], 0.0)

    def test_malformed_lines(self):
        logs = [
            'invalid line',
            '1.1.1.1 - - [date] "GET /valid" 200 0'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 1)

    def test_ipv6_addresses(self):
        logs = ['2001:db8::1 - - [date] "GET /" 200 0']
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["unique_ips"], 1)

    def test_multiple_paths_tie(self):
        logs = [
            '1.1.1.1 - - [date] "GET /a" 200 0',
            '1.1.1.1 - - [date] "GET /b" 200 0'
        ]
        result = self.analyzer.analyze(logs)
        self.assertIn(result["top_path"], ["/a", "/b"])

    def test_various_status_codes(self):
        logs = [
            '1.1.1.1 - - [date] "GET /" 301 0', # Success-ish (Redirect)
            '1.1.1.1 - - [date] "GET /" 403 0', # Error
            '1.1.1.1 - - [date] "GET /" 204 0'  # Success
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 3)
        self.assertAlmostEqual(result["error_rate"], 33.33, places=2)

    def test_no_path_in_request(self):
        # Malformed but matching enough of the pattern to try parsing
        logs = ['1.1.1.1 - - [date] "-" 400 0']
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 1)
        self.assertIsNone(result["top_path"])

    def test_large_size_and_complex_date(self):
        logs = ['10.0.0.1 - - [15/Apr/2026:17:30:00 +0200] "POST /upload HTTP/2" 201 1048576']
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["top_path"], "/upload")

if __name__ == "__main__":
    unittest.main()