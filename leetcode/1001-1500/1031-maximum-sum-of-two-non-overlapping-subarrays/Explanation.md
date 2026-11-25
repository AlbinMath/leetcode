# LeetCode 1031: Maximum Sum of Two Non-Overlapping Subarrays

**LeetCode Problem #1031 — Maximum Sum of Two Non-Overlapping Subarrays**
Solve LeetCode Maximum Sum of Two Non-Overlapping Subarrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of Two Non-Overlapping Subarrays |
| LeetCode | #1031 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and two integers `firstLen` and `secondLen`, return *the maximum sum of elements in two non-overlapping **subarrays** with lengths *`firstLen`* and *`secondLen`.

The array with length `firstLen` could occur before or after the array with length `secondLen`, but they have to be non-overlapping.

A **subarray** is a **contiguous** part of an array.

## Constraints
- `1 <= firstLen, secondLen <= 1000`
- `2 <= firstLen + secondLen <= 1000`
- `firstLen + secondLen <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2`
- **Output:** `20`
- **Explanation:** One choice of subarrays is [9] with length 1, and [6,5] with length 2.

### Example 2
- **Input:** `nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2`
- **Output:** `29`
- **Explanation:** One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

### Example 3
- **Input:** `nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3`
- **Output:** `31`
- **Explanation:** One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Sum of Two Non-Overlapping Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `20`.
4. **Verification:** One choice of subarrays is [9] with length 1, and [6,5] with length 2.

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
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def max_two(L: int, M: int) -> int:
            sum_L = sum(nums[:L])
            sum_M = sum(nums[L : L + M])
            max_L = sum_L
            ans = max_L + sum_M
            
            for i in range(L + M, len(nums)):
                sum_L += nums[i - M] - nums[i - M - L]
                sum_M += nums[i] - nums[i - M]
                if sum_L > max_L:
                    max_L = sum_L
                if max_L + sum_M > ans:
                    ans = max_L + sum_M
                    
            return ans
            
        return max(max_two(firstLen, secondLen), max_two(secondLen, firstLen))
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
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](../../1501-2000/1546-maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)
- [3956. Maximum Sum of M Non-Overlapping Subarrays I](../../3501-4000/3956-maximum-sum-of-m-non-overlapping-subarrays-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/)
