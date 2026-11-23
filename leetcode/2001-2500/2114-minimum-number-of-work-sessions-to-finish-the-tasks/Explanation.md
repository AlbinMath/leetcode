# LeetCode 1986: Minimum Number of Work Sessions to Finish the Tasks

**LeetCode Problem #1986 — Minimum Number of Work Sessions to Finish the Tasks**
Solve LeetCode Minimum Number of Work Sessions to Finish the Tasks using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Work Sessions to Finish the Tasks |
| LeetCode | #1986 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` tasks assigned to you. The task times are represented as an integer array `tasks` of length `n`, where the `i^th` task takes `tasks[i]` hours to finish. A **work session** is when you work for **at most** `sessionTime` consecutive hours and then take a break.

You should finish the given tasks in a way that satisfies the following conditions:

If you start a task in a work session, you must complete it in the **same** work session. 
 You can start a new task **immediately** after finishing the previous one. 
 You may complete the tasks in **any order**.

Given `tasks` and `sessionTime`, return *the **minimum** number of **work sessions** needed to finish all the tasks following the conditions above.*

The tests are generated such that `sessionTime` is **greater** than or **equal** to the **maximum** element in `tasks[i]`.

## Constraints
- `n == tasks.length`
- `1 <= n <= 14`
- `1 <= tasks[i] <= 10`
- `max(tasks[i]) <= sessionTime <= 15`

## Examples
### Example 1
- **Input:** `tasks = [1,2,3], sessionTime = 3`
- **Output:** `2`
- **Explanation:** You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.

### Example 2
- **Input:** `tasks = [3,1,3,1,1], sessionTime = 8`
- **Output:** `2`
- **Explanation:** You can finish the tasks in two work sessions.
- First work session: finish all the tasks except the last one in 3 + 1 + 3 + 1 = 8 hours.
- Second work session: finish the last task in 1 hour.

### Example 3
- **Input:** `tasks = [1,2,3,4,5], sessionTime = 15`
- **Output:** `1`
- **Explanation:** You can finish all the tasks in one work session.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Number of Work Sessions to Finish the Tasks**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tasks = [1,2,3], sessionTime = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.

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
 * @param {number[]} tasks
 * @param {number} sessionTime
 * @return {number}
 */
var minSessions = function(tasks, sessionTime) {
    const n = tasks.length;
    const totalMasks = 1 << n;

    // dp[mask] = [number of sessions, time used in last session]
    const dp = Array.from(
        { length: totalMasks },
        () => [Infinity, Infinity]
    );

    dp[0] = [0, 0];

    for (let mask = 0; mask < totalMasks; mask++) {
        const [sessions, used] = dp[mask];

        if (sessions === Infinity) continue;

        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;

            const nextMask = mask | (1 << i);
            let nextSessions;
            let nextUsed;

            if (sessions === 0) {
                nextSessions = 1;
                nextUsed = tasks[i];
            } else if (used + tasks[i] <= sessionTime) {
                nextSessions = sessions;
                nextUsed = used + tasks[i];
            } else {
                nextSessions = sessions + 1;
                nextUsed = tasks[i];
            }

            const [oldSessions, oldUsed] = dp[nextMask];

            if (
                nextSessions < oldSessions ||
                (nextSessions === oldSessions && nextUsed < oldUsed)
            ) {
                dp[nextMask] = [nextSessions, nextUsed];
            }
        }
    }

    return dp[totalMasks - 1][0];
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
- [1665. Minimum Initial Energy to Finish Tasks](../../1501-2000/1784-minimum-initial-energy-to-finish-tasks/)
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [995. Minimum Number of K Consecutive Bit Flips](../../1001-1500/1037-minimum-number-of-k-consecutive-bit-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/)
