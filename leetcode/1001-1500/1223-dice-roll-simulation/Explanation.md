# LeetCode 1223: Dice Roll Simulation

**LeetCode Problem #1223 — Dice Roll Simulation**
Solve LeetCode Dice Roll Simulation using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Dice Roll Simulation |
| LeetCode | #1223 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

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
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Dice Roll Simulation**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, rollMax = [1,1,2,2,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `34`.
4. **Verification:** There will be 2 rolls of die, if there are no

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

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
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1155. Number of Dice Rolls With Target Sum](../../1001-1500/1155-number-of-dice-rolls-with-target-sum/)
- [874. Walking Robot Simulation](../../0501-1000/0874-walking-robot-simulation/)
- [2069. Walking Robot Simulation II](../../2001-2500/2069-walking-robot-simulation-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/dice-roll-simulation/)
