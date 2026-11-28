# LeetCode 935: Knight Dialer

**LeetCode Problem #935 — Knight Dialer**
Solve LeetCode Knight Dialer using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Knight Dialer |
| LeetCode | #935 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
The chess knight has a **unique movement**, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an **L**). The possible movements of chess knight are shown in this diagram:

A chess knight can move as indicated in the chess diagram below:

We have a chess knight and a phone pad as shown below, the knight **can only stand on a numeric cell** (i.e. blue cell).

Given an integer `n`, return how many distinct phone numbers of length `n` we can dial.

You are allowed to place the knight **on any numeric cell** initially and then you should perform `n - 1` jumps to dial a number of length `n`. All jumps should be **valid** knight jumps.

As the answer may be very large, **return the answer modulo** `10^9 + 7`.

## Constraints
- `1 <= n <= 5000`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `10`
- **Explanation:** We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

### Example 2
- **Input:** `n = 2`
- **Output:** `20`
- **Explanation:** All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

### Example 3
- **Input:** `n = 3131`
- **Output:** `136006598`
- **Explanation:** Please take care of the mod.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Knight Dialer**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

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
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = [
            [4, 6],     # 0
            [6, 8],     # 1
            [7, 9],     # 2
            [4, 8],     # 3
            [0, 3, 9],  # 4
            [],         # 5
            [0, 1, 7],  # 6
            [2, 6],     # 7
            [1, 3],     # 8
            [2, 4]      # 9
        ]
        dp = [1] * 10
        
        for _ in range(n - 1):
            next_dp = [0] * 10
            for digit in range(10):
                for prev_digit in moves[digit]:
                    next_dp[digit] = (next_dp[digit] + dp[prev_digit]) % MOD
            dp = next_dp
            
        return sum(dp) % MOD
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
- [688. Knight Probability in Chessboard](../../0501-1000/0688-knight-probability-in-chessboard/)
- [2596. Check Knight Tour Configuration](../../2501-3000/2596-check-knight-tour-configuration/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/knight-dialer/)
