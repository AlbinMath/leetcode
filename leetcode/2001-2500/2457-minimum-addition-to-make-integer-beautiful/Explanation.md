# LeetCode 2457: Minimum Addition to Make Integer Beautiful

**LeetCode Problem #2457 — Minimum Addition to Make Integer Beautiful**
Solve LeetCode Minimum Addition to Make Integer Beautiful using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Addition to Make Integer Beautiful |
| LeetCode | #2457 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive integers `n` and `target`.

An integer is considered **beautiful** if the sum of its digits is less than or equal to `target`.

Return the *minimum **non-negative** integer *`x`* such that *`n + x`* is beautiful*. The input will be generated such that it is always possible to make `n` beautiful.

## Constraints
- `1 <= n <= 10^12`
- `1 <= target <= 150`
- The input will be generated such that it is always possible to make `n` beautiful.

## Examples
### Example 1
- **Input:** `n = 16, target = 6`
- **Output:** `4`
- **Explanation:** Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and digit sum becomes 2 + 0 = 2. It can be shown that we can not make n beautiful with adding non-negative integer less than 4.

### Example 2
- **Input:** `n = 467, target = 6`
- **Output:** `33`
- **Explanation:** Initially n is 467 and its digit sum is 4 + 6 + 7 = 17. After adding 33, n becomes 500 and digit sum becomes 5 + 0 + 0 = 5. It can be shown that we can not make n beautiful with adding non-negative integer less than 33.

### Example 3
- **Input:** `n = 1, target = 1`
- **Output:** `0`
- **Explanation:** Initially n is 1 and its digit sum is 1, which is already smaller than or equal to target.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Addition to Make Integer Beautiful**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 16, target = 6`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and digit sum becomes 2 + 0 = 2. It can be shown that we can not make n beautiful with adding non-negative integer less than 4.

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
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        orig = n
        p = 10
        while digit_sum(n) > target:
            n = (n // p + 1) * p
            p *= 10
        return n - orig
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
- [2216. Minimum Deletions to Make Array Beautiful](../../2001-2500/2216-minimum-deletions-to-make-array-beautiful/)
- [2914. Minimum Number of Changes to Make Binary String Beautiful](../../2501-3000/2914-minimum-number-of-changes-to-make-binary-string-beautiful/)
- [2749. Minimum Operations to Make the Integer Zero](../../2501-3000/2749-minimum-operations-to-make-the-integer-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/)
