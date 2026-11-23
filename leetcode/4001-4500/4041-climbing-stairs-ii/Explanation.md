# LeetCode 3693: Climbing Stairs II

**LeetCode Problem #3693 — Climbing Stairs II**
Solve LeetCode Climbing Stairs II using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Climbing Stairs II |
| LeetCode | #3693 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are climbing a staircase with `n + 1` steps, numbered from 0 to `n`.

You are also given a **1-indexed** integer array `costs` of length `n`, where `costs[i]` is the cost of step `i`.

From step `i`, you can jump **only** to step `i + 1`, `i + 2`, or `i + 3`. The cost of jumping from step `i` to step `j` is defined as: `costs[j] + (j - i)^2`

You start from step 0 with `cost = 0`.

Return the **minimum** total cost to reach step `n`.

## Constraints
- `1 <= n == costs.length <= 10^5​​​​​​​`
- `1 <= costs[i] <= 10^4`

## Examples
### Example 1
- **Input:** `n = 4, costs = [1,2,3,4]`
- **Output:** `13`
- **Explanation:** One optimal path is `0 &rarr; 1 &rarr; 2 &rarr; 4` 

 
 
 
 Jump 
 Cost Calculation 
 Cost 
 
 
 
 
 0 &rarr; 1 
 `costs[1] + (1 - 0)^2 = 1 + 1` 
 2 
 
 
 1 &rarr; 2 
 `costs[2] + (2 - 1)^2 = 2 + 1` 
 3 
 
 
 2 &rarr; 4 
 `costs[4] + (4 - 2)^2 = 4 + 4` 
 8 
 
 
 

 Thus, the minimum total cost is `2 + 3 + 8 = 13`

### Example 2
- **Input:** `n = 4, costs = [5,1,6,2]`
- **Output:** `11`
- **Explanation:** One optimal path is `0 &rarr; 2 &rarr; 4` 

 
 
 
 Jump 
 Cost Calculation 
 Cost 
 
 
 
 
 0 &rarr; 2 
 `costs[2] + (2 - 0)^2 = 1 + 4` 
 5 
 
 
 2 &rarr; 4 
 `costs[4] + (4 - 2)^2 = 2 + 4` 
 6 
 
 
 

 Thus, the minimum total cost is `5 + 6 = 11`

### Example 3
- **Input:** `n = 3, costs = [9,8,3]`
- **Output:** `12`
- **Explanation:** The optimal path is `0 &rarr; 3` with total cost = `costs[3] + (3 - 0)^2 = 3 + 9 = 12`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Climbing Stairs II**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, costs = [1,2,3,4]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** One optimal path is `0 &rarr; 1 &rarr; 2 &rarr; 4` 

 
 
 
 Jump 
 Cost Calculation 
 Cost 
 
 
 
 
 0 &rarr; 1 
 `costs[1] + (1 - 0)^2 = 1 + 1` 
 2 
 
 
 1 &rarr; 2 
 `costs[2] + (2 - 1)^2 = 2 + 1` 
 3 
 
 
 2 &rarr; 4 
 `costs[4] + (4 - 2)^2 = 4 + 4` 
 8 
 
 
 

 Thus, the minimum total cost is `2 + 3 + 8 = 13`

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
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            for d in (1, 2, 3):
                i = j - d
                if i >= 0:
                    dp[j] = min(dp[j], dp[i] + costs[j - 1] + d * d)
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
- [70. Climbing Stairs](../../0001-0500/0070-climbing-stairs/)
- [746. Min Cost Climbing Stairs](../../0501-1000/0747-min-cost-climbing-stairs/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/climbing-stairs-ii/)
