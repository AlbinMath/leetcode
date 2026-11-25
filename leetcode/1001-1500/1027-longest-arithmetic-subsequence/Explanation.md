# LeetCode 1027: Longest Arithmetic Subsequence

**LeetCode Problem #1027 — Longest Arithmetic Subsequence**
Solve LeetCode Longest Arithmetic Subsequence using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Arithmetic Subsequence |
| LeetCode | #1027 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array `nums` of integers, return *the length of the longest arithmetic subsequence in* `nums`.

**Note** that:

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements. 
 A sequence `seq` is arithmetic if `seq[i + 1] - seq[i]` are all the same value (for `0 <= i < seq.length - 1`).

## Constraints
- `2 <= nums.length <= 1500`
- `0 <= nums[i] <= 500`

## Examples
### Example 1
- **Input:** `nums = [3, 6, 9, 12]`
- **Output:** `4`
- **Explanation:** The whole array is already an arithmetic sequence with a common difference of 3, so the longest arithmetic subsequence is `[3, 6, 9, 12]`, of length 4.

### Example 2
- **Input:** `nums = [9, 4, 7, 2, 10]`
- **Output:** `3`
- **Explanation:** The longest arithmetic subsequence is `[4, 7, 10]` (indices `1`, `2`, `4`), with a common difference of 3. There is no arithmetic subsequence of length 4.

### Example 3
- **Input:** `nums = [20, 1, 15, 3, 10, 5, 8]`
- **Output:** `4`
- **Explanation:** The longest arithmetic subsequence is `[20, 15, 10, 5]` (indices `0`, `2`, `4`, `5`), with a common difference of -5.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Longest Arithmetic Subsequence**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3, 6, 9, 12]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The whole array is already an arithmetic sequence with a common difference of 3, so the longest arithmetic subsequence is `[3, 6, 9, 12]`, of length 4.

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
from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        OFFSET = 500
        dp = [[1] * 1001 for _ in range(n)]   # dp[i][d + OFFSET], default length 1
        best = 2

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j] + OFFSET
                dp[i][d] = dp[j][d] + 1
                best = max(best, dp[i][d])

        return best
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
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [516. Longest Palindromic Subsequence](../../0501-1000/0516-longest-palindromic-subsequence/)
- [521. Longest Uncommon Subsequence I](../../0501-1000/0521-longest-uncommon-subsequence-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-arithmetic-subsequence/)
