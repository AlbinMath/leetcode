# LeetCode 3825: Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND

**LeetCode Problem #3825 — Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND**
Solve LeetCode Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND |
| LeetCode | #3825 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Return the length of the **longest strictly increasing subsequence ** in `nums` whose bitwise **AND** is **non-zero**. If no such **subsequence** exists, return 0.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`​​​​​​​

## Examples
### Example 1
- **Input:** `nums = [5,4,7]`
- **Output:** `2`
- **Explanation:** One longest strictly increasing subsequence is `[5, 7]`. The bitwise AND is `5 AND 7 = 5`, which is non-zero.

### Example 2
- **Input:** `nums = [2,3,6]`
- **Output:** `3`
- **Explanation:** The longest strictly increasing subsequence is `[2, 3, 6]`. The bitwise AND is `2 AND 3 AND 6 = 2`, which is non-zero.

### Example 3
- **Input:** `nums = [0,1]`
- **Output:** `1`
- **Explanation:** One longest strictly increasing subsequence is `[1]`. The bitwise AND is 1, which is non-zero.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,4,7]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One longest strictly increasing subsequence is `[5, 7]`. The bitwise AND is `5 AND 7 = 5`, which is non-zero.

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
from bisect import bisect_left

class Solution(object):
    def longestSubsequence(self, nums):
        best = 0
        for b in range(30):
            tails = []
            for x in nums:
                if (x >> b) & 1:
                    i = bisect_left(tails, x)
                    if i == len(tails):
                        tails.append(x)
                    else:
                        tails[i] = x
            if len(tails) > best:
                best = len(tails)
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
- [3702. Longest Subsequence With Non-Zero Bitwise XOR](../../3501-4000/3702-longest-subsequence-with-non-zero-bitwise-xor/)
- [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](../../3001-3500/3105-longest-strictly-increasing-or-strictly-decreasing-subarray/)
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)
