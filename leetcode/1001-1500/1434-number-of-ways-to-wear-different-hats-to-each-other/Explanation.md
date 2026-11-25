# LeetCode 1434: Number of Ways to Wear Different Hats to Each Other

**LeetCode Problem #1434 — Number of Ways to Wear Different Hats to Each Other**
Solve LeetCode Number of Ways to Wear Different Hats to Each Other using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Wear Different Hats to Each Other |
| LeetCode | #1434 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` people and `40` types of hats labeled from `1` to `40`.

Given a 2D integer array `hats`, where `hats[i]` is a list of all hats preferred by the `i^th` person.

Return the number of ways that `n` people can wear **different** hats from each other.

Since the answer may be too large, return it modulo `10^9 + 7`.

## Constraints
- `n == hats.length`
- `1 <= n <= 10`
- `1 <= hats[i].length <= 40`
- `1 <= hats[i][j] <= 40`
- `hats[i]` contains a list of **unique** integers.

## Examples
### Example 1
- **Input:** `hats = [[3,4],[4,5],[5]]`
- **Output:** `1`
- **Explanation:** There is only one way to choose hats given the conditions. 
First person chooses hat 3, Second person chooses hat 4 and last one hat 5.

### Example 2
- **Input:** `hats = [[3,5,1],[3,5]]`
- **Output:** `4`
- **Explanation:** There are 4 ways to choose hats:
(3,5), (5,3), (1,3) and (1,5)

### Example 3
- **Input:** `hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]`
- **Output:** `24`
- **Explanation:** Each person can choose hats labeled from 1 to 4.
Number of Permutations of (1,2,3,4) = 24.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Ways to Wear Different Hats to Each Other**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `hats = [[3,4],[4,5],[5]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There is only one way to choose hats given the conditions. 
First person chooses hat 3, Second person chooses hat 4 and last one hat 5.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var numberWays = function (hats) {
  const MOD = 1000000007, n = hats.length, full = (1 << n) - 1;
  const byHat = Array.from({ length: 41 }, () => []);
  hats.forEach((list, p) => list.forEach((h) => byHat[h].push(p)));
  const dp = new Array(1 << n).fill(0);
  dp[0] = 1;
  for (let h = 1; h <= 40; h++) for (let m = full; m >= 0; m--) for (const p of byHat[h]) if (dp[m] && !(m & (1 << p))) dp[m | (1 << p)] = (dp[m | (1 << p)] + dp[m]) % MOD;
  return dp[full];
};
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
- [1178. Number of Valid Words for Each Puzzle](../../1001-1500/1178-number-of-valid-words-for-each-puzzle/)
- [1444. Number of Ways of Cutting a Pizza](../../1001-1500/1444-number-of-ways-of-cutting-a-pizza/)
- [1525. Number of Good Ways to Split a String](../../1501-2000/1525-number-of-good-ways-to-split-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/)
