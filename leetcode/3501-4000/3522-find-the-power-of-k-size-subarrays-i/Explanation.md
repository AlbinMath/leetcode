# LeetCode 3254: Find the Power of K-Size Subarrays I

**LeetCode Problem #3254 — Find the Power of K-Size Subarrays I**
Solve LeetCode Find the Power of K-Size Subarrays I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Power of K-Size Subarrays I |
| LeetCode | #3254 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums` of length `n` and a *positive* integer `k`.

The **power** of an array is defined as:

Its **maximum** element if *all* of its elements are **consecutive** and **sorted** in **ascending** order. 
 -1 otherwise.

You need to find the **power** of all subarrays of `nums` of size `k`.

Return an integer array `results` of size `n - k + 1`, where `results[i]` is the *power* of `nums[i..(i + k - 1)]`.

## Constraints
- `1 <= n == nums.length <= 500`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,3,2,5], k = 3`
- **Output:** `[3,4,-1,-1,-1]`
- **Explanation:** There are 5 subarrays of `nums` of size 3: 

 
 `[1, 2, 3]` with the maximum element 3. 
 `[2, 3, 4]` with the maximum element 4. 
 `[3, 4, 3]` whose elements are

### Example 2
- **Input:** `nums = [2,2,2,2,2], k = 4`
- **Output:** `[-1,-1]`

### Example 3
- **Input:** `nums = [3,2,3,2,3,2], k = 2`
- **Output:** `[-1,3,-1,3,-1]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Power of K-Size Subarrays I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,3,2,5], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4,-1,-1,-1]`.
4. **Verification:** There are 5 subarrays of `nums` of size 3: 

 
 `[1, 2, 3]` with the maximum element 3. 
 `[2, 3, 4]` with the maximum element 4. 
 `[3, 4, 3]` whose elements are

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
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        run = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                run += 1
            else:
                run = 1
            if i >= k - 1:
                res.append(nums[i] if run >= k else -1)
        return res
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
- [3255. Find the Power of K-Size Subarrays II](../../3501-4000/3523-find-the-power-of-k-size-subarrays-ii/)
- [3430. Maximum and Minimum Sums of at Most Size K Subarrays](../../3501-4000/3725-maximum-and-minimum-sums-of-at-most-size-k-subarrays/)
- [3318. Find X-Sum of All K-Long Subarrays I](../../3501-4000/3610-find-x-sum-of-all-k-long-subarrays-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/)
