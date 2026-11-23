# LeetCode 1362: Closest Divisors

**LeetCode Problem #1362 — Closest Divisors**
Solve LeetCode Closest Divisors using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Closest Divisors |
| LeetCode | #1362 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `num`, find the closest two integers in absolute difference whose product equals `num + 1` or `num + 2`.

Return the two integers in any order.

## Constraints
- `1 <= num <= 10^9`

## Examples
### Example 1
- **Input:** `num = 8`
- **Output:** `[3,3]`
- **Explanation:** For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

### Example 2
- **Input:** `num = 123`
- **Output:** `[5,25]`

### Example 3
- **Input:** `num = 999`
- **Output:** `[40,25]`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Closest Divisors**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 8`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,3]`.
4. **Verification:** For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from math import isqrt
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def closest(t: int) -> List[int]:
            for d in range(isqrt(t), 0, -1):
                if t % d == 0:
                    return [d, t // d]

        a = closest(num + 1)
        b = closest(num + 2)
        return a if abs(a[0] - a[1]) <= abs(b[0] - b[1]) else b
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1390. Four Divisors](../../1001-1500/1284-four-divisors/)
- [1808. Maximize Number of Nice Divisors](../../1501-2000/1936-maximize-number-of-nice-divisors/)
- [1952. Three Divisors](../../2001-2500/2083-three-divisors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/closest-divisors/)
