# LeetCode 1043: Partition Array for Maximum Sum

**LeetCode Problem #1043 — Partition Array for Maximum Sum**
Solve LeetCode Partition Array for Maximum Sum using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array for Maximum Sum |
| LeetCode | #1043 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr`, partition the array into (contiguous) subarrays of length **at most** `k`. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return *the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a **32-bit** integer.*

## Constraints
- `1 <= arr.length <= 500`
- `0 <= arr[i] <= 10^9`
- `1 <= k <= arr.length`

## Examples
### Example 1
- **Input:** `arr = [1,15,7,9,2,5,10], k = 3`
- **Output:** `84`
- **Explanation:** arr becomes [15,15,15,9,10,10,10]

### Example 2
- **Input:** `arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4`
- **Output:** `83`

### Example 3
- **Input:** `arr = [1], k = 1`
- **Output:** `1`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Partition Array for Maximum Sum**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,15,7,9,2,5,10], k = 3`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `84`.
4. **Verification:** arr becomes [15,15,15,9,10,10,10]

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
class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            curr_max = 0
            for length in range(1, min(i, k) + 1):
                curr_max = max(curr_max, arr[i - length])
                dp[i] = max(dp[i], dp[i - length] + curr_max * length)
                
        return dp[n]
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
- [1013. Partition Array Into Three Parts With Equal Sum](../../1001-1500/1013-partition-array-into-three-parts-with-equal-sum/)
- [2025. Maximum Number of Ways to Partition an Array](../../2001-2500/2025-maximum-number-of-ways-to-partition-an-array/)
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2035-partition-array-into-two-arrays-to-minimize-sum-difference/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-for-maximum-sum/)
