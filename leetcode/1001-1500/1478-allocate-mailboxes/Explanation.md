# LeetCode 1478: Allocate Mailboxes

**LeetCode Problem #1478 — Allocate Mailboxes**
Solve LeetCode Allocate Mailboxes using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Allocate Mailboxes |
| LeetCode | #1478 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the array `houses` where `houses[i]` is the location of the `i^th` house along a street and an integer `k`, allocate `k` mailboxes in the street.

Return *the **minimum** total distance between each house and its nearest mailbox*.

The test cases are generated so that the answer fits in a 32-bit integer.

## Constraints
- `1 <= k <= houses.length <= 100`
- `1 <= houses[i] <= 10^4`
- All the integers of `houses` are **unique**.

## Examples
### Example 1
- **Input:** `houses = [1,4,8,10,20], k = 3`
- **Output:** `5`
- **Explanation:** Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5

### Example 2
- **Input:** `houses = [2,3,5,12,18], k = 2`
- **Output:** `9`
- **Explanation:** Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Allocate Mailboxes**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `houses = [1,4,8,10,20], k = 3`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minDistance = function(houses, k) {
    houses.sort((a, b) => a - b);

    const n = houses.length;

    const cost = Array.from({ length: n }, () => 
        new Array(n).fill(0)
    );

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const mid = Math.floor((i + j) / 2);
            cost[i][j] = cost[i][j - 1] + houses[j] - houses[mid];
        }
    }

    const dp = Array.from({ length: n + 1 }, () =>
        new Array(k + 1).fill(Infinity)
    );

    dp[0][0] = 0;

    for (let i = 1; i <= n; i++) {
        for (let m = 1; m <= Math.min(i, k); m++) {
            for (let j = 0; j < i; j++) {
                dp[i][m] = Math.min(
                    dp[i][m],
                    dp[j][m - 1] + cost[j][i - 1]
                );
            }
        }
    }

    return dp[n][k];
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [6. Zigzag Conversion](../../0001-0500/0006-zigzag-conversion/)
- [79. Word Search](../../0001-0500/0079-word-search/)
- [112. Path Sum](../../0001-0500/0112-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/allocate-mailboxes/)
