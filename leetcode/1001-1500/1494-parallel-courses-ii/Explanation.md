# LeetCode 1494: Parallel Courses II

**LeetCode Problem #1494 — Parallel Courses II**
Solve LeetCode Parallel Courses II using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Parallel Courses II |
| LeetCode | #1494 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given an array `relations` where `relations[i] = [prevCourse_i, nextCourse_i]`, representing a prerequisite relationship between course `prevCourse_i` and course `nextCourse_i`: course `prevCourse_i` has to be taken before course `nextCourse_i`. Also, you are given the integer `k`.

In one semester, you can take **at most** `k` courses as long as you have taken all the prerequisites in the **previous** semesters for the courses you are taking.

Return *the **minimum** number of semesters needed to take all courses*. The testcases will be generated such that it is possible to take every course.

## Constraints
- `1 <= n <= 15`
- `1 <= k <= n`
- `0 <= relations.length <= n * (n-1) / 2`
- `relations[i].length == 2`
- `1 <= prevCourse_i, nextCourse_i <= n`
- `prevCourse_i != nextCourse_i`
- All the pairs `[prevCourse_i, nextCourse_i]` are **unique**.
- The given graph is a directed acyclic graph.

## Examples
### Example 1
- **Input:** `n = 4, relations = [[2,1],[3,1],[1,4]], k = 2`
- **Output:** `3`
- **Explanation:** The figure above represents the given graph.
In the first semester, you can take courses 2 and 3.
In the second semester, you can take course 1.
In the third semester, you can take course 4.

### Example 2
- **Input:** `n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2`
- **Output:** `4`
- **Explanation:** The figure above represents the given graph.
In the first semester, you can only take courses 2 and 3 since you cannot take more than two per semester.
In the second semester, you can take course 4.
In the third semester, you can take course 1.
In the fourth semester, you can take course 5.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Parallel Courses II**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, relations = [[2,1],[3,1],[1,4]], k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The figure above represents the given graph.
In the first semester, you can take courses 2 and 3.
In the second semester, you can take course 1.
In the third semester, you can take course 4.

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
/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number} k
 * @return {number}
 */
var minNumberOfSemesters = function (n, relations, k) {
  const pre = new Array(n).fill(0);
  for (const [a, b] of relations) pre[b - 1] |= 1 << (a - 1);

  const popcount = (x) => {
    let c = 0;
    for (; x; x &= x - 1) c++;
    return c;
  };

  const full = (1 << n) - 1;
  const dp = new Array(1 << n).fill(Infinity);
  dp[0] = 0;

  for (let mask = 0; mask < full; mask++) {
    if (dp[mask] === Infinity) continue;

    let avail = 0;
    for (let i = 0; i < n; i++) {
      if (!(mask & (1 << i)) && (pre[i] & mask) === pre[i]) avail |= 1 << i;
    }

    if (popcount(avail) <= k) {
      const nm = mask | avail;
      dp[nm] = Math.min(dp[nm], dp[mask] + 1);
    } else {
      for (let sub = avail; sub > 0; sub = (sub - 1) & avail) {
        if (popcount(sub) !== k) continue;
        const nm = mask | sub;
        dp[nm] = Math.min(dp[nm], dp[mask] + 1);
      }
    }
  }

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
- [2050. Parallel Courses III](../../2001-2500/2050-parallel-courses-iii/)
- [2721. Execute Asynchronous Functions in Parallel](../../2501-3000/2721-execute-asynchronous-functions-in-parallel/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/parallel-courses-ii/)
