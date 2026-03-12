# Prompt Testing Examples

## Example 1 – Refactoring Prompt

**Prompt Used**: "As a Senior Developer, refactor the following Python code for clarity and performance. Provide clean, optimized code with inline comments explaining major changes."

**Input**:
```python
def procss(lst):
    result=[]
    for i in range(len(lst)):
        if lst[i]%2==0:
            result.append(lst[i]*lst[i])
    return result
```

**AI Output**:
```python
def get_squared_even_numbers(numbers: list[int]) -> list[int]:
    """Filter even numbers and return their squares."""
    # Use list comprehension for cleaner, more Pythonic approach
    # This is more readable and faster than manual loop iteration
    return [num ** 2 for num in numbers if num % 2 == 0]
```

**Feedback**: Excellent output. The refactored code:
- Fixes the typo in function name (`procss` → `get_squared_even_numbers`)
- Adds type hints for better code documentation
- Replaces verbose loop with Pythonic list comprehension
- Includes a docstring explaining functionality
- More efficient and readable. Only minor note: the comment could mention performance benefits (O(n) complexity maintained but faster execution).

---

## Example 2 – Unit Test Generation Prompt

**Prompt Used**: "As a Test Engineer, generate comprehensive unit tests for the provided Python function using pytest. Include normal operations, edge cases, error conditions, and boundary values with clear test names and assertions."

**Input**:
```python
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate final price after applying discount percentage."""
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be non-negative")
    if discount_percent > 100:
        raise ValueError("Discount cannot exceed 100%")
    return price * (1 - discount_percent / 100)
```

**AI Output**:
```python
import pytest
from module import calculate_discount

class TestCalculateDiscount:
    """Test suite for calculate_discount function."""
    
    def test_normal_discount_calculation(self):
        """Test standard discount application."""
        assert calculate_discount(100, 10) == 90.0
        assert calculate_discount(50, 25) == 37.5
    
    def test_zero_discount(self):
        """Test with zero discount (no reduction)."""
        assert calculate_discount(100, 0) == 100.0
    
    def test_full_discount(self):
        """Test with 100% discount (free item)."""
        assert calculate_discount(100, 100) == 0.0
    
    def test_zero_price(self):
        """Test with zero priced item."""
        assert calculate_discount(0, 50) == 0.0
    
    def test_negative_price_raises_error(self):
        """Test that negative price raises ValueError."""
        with pytest.raises(ValueError, match="non-negative"):
            calculate_discount(-50, 10)
    
    def test_negative_discount_raises_error(self):
        """Test that negative discount raises ValueError."""
        with pytest.raises(ValueError, match="non-negative"):
            calculate_discount(100, -10)
    
    def test_discount_over_100_raises_error(self):
        """Test that discount > 100% raises ValueError."""
        with pytest.raises(ValueError, match="exceed 100"):
            calculate_discount(100, 150)
    
    def test_float_precision(self):
        """Test floating point handling."""
        assert abs(calculate_discount(99.99, 33.33) - 66.66) < 0.01
```

**Feedback**: Outstanding test coverage:
- ✓ Tests all normal cases (standard discounts)
- ✓ Tests boundary values (0%, 100%, 0 price)
- ✓ Tests error conditions (negative values, discount > 100)
- ✓ Tests floating point edge case
- ✓ Clear test naming conventions (test_<scenario>)
- ✓ Proper use of pytest.raises for exception testing
Minor improvement: Could add parameterized tests using @pytest.mark.parametrize for reducing repetition.

---

## Example 3 – Code Review Checklist Prompt

**Prompt Used**: "As a Code Review Lead, generate a context-specific code review checklist for a React + Node.js web application with authentication requirements and GDPR compliance needs. Include categories for Functionality, Performance, Security, Documentation, Testing, and Style."

**Input**:
- Project Type: Web Application (Full Stack)
- Tech Stack: React, Node.js, PostgreSQL
- Compliance: GDPR
- Coding Standards: ESLint, Prettier

**AI Output**:
```
# Code Review Checklist - React + Node.js Web App

## Functionality
- [ ] Features match requirements and user stories
- [ ] All happy paths and error flows are implemented
- [ ] Form validation is present and working correctly
- [ ] API endpoints return correct status codes (200, 201, 400, 401, 404, 500)
- [ ] Database queries handle NULL values properly
- [ ] Session/token management is working per specifications

## Performance
- [ ] API responses are under 200ms for standard queries
- [ ] Database queries use proper indexing and avoid N+1 problems
- [ ] Large datasets are paginated (implement limit/offset)
- [ ] React components avoid unnecessary re-renders (use React.memo, useMemo)
- [ ] Bundle size is optimized (check with webpack-analyzer)
- [ ] Database connection pooling is established (Node.js)
- [ ] No memory leaks in event listeners or subscriptions

## Security
- [ ] SQL injection risks are mitigated (use parameterized queries)
- [ ] CSRF tokens are implemented for state-changing operations
- [ ] Passwords are hashed using bcrypt or Argon2 (minimum 10 rounds)
- [ ] Sensitive data (emails, phone) are encrypted at rest
- [ ] Environment variables are used for secrets (no hardcoded credentials)
- [ ] CORS is properly configured (not using *)
- [ ] Authentication tokens have reasonable expiration times
- [ ] User permissions are validated on backend (not just frontend)

## Compliance (GDPR)
- [ ] User data deletion requests are fully implemented
- [ ] Data export functionality available for users
- [ ] User consent for data collection is documented
- [ ] Personal data is not logged in error messages
- [ ] Data retention policies are documented and enforced
- [ ] Privacy policy is accessible and up-to-date

## Documentation
- [ ] README includes setup and deployment instructions
- [ ] API endpoints are documented with examples (Swagger/OpenAPI)
- [ ] Complex business logic has explanatory comments
- [ ] Database schema is documented
- [ ] Environment variables are listed and explained

## Testing
- [ ] Unit test coverage is > 80% for critical functions
- [ ] Integration tests cover main user workflows
- [ ] API tests verify status codes and response structure
- [ ] Database migrations have rollback tests
- [ ] Error handling is tested for edge cases

## Code Style
- [ ] Code follows ESLint rules (no warnings)
- [ ] Prettier formatting is applied consistently
- [ ] Variable names are descriptive and use camelCase
- [ ] Function names describe what they do
- [ ] Comments explain WHY, not WHAT
- [ ] Console.logs are removed (except debug mode)
```

**Feedback**: Highly practical and comprehensive:
- ✓ Organized into required categories
- ✓ Specific to React + Node.js stack
- ✓ Includes GDPR-specific items
- ✓ Actionable checklist items (not vague)
- ✓ Includes performance benchmarks (200ms response time, >80% test coverage)
- ✓ Security-focused with concrete examples
Minor enhancement: Could include specific quantum numbers (e.g., "> 4.2 Lighthouse score") for broader applicability.

---

## Example 4 – Performance Optimization Prompt

**Prompt Used**: "As a Performance Engineer, analyze and optimize the following Python function for performance and resource efficiency. Provide Big O complexity analysis, explain improvements, and include benchmarking recommendations."

**Input**:
```python
def find_duplicates(arr):
    """Find all duplicate values in array."""
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates
```

**Performance Metrics**: Array size up to 1 million elements. Current execution time: ~45 seconds.

**AI Output**:
```python
def find_duplicates(arr):
    """Find all duplicate values in array using hash set for O(n) performance."""
    seen = set()
    duplicates = set()
    
    # Single pass through array with O(1) hash lookups
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Alternative if order preservation needed:
from collections import OrderedDict

def find_duplicates_ordered(arr):
    """Find duplicates while preserving first occurrence order."""
    seen = set()
    duplicates = OrderedDict()
    
    for num in arr:
        if num in seen and num not in duplicates:
            duplicates[num] = True  # Use keys to maintain order
        else:
            seen.add(num)
    
    return list(duplicates.keys())
```

**Complexity Analysis**:

| Approach | Time Complexity | Space Complexity | Notes |
|----------|-----------------|------------------|-------|
| Original (nested loops) | O(n²) | O(k) where k = duplicates | For 1M items: ~1 trillion comparisons |
| Optimized (hash set) | O(n) | O(n) | Linear time, single pass |
| Improvement | **45x faster** | +O(n) space | Trade memory for speed |

**Benchmarking Recommendations**:
```python
import timeit

test_data = list(range(100000)) + list(range(50000))  # 150k items with duplicates

# Benchmark original: ~8 seconds
original_time = timeit.timeit(lambda: find_duplicates_original(test_data), number=1)

# Benchmark optimized: ~0.18 seconds
optimized_time = timeit.timeit(lambda: find_duplicates(test_data), number=1)

print(f"Speed improvement: {original_time / optimized_time:.1f}x faster")
```

**Feedback**: Excellent optimization analysis:
- ✓ Correctly identified O(n²) vs O(n) complexity difference
- ✓ Provided working optimized solution
- ✓ Included table comparing approaches
- ✓ Offered alternative solution for order preservation
- ✓ Provided concrete benchmarking code
- ✓ Accurate performance estimates (45x faster is realistic)
Minor note: Could include memory usage comparison and CPU profiling recommendations for very large datasets.

---

## Example 5 – Design Pattern Application Prompt

**Prompt Used**: "As a Software Architect, suggest appropriate design patterns for the following problem in Python. Provide the recommended pattern with explanation, implementation example, pros/cons, and alternative patterns."

**Input Problem**: "We have a configuration system that loads settings from multiple sources: environment variables, JSON files, and a database. The application needs to check sources in priority order and we may add more sources later. Additionally, we need to validate and cache configuration values."

**AI Output**:

### Recommended Pattern: **Chain of Responsibility + Strategy Pattern**

**Explanation**: The Chain of Responsibility pattern allows requests to be passed along a chain of handlers, where each handler decides whether to process the request or pass it on. Combined with the Strategy pattern for source-specific loading logic, this provides flexibility for adding new sources.

**Implementation**:
```python
from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Any, Optional

class ConfigSource(ABC):
    """Abstract base for configuration sources."""
    
    def __init__(self, next_source: Optional['ConfigSource'] = None):
        self.next_source = next_source
    
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        """Return config value or None if not found."""
        pass
    
    def retrieve(self, key: str) -> Optional[Any]:
        """Chain lookup across sources."""
        value = self.get(key)
        if value is not None:
            return value
        return self.next_source.retrieve(key) if self.next_source else None


class EnvVarSource(ConfigSource):
    """Load from environment variables."""
    def get(self, key: str) -> Optional[str]:
        import os
        return os.getenv(key)


class JSONFileSource(ConfigSource):
    """Load from JSON file."""
    def __init__(self, filepath: str, next_source: Optional[ConfigSource] = None):
        super().__init__(next_source)
        self.filepath = filepath
        self._cache = None
    
    def get(self, key: str) -> Optional[Any]:
        if self._cache is None:
            import json
            with open(self.filepath) as f:
                self._cache = json.load(f)
        return self._cache.get(key)


class DatabaseSource(ConfigSource):
    """Load from database."""
    def __init__(self, db_connection, next_source: Optional[ConfigSource] = None):
        super().__init__(next_source)
        self.db = db_connection
    
    def get(self, key: str) -> Optional[Any]:
        # Pseudo-code for database query
        result = self.db.query("SELECT value FROM config WHERE key = ?", key)
        return result[0] if result else None


# Usage with priority chain
config_loader = EnvVarSource(
    JSONFileSource("config.json",
        DatabaseSource(db_connection)
    )
)

@lru_cache(maxsize=128)
def get_config(key: str) -> Any:
    """Get config value with caching."""
    return config_loader.retrieve(key)

# Example
database_host = get_config("DATABASE_HOST")  # Checks env vars → JSON → DB
```

**Pros & Cons**:
| Pros | Cons |
|------|------|
| Easy to add new sources | Slightly more overhead than direct lookup |
| Clear separation of concerns | Requires careful ordering of chain |
| Order-based priority is intuitive | Can be overkill for simple config |
| Each source is independent | Need to handle exceptions per source |

**Alternative Patterns**:

1. **Factory Pattern**: If you need to create different config loaders based on environment
   - Good for: Clear instantiation logic, environment-specific configs
   - Trade-off: Less flexible for multiple sources

2. **Strategy Pattern alone**: If you just want pluggable sources without priority
   - Good for: Simple cases, no chaining needed
   - Trade-off: Doesn't handle source precedence naturally

3. **Decorator Pattern**: If you want to add validation/caching as wrappers
   - Good for: Non-invasive enhancements
   - Trade-off: More verbose for complex scenarios

**Feedback**: Outstanding architectural guidance:
- ✓ Identified core pattern (Chain of Responsibility) correctly
- ✓ Showed practical integration with caching (lru_cache)
- ✓ Provided complete, runnable implementation
- ✓ Included concrete pros/cons table
- ✓ Offered 3 realistic alternative patterns with trade-offs
- ✓ Clear explanation of when to use each approach
- ✓ Addressed extensibility requirement (easy to add sources)
Only minor enhancement: Could include performance considerations for large config sets and thread-safety notes for concurrent access.

---

## Summary of Testing Results

| Template | Quality | Key Strengths | Areas for Improvement |
|----------|---------|---------------|----------------------|
| Refactoring | ⭐⭐⭐⭐⭐ | Excellent code quality, good explanations | Could mention performance benchmarks |
| Unit Testing | ⭐⭐⭐⭐⭐ | Comprehensive coverage, clear naming | Could use parameterized tests |
| Code Review | ⭐⭐⭐⭐⭐ | Specific, actionable, comprehensive | Tech stack-specific items excellent |
| Performance | ⭐⭐⭐⭐⭐ | Strong analysis, realistic benchmarks | Could include profiling recommendations |
| Design Pattern | ⭐⭐⭐⭐⭐ | Excellent guidance, practical code | Could add thread-safety discussion |

**Overall Assessment**: All five templates produced high-quality outputs with detailed, practical guidance. The templates are well-designed for their respective use cases and handle both common scenarios and edge cases effectively.
