# LeetCode 2653: Sliding Subarray Beauty

**LeetCode Problem #2653 — Sliding Subarray Beauty**
Solve LeetCode Sliding Subarray Beauty using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sliding Subarray Beauty |
| LeetCode | #2653 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` containing `n` integers, find the **beauty** of each subarray of size `k`.

The **beauty** of a subarray is the `x^th`** smallest integer **in the subarray if it is **negative**, or `0` if there are fewer than `x` negative integers.

Return *an integer array containing *`n - k + 1` *integers, which denote the ***beauty*** of the subarrays **in order** from the first index in the array.*

A subarray is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `n == nums.length `
- `1 <= n <= 10^5`
- `1 <= k <= n`
- `1 <= x <= k `
- `-50 <= nums[i] <= 50 `

## Examples
### Example 1
- **Input:** `nums = [1,-1,-3,-2,3], k = 3, x = 2`
- **Output:** `[-1,-2,-2]`
- **Explanation:** There are 3 subarrays with size k = 3. 
The first subarray is `[1, -1, -3]` and the 2^nd smallest negative integer is -1. 
The second subarray is `[-1, -3, -2]` and the 2^nd smallest negative integer is -2. 
The third subarray is `[-3, -2, 3] `and the 2^nd smallest negative integer is -2.

### Example 2
- **Input:** `nums = [-1,-2,-3,-4,-5], k = 2, x = 2`
- **Output:** `[-1,-2,-3,-4]`
- **Explanation:** There are 4 subarrays with size k = 2.
For `[-1, -2]`, the 2^nd smallest negative integer is -1.
For `[-2, -3]`, the 2^nd smallest negative integer is -2.
For `[-3, -4]`, the 2^nd smallest negative integer is -3.
For `[-4, -5]`, the 2^nd smallest negative integer is -4.

### Example 3
- **Input:** `nums = [-3,1,2,-3,0,-3], k = 2, x = 1`
- **Output:** `[-3,0,-3,-3,-3]`
- **Explanation:** There are 5 subarrays with size k = 2

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Sliding Subarray Beauty**, we observe the problem requirements and utilize the **Sliding Window** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,-1,-3,-2,3], k = 3, x = 2`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[-1,-2,-2]`.
4. **Verification:** There are 3 subarrays with size k = 3. 
The first subarray is `[1, -1, -3]` and the 2^nd smallest negative integer is -1. 
The second subarray is `[-1, -3, -2]` and the 2^nd smallest negative integer is -2. 
The third subarray is `[-3, -2, 3] `and the 2^nd smallest negative integer is -2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = [0] * 50
        ans = []
        
        for i, val in enumerate(nums):
            if val < 0:
                freq[val + 50] += 1
                
            if i >= k and nums[i - k] < 0:
                freq[nums[i - k] + 50] -= 1
                
            if i >= k - 1:
                count = 0
                beauty = 0
                for idx in range(50):
                    count += freq[idx]
                    if count >= x:
                        beauty = idx - 50
                        break
                ans.append(beauty)
                
        return ans
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [1781. Sum of Beauty of All Substrings](../../1501-2000/1890-sum-of-beauty-of-all-substrings/)
- [2234. Maximum Total Beauty of the Gardens](../../2001-2500/2330-maximum-total-beauty-of-the-gardens/)
- [2269. Find the K-Beauty of a Number](../../1001-1500/1430-find-the-k-beauty-of-a-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sliding-subarray-beauty/)
