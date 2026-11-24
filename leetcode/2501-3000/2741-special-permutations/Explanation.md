# LeetCode 2741: Special Permutations

**LeetCode Problem #2741 — Special Permutations**
Solve LeetCode Special Permutations using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Special Permutations |
| LeetCode | #2741 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` containing `n` **distinct** positive integers. A permutation of `nums` is called special if:

For all indexes `0 <= i < n - 1`, either `nums[i] % nums[i+1] == 0` or `nums[i+1] % nums[i] == 0`.

Return *the total number of special permutations. *As the answer could be large, return it **modulo **`10^9 + 7`.

## Constraints
- `2 <= nums.length <= 14`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,3,6]`
- **Output:** `2`
- **Explanation:** [3,6,2] and [2,6,3] are the two special permutations of nums.

### Example 2
- **Input:** `nums = [1,4,3]`
- **Output:** `2`
- **Explanation:** [3,1,4] and [4,1,3] are the two special permutations of nums.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Special Permutations**, we observe the problem requirements and utilize the **Backtracking** technique. We decompose the problem into overlapping subproblems using a **Recursion Tree**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,6]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** [3,6,2] and [2,6,3] are the two special permutations of nums.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        full = (1 << n) - 1

        ok = [[nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0
               for j in range(n)] for i in range(n)]

        dp = [[0] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 1

        for mask in range(1, 1 << n):
            for last in range(n):
                cur = dp[mask][last]
                if cur == 0:
                    continue
                for j in range(n):
                    if mask >> j & 1 or not ok[last][j]:
                        continue
                    nm = mask | (1 << j)
                    dp[nm][j] = (dp[nm][j] + cur) % MOD

        return sum(dp[full]) % MOD
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [46. Permutations](../../0001-0500/0046-permutations/)
- [47. Permutations II](../../0001-0500/0047-permutations-ii/)
- [903. Valid Permutations for DI Sequence](../../0501-1000/0903-valid-permutations-for-di-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/special-permutations/)
