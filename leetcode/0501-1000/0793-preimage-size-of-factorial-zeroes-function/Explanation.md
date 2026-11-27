# LeetCode 793: Preimage Size of Factorial Zeroes Function

**LeetCode Problem #793 — Preimage Size of Factorial Zeroes Function**
Solve LeetCode Preimage Size of Factorial Zeroes Function using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Preimage Size of Factorial Zeroes Function |
| LeetCode | #793 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Let `f(x)` be the number of zeroes at the end of `x!`. Recall that `x! = 1 * 2 * 3 * ... * x` and by convention, `0! = 1`.

For example, `f(3) = 0` because `3! = 6` has no zeroes at the end, while `f(11) = 2` because `11! = 39916800` has two zeroes at the end.

Given an integer `k`, return the number of non-negative integers `x` have the property that `f(x) = k`.

## Constraints
- `0 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `k = 0`
- **Output:** `5`
- **Explanation:** 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.

### Example 2
- **Input:** `k = 5`
- **Output:** `0`
- **Explanation:** There is no x such that x! ends in k = 5 zeroes.

### Example 3
- **Input:** `k = 3`
- **Output:** `5`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Preimage Size of Factorial Zeroes Function**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 0`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.

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
    def preimageSizeFZF(self, k: int) -> int:
        def f(x: int) -> int:
            zeros = 0
            while x:
                x //= 5
                zeros += x
            return zeros

        lo, hi = 0, 5 * (k + 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if f(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return 5 if f(lo) == k else 0
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
- [172. Factorial Trailing Zeroes](../../0001-0500/0172-factorial-trailing-zeroes/)
- [209. Minimum Size Subarray Sum](../../0001-0500/0209-minimum-size-subarray-sum/)
- [952. Largest Component Size by Common Factor](../../0501-1000/0952-largest-component-size-by-common-factor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/)
