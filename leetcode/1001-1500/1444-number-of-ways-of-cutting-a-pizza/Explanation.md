# LeetCode 1444: Number of Ways of Cutting a Pizza

**LeetCode Problem #1444 — Number of Ways of Cutting a Pizza**
Solve LeetCode Number of Ways of Cutting a Pizza using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways of Cutting a Pizza |
| LeetCode | #1444 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a rectangular pizza represented as a `rows x cols` matrix containing the following characters: `'A'` (an apple) and `'.'` (empty cell) and given the integer `k`. You have to cut the pizza into `k` pieces using `k-1` cuts.

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

*Return the number of ways of cutting the pizza such that each piece contains **at least** one apple. *Since the answer can be a huge number, return this modulo 10^9 + 7.

## Constraints
- `1 <= rows, cols <= 50`
- `rows == pizza.length`
- `cols == pizza[i].length`
- `1 <= k <= 10`
- `pizza` consists of characters `'A'` and `'.'` only.

## Examples
### Example 1
- **Input:** `pizza = ["A..","AAA","..."], k = 3`
- **Output:** `3`
- **Explanation:** The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

### Example 2
- **Input:** `pizza = ["A..","AA.","..."], k = 3`
- **Output:** `1`

### Example 3
- **Input:** `pizza = ["A..","A..","..."], k = 1`
- **Output:** `1`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Ways of Cutting a Pizza**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `pizza = ["A..","AAA","..."], k = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

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
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        R, C = len(pizza), len(pizza[0])

        apples = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                apples[r][c] = (
                    (pizza[r][c] == 'A')
                    + apples[r + 1][c]
                    + apples[r][c + 1]
                    - apples[r + 1][c + 1]
                )

        dp = [[1 if apples[r][c] > 0 else 0 for c in range(C)] for r in range(R)]

        for _ in range(2, k + 1):
            new = [[0] * C for _ in range(R)]
            for r in range(R):
                for c in range(C):
                    total = 0
                    for i in range(r + 1, R):
                        if apples[r][c] - apples[i][c] > 0:
                            total += dp[i][c]
                    for i in range(c + 1, C):
                        if apples[r][c] - apples[r][i] > 0:
                            total += dp[r][i]
                    new[r][c] = total % MOD
            dp = new

        return dp[0][0]
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
- [1269. Number of Ways to Stay in the Same Place After Some Steps](../../1001-1500/1269-number-of-ways-to-stay-in-the-same-place-after-some-steps/)
- [1411. Number of Ways to Paint N × 3 Grid](../../1001-1500/1411-number-of-ways-to-paint-n-3-grid/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1001-1500/1434-number-of-ways-to-wear-different-hats-to-each-other/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/)
