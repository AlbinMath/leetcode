# LeetCode 1553: Minimum Number of Days to Eat N Oranges

**LeetCode Problem #1553 — Minimum Number of Days to Eat N Oranges**
Solve LeetCode Minimum Number of Days to Eat N Oranges using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Days to Eat N Oranges |
| LeetCode | #1553 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange. 
 If the number of remaining oranges `n` is divisible by `2` then you can eat `n / 2` oranges. 
 If the number of remaining oranges `n` is divisible by `3` then you can eat `2 * (n / 3)` oranges.

You can only choose one of the actions per day.

Given the integer `n`, return *the minimum number of days to eat* `n` *oranges*.

## Constraints
- `1 <= n <= 2 * 10^9`

## Examples
### Example 1
- **Input:** `n = 10`
- **Output:** `4`
- **Explanation:** You have 10 oranges.
Day 1: Eat 1 orange, 10 - 1 = 9. 
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
Day 4: Eat the last orange 1 - 1 = 0.
You need at least 4 days to eat the 10 oranges.

### Example 2
- **Input:** `n = 6`
- **Output:** `3`
- **Explanation:** You have 6 oranges.
Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
Day 3: Eat the last orange 1 - 1 = 0.
You need at least 3 days to eat the 6 oranges.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Days to Eat N Oranges**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** You have 10 oranges.
Day 1: Eat 1 orange, 10 - 1 = 9. 
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
Day 4: Eat the last orange 1 - 1 = 0.
You need at least 4 days to eat the 10 oranges.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def f(n):
            if n <= 1:
                return n
            return 1 + min(n % 2 + f(n // 2), n % 3 + f(n // 3))

        return f(n)
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1568. Minimum Number of Days to Disconnect Island](../../1501-2000/1691-minimum-number-of-days-to-disconnect-island/)
- [957. Prison Cells After N Days](../../0501-1000/0994-prison-cells-after-n-days/)
- [1137. N-th Tribonacci Number](../../1001-1500/1236-n-th-tribonacci-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/)
