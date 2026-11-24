# LeetCode 263: Ugly Number

**LeetCode Problem #263 — Ugly Number**
Solve LeetCode Ugly Number using PHP, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Ugly Number |
| LeetCode | #263 |
| Difficulty | Easy |
| Language | PHP, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An **ugly number** is a *positive* integer which does not have a prime factor other than 2, 3, and 5.

Given an integer `n`, return `true` *if* `n` *is an **ugly number***.

## Constraints
- `-2^31 <= n <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `n = 6`
- **Output:** `true`
- **Explanation:** 6 = 2 &times; 3

### Example 2
- **Input:** `n = 1`
- **Output:** `true`
- **Explanation:** 1 has no prime factors.

### Example 3
- **Input:** `n = 14`
- **Output:** `false`
- **Explanation:** 14 is not ugly since it includes the prime factor 7.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Ugly Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** 6 = 2 &times; 3

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
PHP, Python

## Source Code
- [solution.php](./solution.php)
- [solution.py](./solution.py)


### PHP
```php
class Solution {
    function isUgly($n) {
        // Ugly numbers must be positive
        if ($n <= 0) {
            return false;
        }

        // Remove all factors of 2, 3, and 5
        while ($n % 2 == 0) {
            $n = intdiv($n, 2);
        }

        while ($n % 3 == 0) {
            $n = intdiv($n, 3);
        }

        while ($n % 5 == 0) {
            $n = intdiv($n, 5);
        }

        // No other prime factors should remain
        return $n == 1;
    }
}
```

### Python
```python
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in (2, 3, 5):
            while n % p == 0:
                n //= p
        return n == 1
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1201. Ugly Number III](../../1001-1500/1201-ugly-number-iii/)
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/ugly-number/)
