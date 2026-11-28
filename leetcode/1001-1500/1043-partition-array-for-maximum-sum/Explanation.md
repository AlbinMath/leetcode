# LeetCode 1043: Partition Array for Maximum Sum

**LeetCode Problem #1043 — Partition Array for Maximum Sum**
Solve LeetCode Partition Array for Maximum Sum using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array for Maximum Sum |
| LeetCode | #1043 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

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
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Partition Array for Maximum Sum**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,15,7,9,2,5,10], k = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `84`.
4. **Verification:** arr becomes [15,15,15,9,10,10,10]

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

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
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1013. Partition Array Into Three Parts With Equal Sum](../../1001-1500/1013-partition-array-into-three-parts-with-equal-sum/)
- [1877. Minimize Maximum Pair Sum in Array](../../1501-2000/1877-minimize-maximum-pair-sum-in-array/)
- [2025. Maximum Number of Ways to Partition an Array](../../2001-2500/2025-maximum-number-of-ways-to-partition-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-for-maximum-sum/)
