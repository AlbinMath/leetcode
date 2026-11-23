# LeetCode 1866: Number of Ways to Rearrange Sticks With K Sticks Visible

**LeetCode Problem #1866 — Number of Ways to Rearrange Sticks With K Sticks Visible**
Solve LeetCode Number of Ways to Rearrange Sticks With K Sticks Visible using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Rearrange Sticks With K Sticks Visible |
| LeetCode | #1866 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` uniquely-sized sticks whose lengths are integers from `1` to `n`. You want to arrange the sticks such that **exactly** `k` sticks are **visible** from the left. A stick is **visible** from the left if there are no **longer** sticks to the **left** of it.

For example, if the sticks are arranged `[ 1 , 3 ,2, 5 ,4]`, then the sticks with lengths `1`, `3`, and `5` are visible from the left.

Given `n` and `k`, return *the **number** of such arrangements*. Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= n <= 1000`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `n = 3, k = 2`
- **Output:** `3`
- **Explanation:** [ 1 , 3 ,2], [ 2 , 3 ,1], and [ 2 ,1, 3 ] are the only arrangements such that exactly 2 sticks are visible.
The visible sticks are underlined.

### Example 2
- **Input:** `n = 5, k = 5`
- **Output:** `1`
- **Explanation:** [ 1 , 2 , 3 , 4 , 5 ] is the only arrangement such that all 5 sticks are visible.
The visible sticks are underlined.

### Example 3
- **Input:** `n = 20, k = 11`
- **Output:** `647427950`
- **Explanation:** There are 647427950 (mod 10^9 + 7) ways to rearrange the sticks such that exactly 11 sticks are visible.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Ways to Rearrange Sticks With K Sticks Visible**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** [ 1 , 3 ,2], [ 2 , 3 ,1], and [ 2 ,1, 3 ] are the only arrangements such that exactly 2 sticks are visible.
The visible sticks are underlined.

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
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(min(i, k), 0, -1):
                dp[j] = (dp[j - 1] + dp[j] * (i - 1)) % MOD
            dp[0] = 0
        return dp[k]
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
- [2400. Number of Ways to Reach a Position After Exactly k Steps](../../2001-2500/2477-number-of-ways-to-reach-a-position-after-exactly-k-steps/)
- [3154. Find Number of Ways to Reach the K-th Stair](../../3001-3500/3414-find-number-of-ways-to-reach-the-k-th-stair/)
- [995. Minimum Number of K Consecutive Bit Flips](../../1001-1500/1037-minimum-number-of-k-consecutive-bit-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/)
