# LeetCode 1155: Number of Dice Rolls With Target Sum

**LeetCode Problem #1155 — Number of Dice Rolls With Target Sum**
Solve LeetCode Number of Dice Rolls With Target Sum using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Dice Rolls With Target Sum |
| LeetCode | #1155 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have `n` dice, and each dice has `k` faces numbered from `1` to `k`.

Given three integers `n`, `k`, and `target`, return *the number of possible ways (out of the *`k^n`* total ways) **to roll the dice, so the sum of the face-up numbers equals *`target`. Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= n, k <= 30`
- `1 <= target <= 1000`

## Examples
### Example 1
- **Input:** `n = 1, k = 6, target = 3`
- **Output:** `1`
- **Explanation:** You throw one die with 6 faces.
There is only one way to get a sum of 3.

### Example 2
- **Input:** `n = 2, k = 6, target = 7`
- **Output:** `6`
- **Explanation:** You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

### Example 3
- **Input:** `n = 30, k = 30, target = 500`
- **Output:** `222616187`
- **Explanation:** The answer must be returned modulo 10^9 + 7.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Dice Rolls With Target Sum**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1, k = 6, target = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** You throw one die with 6 faces.
There is only one way to get a sum of 3.

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
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n or target > n * k:
            return 0
            
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for dice in range(1, n + 1):
            next_dp = [0] * (target + 1)
            # Sum with `dice` dice is bounded between `dice` and `min(dice * k, target)`
            for s in range(dice, min(dice * k, target) + 1):
                for face in range(1, min(k, s) + 1):
                    next_dp[s] = (next_dp[s] + dp[s - face]) % MOD
            dp = next_dp
            
        return dp[target]
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
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1074-number-of-submatrices-that-sum-to-target/)
- [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](../../1501-2000/1546-maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)
- [1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](../../1001-1500/1414-find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)
