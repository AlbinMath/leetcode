# LeetCode 1269: Number of Ways to Stay in the Same Place After Some Steps

**LeetCode Problem #1269 — Number of Ways to Stay in the Same Place After Some Steps**
Solve LeetCode Number of Ways to Stay in the Same Place After Some Steps using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Stay in the Same Place After Some Steps |
| LeetCode | #1269 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have a pointer at index `0` in an array of size `arrLen`. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers `steps` and `arrLen`, return the number of ways such that your pointer is still at index `0` after **exactly** `steps` steps. Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= steps <= 500`
- `1 <= arrLen <= 10^6`

## Examples
### Example 1
- **Input:** `steps = 3, arrLen = 2`
- **Output:** `4`
- **Explanation:** There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay

### Example 2
- **Input:** `steps = 2, arrLen = 4`
- **Output:** `2`
- **Explanation:** There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay

### Example 3
- **Input:** `steps = 4, arrLen = 2`
- **Output:** `8`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Ways to Stay in the Same Place After Some Steps**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `steps = 3, arrLen = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay

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
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_pos = min(arrLen - 1, steps // 2)
        
        dp = [0] * (max_pos + 1)
        dp[0] = 1
        
        for _ in range(steps):
            next_dp = [0] * (max_pos + 1)
            for i in range(max_pos + 1):
                ways = dp[i]
                if i > 0:
                    ways += dp[i - 1]
                if i < max_pos:
                    ways += dp[i + 1]
                next_dp[i] = ways % MOD
            dp = next_dp
            
        return dp[0]
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
- [2400. Number of Ways to Reach a Position After Exactly k Steps](../../2001-2500/2400-number-of-ways-to-reach-a-position-after-exactly-k-steps/)
- [1569. Number of Ways to Reorder Array to Get Same BST](../../1501-2000/1569-number-of-ways-to-reorder-array-to-get-same-bst/)
- [3025. Find the Number of Ways to Place People I](../../3001-3500/3025-find-the-number-of-ways-to-place-people-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/)
