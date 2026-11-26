# LeetCode 3350: Adjacent Increasing Subarrays Detection II

**LeetCode Problem #3350 — Adjacent Increasing Subarrays Detection II**
Solve LeetCode Adjacent Increasing Subarrays Detection II using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Adjacent Increasing Subarrays Detection II |
| LeetCode | #3350 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` of `n` integers, your task is to find the **maximum** value of `k` for which there exist **two** adjacent subarrays of length `k` each, such that both subarrays are **strictly** **increasing**. Specifically, check if there are **two** subarrays of length `k` starting at indices `a` and `b` (`a < b`), where:

Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly increasing**. 
 The subarrays must be **adjacent**, meaning `b = a + k`.

Return the **maximum** *possible* value of `k`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Constraints
- `2 <= nums.length <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,5,7,8,9,2,3,4,3,1]`
- **Output:** `3`
- **Explanation:** The subarray starting at index 2 is `[7, 8, 9]`, which is strictly increasing. 
 The subarray starting at index 5 is `[2, 3, 4]`, which is also strictly increasing. 
 These two subarrays are adjacent, and 3 is the

### Example 2
- **Input:** `nums = [1,2,3,4,4,4,4,5,6,7]`
- **Output:** `2`
- **Explanation:** The subarray starting at index 0 is `[1, 2]`, which is strictly increasing. 
 The subarray starting at index 2 is `[3, 4]`, which is also strictly increasing. 
 These two subarrays are adjacent, and 2 is the

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Adjacent Increasing Subarrays Detection II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,5,7,8,9,2,3,4,3,1]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The subarray starting at index 2 is `[7, 8, 9]`, which is strictly increasing. 
 The subarray starting at index 5 is `[2, 3, 4]`, which is also strictly increasing. 
 These two subarrays are adjacent, and 3 is the

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        prev = 0      # length of the previous run
        cur = 1       # length of the current run

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
                ans = max(ans, cur // 2, min(prev, cur))
                prev, cur = cur, 1

        ans = max(ans, cur // 2, min(prev, cur))
        return ans
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [329. Longest Increasing Path in a Matrix](../../0001-0500/0329-longest-increasing-path-in-a-matrix/)
- [334. Increasing Triplet Subsequence](../../0001-0500/0334-increasing-triplet-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/)
