# LeetCode 1223: Dice Roll Simulation

**LeetCode Problem #1223 — Dice Roll Simulation**
Solve LeetCode Dice Roll Simulation using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Dice Roll Simulation |
| LeetCode | #1223 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A die simulator generates a random number from `1` to `6` for each roll. You introduced a constraint to the generator such that it cannot roll the number `i` more than `rollMax[i]` (**1-indexed**) consecutive times.

Given an array of integers `rollMax` and an integer `n`, return *the number of distinct sequences that can be obtained with exact *`n`* rolls*. Since the answer may be too large, return it **modulo** `10^9 + 7`.

Two sequences are considered different if at least one element differs from each other.

## Constraints
- `1 <= n <= 5000`
- `rollMax.length == 6`
- `1 <= rollMax[i] <= 15`

## Examples
### Example 1
- **Input:** `n = 2, rollMax = [1,1,2,2,2,3]`
- **Output:** `34`
- **Explanation:** There will be 2 rolls of die, if there are no

### Example 2
- **Input:** `n = 2, rollMax = [1,1,1,1,1,1]`
- **Output:** `30`

### Example 3
- **Input:** `n = 3, rollMax = [1,1,1,2,2,3]`
- **Output:** `181`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Dice Roll Simulation**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, rollMax = [1,1,2,2,2,3]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `34`.
4. **Verification:** There will be 2 rolls of die, if there are no

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
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (rollMax[j] + 1) for j in range(6)]
        for j in range(6):
            dp[j][1] = 1
            
        for _ in range(1, n):
            next_dp = [[0] * (rollMax[j] + 1) for j in range(6)]
            row_sums = [sum(dp[j]) % MOD for j in range(6)]
            total_prev = sum(row_sums) % MOD
            
            for j in range(6):
                next_dp[j][1] = (total_prev - row_sums[j]) % MOD
                
                for k in range(2, rollMax[j] + 1):
                    next_dp[j][k] = dp[j][k - 1]
                    
            dp = next_dp
            
        return sum(sum(row) for row in dp) % MOD
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
- [1155. Number of Dice Rolls With Target Sum](../../1001-1500/1155-number-of-dice-rolls-with-target-sum/)
- [2318. Number of Distinct Roll Sequences](../../2001-2500/2318-number-of-distinct-roll-sequences/)
- [874. Walking Robot Simulation](../../0501-1000/0874-walking-robot-simulation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/dice-roll-simulation/)
