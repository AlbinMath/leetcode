# LeetCode 264: Ugly Number II

**LeetCode Problem #264 — Ugly Number II**
Solve LeetCode Ugly Number II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Ugly Number II |
| LeetCode | #264 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

Given an integer `n`, return *the* `n^th` ***ugly number***.

## Constraints
- `1 <= n <= 1690`

## Examples
### Example 1
- **Input:** `n = 10`
- **Output:** `12`
- **Explanation:** [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

### Example 2
- **Input:** `n = 1`
- **Output:** `1`
- **Explanation:** 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Ugly Number II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2 = i3 = i5 = 0
        for k in range(1, n):
            a, b, c = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            nxt = min(a, b, c)
            ugly[k] = nxt
            if nxt == a:
                i2 += 1
            if nxt == b:
                i3 += 1
            if nxt == c:
                i5 += 1
        return ugly[-1]
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
- [263. Ugly Number](../../0001-0500/0263-ugly-number/)
- [313. Super Ugly Number](../../0001-0500/0313-super-ugly-number/)
- [1201. Ugly Number III](../../1001-1500/1201-ugly-number-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/ugly-number-ii/)
