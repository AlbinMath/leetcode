# LeetCode 3356: Zero Array Transformation II

**LeetCode Problem #3356 — Zero Array Transformation II**
Solve LeetCode Zero Array Transformation II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Zero Array Transformation II |
| LeetCode | #3356 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [l_i, r_i, val_i]`.

Each `queries[i]` represents the following action on `nums`:

Decrement the value at each index in the range `[l_i, r_i]` in `nums` by **at most** `val_i`. 
 The amount by which each value is decremented can be chosen **independently** for each index.

A **Zero Array** is an array with all its elements equal to 0.

Return the **minimum** possible **non-negative** value of `k`, such that after processing the first `k` queries in **sequence**, `nums` becomes a **Zero Array**. If no such `k` exists, return -1.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 5 * 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 3`
- `0 <= l_i <= r_i < nums.length`
- `1 <= val_i <= 5`

## Examples
### Example 1
- **Input:** `nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]`
- **Output:** `2`

### Example 2
- **Input:** `nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]`
- **Output:** `-1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Zero Array Transformation II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

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
from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)

        def can(k: int) -> bool:
            diff = [0] * (n + 1)
            for l, r, v in queries[:k]:
                diff[l] += v
                diff[r + 1] -= v
            cur = 0
            for i in range(n):
                cur += diff[i]
                if cur < nums[i]:
                    return False
            return True

        if not can(q):
            return -1

        lo, hi = 0, q
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
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
- [1969. Minimum Non-Zero Product of the Array Elements](../../1501-2000/1969-minimum-non-zero-product-of-the-array-elements/)
- [2357. Make Array Zero by Subtracting Equal Amounts](../../2001-2500/2357-make-array-zero-by-subtracting-equal-amounts/)
- [3354. Make Array Elements Equal to Zero](../../3001-3500/3354-make-array-elements-equal-to-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/zero-array-transformation-ii/)
