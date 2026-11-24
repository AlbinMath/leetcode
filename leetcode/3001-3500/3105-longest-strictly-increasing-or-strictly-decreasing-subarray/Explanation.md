# LeetCode 3105: Longest Strictly Increasing or Strictly Decreasing Subarray

**LeetCode Problem #3105 — Longest Strictly Increasing or Strictly Decreasing Subarray**
Solve LeetCode Longest Strictly Increasing or Strictly Decreasing Subarray using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Strictly Increasing or Strictly Decreasing Subarray |
| LeetCode | #3105 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of integers `nums`. Return *the length of the **longest** subarray of *`nums`* which is either ** strictly increasing ** or ** strictly decreasing ***.

## Constraints
- `1 <= nums.length <= 50`
- `1 <= nums[i] <= 50`

## Examples
### Example 1
- **Input:** `nums = [1,4,3,3,2]`
- **Output:** `2`
- **Explanation:** The strictly increasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, and `[1,4]`. 

 The strictly decreasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, `[3,2]`, and `[4,3]`. 

 Hence, we return `2`.

### Example 2
- **Input:** `nums = [3,3,3,3]`
- **Output:** `1`
- **Explanation:** The strictly increasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`. 

 The strictly decreasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`. 

 Hence, we return `1`.

### Example 3
- **Input:** `nums = [3,2,1]`
- **Output:** `3`
- **Explanation:** The strictly increasing subarrays of `nums` are `[3]`, `[2]`, and `[1]`. 

 The strictly decreasing subarrays of `nums` are `[3]`, `[2]`, `[1]`, `[3,2]`, `[2,1]`, and `[3,2,1]`. 

 Hence, we return `3`.

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Longest Strictly Increasing or Strictly Decreasing Subarray**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,3,3,2]`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The strictly increasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, and `[1,4]`. 

 The strictly decreasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, `[3,2]`, and `[4,3]`. 

 Hence, we return `2`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            best = max(best, inc, dec)
        return best
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](../../3501-4000/3825-longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)
- [1909. Remove One Element to Make the Array Strictly Increasing](../../1501-2000/1909-remove-one-element-to-make-the-array-strictly-increasing/)
- [2713. Maximum Strictly Increasing Cells in a Matrix](../../2501-3000/2713-maximum-strictly-increasing-cells-in-a-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)
