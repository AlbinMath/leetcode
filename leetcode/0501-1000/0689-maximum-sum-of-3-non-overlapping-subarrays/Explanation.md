# LeetCode 689: Maximum Sum of 3 Non-Overlapping Subarrays

**LeetCode Problem #689 — Maximum Sum of 3 Non-Overlapping Subarrays**
Solve LeetCode Maximum Sum of 3 Non-Overlapping Subarrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of 3 Non-Overlapping Subarrays |
| LeetCode | #689 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and an integer `k`, find three non-overlapping subarrays of length `k` with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (**0-indexed**). If there are multiple answers, return the lexicographically smallest one.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i] < 2^16`
- `1 <= k <= floor(nums.length / 3)`

## Examples
### Example 1
- **Input:** `nums = [1,2,1,2,6,7,5,1], k = 2`
- **Output:** `[0,3,5]`
- **Explanation:** Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

### Example 2
- **Input:** `nums = [1,2,1,2,1,2,1,2,1], k = 2`
- **Output:** `[0,2,4]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Sum of 3 Non-Overlapping Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1,2,6,7,5,1], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,3,5]`.
4. **Verification:** Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

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
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        m = n - k + 1
        
        win = [0] * m
        curr_sum = sum(nums[:k])
        win[0] = curr_sum
        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]
            win[i - k + 1] = curr_sum
            
        left = [0] * m
        best_left = 0
        for i in range(m):
            if win[i] > win[best_left]:
                best_left = i
            left[i] = best_left
            
        right = [0] * m
        best_right = m - 1
        for i in range(m - 1, -1, -1):
            if win[i] >= win[best_right]:
                best_right = i
            right[i] = best_right
            
        ans = [0, k, 2 * k]
        max_total = -1
        for j in range(k, m - k):
            i = left[j - k]
            l = right[j + k]
            total = win[i] + win[j] + win[l]
            if total > max_total:
                max_total = total
                ans = [i, j, l]
                
        return ans
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
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1096-maximum-sum-of-two-non-overlapping-subarrays/)
- [3956. Maximum Sum of M Non-Overlapping Subarrays I](../../4001-4500/4123-maximum-sum-of-m-non-overlapping-subarrays-i/)
- [3957. Maximum Sum of M Non-Overlapping Subarrays II](../../4001-4500/4125-maximum-sum-of-m-non-overlapping-subarrays-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/)
