# LeetCode 1723: Find Minimum Time to Finish All Jobs

**LeetCode Problem #1723 — Find Minimum Time to Finish All Jobs**
Solve LeetCode Find Minimum Time to Finish All Jobs using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Minimum Time to Finish All Jobs |
| LeetCode | #1723 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `jobs`, where `jobs[i]` is the amount of time it takes to complete the `i^th` job.

There are `k` workers that you can assign jobs to. Each job should be assigned to **exactly** one worker. The **working time** of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the **maximum working time** of any worker is **minimized**.

*Return the **minimum** possible **maximum working time** of any assignment. *

## Constraints
- `1 <= k <= jobs.length <= 12`
- `1 <= jobs[i] <= 10^7`

## Examples
### Example 1
- **Input:** `jobs = [3,2,3], k = 3`
- **Output:** `3`
- **Explanation:** By assigning each person one job, the maximum time is 3.

### Example 2
- **Input:** `jobs = [1,2,4,7,8], k = 2`
- **Output:** `11`
- **Explanation:** Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Find Minimum Time to Finish All Jobs**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `jobs = [3,2,3], k = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** By assigning each person one job, the maximum time is 3.

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
 * @param {number[]} jobs
 * @param {number} k
 * @return {number}
 */
var minimumTimeRequired = function(jobs, k) {
    const n = jobs.length;
    const totalMasks = 1 << n;

    // sum[mask] = total time for the jobs selected by mask.
    const sum = new Array(totalMasks).fill(0);

    for (let mask = 1; mask < totalMasks; mask++) {
        const bit = mask & -mask;
        const index = Math.log2(bit);

        sum[mask] = sum[mask ^ bit] + jobs[index];
    }

    // dp[w][mask] = minimum possible maximum workload
    // when assigning jobs in mask to w workers.
    const dp = Array.from(
        { length: k + 1 },
        () => new Array(totalMasks).fill(Infinity)
    );

    dp[0][0] = 0;

    for (let w = 1; w <= k; w++) {
        for (let mask = 0; mask < totalMasks; mask++) {
            // The last worker must receive a non-empty subset
            // of the jobs represented by mask.
            for (
                let sub = mask;
                sub > 0;
                sub = (sub - 1) & mask
            ) {
                const remaining = mask ^ sub;

                if (dp[w - 1][remaining] === Infinity) {
                    continue;
                }

                dp[w][mask] = Math.min(
                    dp[w][mask],
                    Math.max(
                        dp[w - 1][remaining],
                        sum[sub]
                    )
                );
            }
        }
    }

    return dp[k][totalMasks - 1];
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
- [3197. Find the Minimum Area to Cover All Ones II](../../3001-3500/3197-find-the-minimum-area-to-cover-all-ones-ii/)
- [3341. Find Minimum Time to Reach Last Room I](../../3001-3500/3341-find-minimum-time-to-reach-last-room-i/)
- [3342. Find Minimum Time to Reach Last Room II](../../3001-3500/3342-find-minimum-time-to-reach-last-room-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/)
