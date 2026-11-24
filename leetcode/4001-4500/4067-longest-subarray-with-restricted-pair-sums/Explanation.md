# LeetCode 4067: Longest Subarray With Restricted Pair Sums

**LeetCode Problem #4067 — Longest Subarray With Restricted Pair Sums**
Solve LeetCode Longest Subarray With Restricted Pair Sums using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subarray With Restricted Pair Sums |
| LeetCode | #4067 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A ** subarray ** `nums[l..r]` is valid if there are no three **distinct** indices `i`, `j`, and `k` such that `l <= i, j, k <= r` and:

`nums[i] + nums[j] == nums[k]`

Return the **maximum** length of a valid subarray of `nums`.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 500`

## Examples
### Example 1
- **Input:** `nums = [2,3,5,3,2,1]`
- **Output:** `3`
- **Explanation:** Consider the subarray `[3, 5, 3]`. The pairs of elements at distinct indices have the following sums: 

 
 `3 + 5 = 8` 
 `3 + 3 = 6`, using the two different occurrences of 3 
 `5 + 3 = 8` 
 

 None of these sums is an element at the remaining index, so the subarray is valid. 

 Every subarray of length 4 contains 2, 3, and 5 at distinct indices, where `2 + 3 = 5`. Therefore, no longer valid subarray exists, and the answer is 3.

### Example 2
- **Input:** `nums = [3,4,5,6]`
- **Output:** `4`
- **Explanation:** The sums obtained from every pair of elements at distinct indices are 7, 8, 9, 9, 10, and 11. None of these values appears at the remaining index, so the entire array is valid.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Subarray With Restricted Pair Sums**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,5,3,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Consider the subarray `[3, 5, 3]`. The pairs of elements at distinct indices have the following sums: 

 
 `3 + 5 = 8` 
 `3 + 3 = 6`, using the two different occurrences of 3 
 `5 + 3 = 8` 
 

 None of these sums is an element at the remaining index, so the subarray is valid. 

 Every subarray of length 4 contains 2, 3, and 5 at distinct indices, where `2 + 3 = 5`. Therefore, no longer valid subarray exists, and the answer is 3.

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
    def maxSubarray(self, nums: List[int]) -> int:
        MAXV = 500
        last = [-1] * (2 * MAXV + 2)
        last2 = [-1] * (2 * MAXV + 2)
        L = -1
        best = 0
        for r, x in enumerate(nums):
            m = -1
            # r is the sum element: a + b == x
            for a in range(1, x):
                b = x - a
                if a > b:
                    break
                if a == b:
                    cand = last2[a]
                else:
                    cand = min(last[a], last[b])
                if cand >= 0 and cand > m:
                    m = cand
            # r is an addend: x + b == nums[k]
            for b in range(1, MAXV + 1):
                s = x + b
                if s > MAXV:
                    break
                j, k = last[b], last[s]
                if j >= 0 and k >= 0:
                    c = min(j, k)
                    if c > m:
                        m = c
            if m > L:
                L = m
            best = max(best, r - L)
            last2[x] = last[x]
            last[x] = r
        return best
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
- [2607. Make K-Subarray Sums Equal](../../2501-3000/2607-make-k-subarray-sums-equal/)
- [978. Longest Turbulent Subarray](../../0501-1000/0978-longest-turbulent-subarray/)
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1001-1500/1438-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subarray-with-restricted-pair-sums/)
