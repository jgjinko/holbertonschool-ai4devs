import re
from collections import Counter

class LogAnalyzer:
    # Common Log Format Regex: IP - - [Date] "Method Path Protocol" Status Size
    LOG_PATTERN = r'^(\S+) - - \[(.*?)\] "(?:[A-Z]+ )?(/\S*)?.*?" (\d{3}) (\d+|-)'

    def analyze(self, lines: list) -> dict:
        if not lines:
            return {
                "total_requests": 0,
                "unique_ips": 0,
                "error_rate": 0.0,
                "top_path": None
            }

        total_requests = 0
        unique_ips = set()
        error_count = 0
        paths = []

        for line in lines:
            match = re.search(self.LOG_PATTERN, line)
            if not match:
                continue
            
            total_requests += 1
            ip, date, path, status, size = match.groups()
            
            unique_ips.add(ip)
            
            if int(status) >= 400:
                error_count += 1
            
            if path:
                paths.append(path)

        top_path = Counter(paths).most_common(1)[0][0] if paths else None
        error_rate = (error_count / total_requests * 100) if total_requests > 0 else 0.0

        return {
            "total_requests": total_requests,
            "unique_ips": len(unique_ips),
            "error_rate": round(error_rate, 2),
            "top_path": top_path
        }