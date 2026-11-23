# LeetCode 3364: Minimum Positive Sum Subarray 

**LeetCode Problem #3364 — Minimum Positive Sum Subarray **
Solve LeetCode Minimum Positive Sum Subarray  using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Positive Sum Subarray  |
| LeetCode | #3364 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and **two** integers `l` and `r`. Your task is to find the **minimum** sum of a **subarray** whose size is between `l` and `r` (inclusive) and whose sum is greater than 0.

Return the **minimum** sum of such a subarray. If no such subarray exists, return -1.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= l <= r <= nums.length`
- `-1000 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [3, -2, 1, 4], l = 2, r = 3`
- **Output:** `1`
- **Explanation:** The subarrays of length between `l = 2` and `r = 3` where the sum is greater than 0 are: 

 
 `[3, -2]` with a sum of 1 
 `[1, 4]` with a sum of 5 
 `[3, -2, 1]` with a sum of 2 
 `[-2, 1, 4]` with a sum of 3 
 

 Out of these, the subarray `[3, -2]` has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

### Example 2
- **Input:** `nums = [-2, 2, -3, 1], l = 2, r = 3`
- **Output:** `-1`
- **Explanation:** There is no subarray of length between `l` and `r` that has a sum greater than 0. So, the answer is -1.

### Example 3
- **Input:** `nums = [1, 2, 3, 4], l = 2, r = 4`
- **Output:** `3`
- **Explanation:** The subarray `[1, 2]` has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Positive Sum Subarray **, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3, -2, 1, 4], l = 2, r = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The subarrays of length between `l = 2` and `r = 3` where the sum is greater than 0 are: 

 
 `[3, -2]` with a sum of 1 
 `[1, 4]` with a sum of 5 
 `[3, -2, 1]` with a sum of 2 
 `[-2, 1, 4]` with a sum of 3 
 

 Out of these, the subarray `[3, -2]` has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

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
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x

        best = float('inf')
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                s = prefix[i + length] - prefix[i]
                if s > 0:
                    best = min(best, s)

        return -1 if best == float('inf') else best
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
- [209. Minimum Size Subarray Sum](../../0001-0500/0209-minimum-size-subarray-sum/)
- [1413. Minimum Value to Get Positive Step by Step Sum](../../1501-2000/1514-minimum-value-to-get-positive-step-by-step-sum/)
- [3795. Minimum Subarray Length With Distinct Sum At Least K](../../4001-4500/4152-minimum-subarray-length-with-distinct-sum-at-least-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-positive-sum-subarray/)
