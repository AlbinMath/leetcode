# LeetCode 1802: Maximum Value at a Given Index in a Bounded Array

**LeetCode Problem #1802 — Maximum Value at a Given Index in a Bounded Array**
Solve LeetCode Maximum Value at a Given Index in a Bounded Array using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Value at a Given Index in a Bounded Array |
| LeetCode | #1802 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three positive integers: `n`, `index`, and `maxSum`. You want to construct an array `nums` (**0-indexed**)** **that satisfies the following conditions:

`nums.length == n` 
 `nums[i]` is a **positive** integer where `0 <= i < n`. 
 `abs(nums[i] - nums[i+1]) <= 1` where `0 <= i < n-1`. 
 The sum of all the elements of `nums` does not exceed `maxSum`. 
 `nums[index]` is **maximized**.

Return `nums[index]`* of the constructed array*.

Note that `abs(x)` equals `x` if `x >= 0`, and `-x` otherwise.

## Constraints
- `1 <= n <= maxSum <= 10^9`
- `0 <= index < n`

## Examples
### Example 1
- **Input:** `n = 4, index = 2, maxSum = 6`
- **Output:** `2`
- **Explanation:** nums = [1,2,

### Example 2
- **Input:** `n = 6, index = 1, maxSum = 10`
- **Output:** `3`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Value at a Given Index in a Bounded Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, index = 2, maxSum = 6`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** nums = [1,2,

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side(v: int, length: int) -> int:
            # sum of `length` elements descending from v-1, floored at 1
            if length < v:
                return length * (2 * v - length - 1) // 2
            return v * (v - 1) // 2 + (length - (v - 1))

        def total(v: int) -> int:
            return v + side(v, index) + side(v, n - index - 1)

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if total(mid) <= maxSum:
                lo = mid
            else:
                hi = mid - 1

        return lo
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3287. Find the Maximum Sequence Value of Array](../../3001-3500/3287-find-the-maximum-sequence-value-of-array/)
- [4098. Minimize the Maximum Value of GCD-Connected Array](../../4001-4500/4098-minimize-the-maximum-value-of-gcd-connected-array/)
- [1131. Maximum of Absolute Value Expression](../../1001-1500/1131-maximum-of-absolute-value-expression/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/)
