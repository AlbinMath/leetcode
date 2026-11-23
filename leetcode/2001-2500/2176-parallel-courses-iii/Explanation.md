# LeetCode 2050: Parallel Courses III

**LeetCode Problem #2050 — Parallel Courses III**
Solve LeetCode Parallel Courses III using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Parallel Courses III |
| LeetCode | #2050 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given a 2D integer array `relations` where `relations[j] = [prevCourse_j, nextCourse_j]` denotes that course `prevCourse_j` has to be completed **before** course `nextCourse_j` (prerequisite relationship). Furthermore, you are given a **0-indexed** integer array `time` where `time[i]` denotes how many **months** it takes to complete the `(i+1)^th` course.

You must find the **minimum** number of months needed to complete all the courses following these rules:

You may start taking a course at **any time** if the prerequisites are met. 
 **Any number of courses** can be taken at the **same time**.

Return *the **minimum** number of months needed to complete all the courses*.

**Note:** The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).

## Constraints
- `1 <= n <= 5 * 10^4`
- `0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)`
- `relations[j].length == 2`
- `1 <= prevCourse_j, nextCourse_j <= n`
- `prevCourse_j != nextCourse_j`
- All the pairs `[prevCourse_j, nextCourse_j]` are **unique**.
- `time.length == n`
- `1 <= time[i] <= 10^4`
- The given graph is a directed acyclic graph.

## Examples
### Example 1
- **Input:** `n = 3, relations = [[1,3],[2,3]], time = [3,2,5]`
- **Output:** `8`
- **Explanation:** The figure above represents the given graph and the time required to complete each course. 
We start course 1 and course 2 simultaneously at month 0.
Course 1 takes 3 months and course 2 takes 2 months to complete respectively.
Thus, the earliest time we can start course 3 is at month 3, and the total time required is 3 + 5 = 8 months.

### Example 2
- **Input:** `n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]`
- **Output:** `12`
- **Explanation:** The figure above represents the given graph and the time required to complete each course.
You can start courses 1, 2, and 3 at month 0.
You can complete them after 1, 2, and 3 months respectively.
Course 4 can be taken only after course 3 is completed, i.e., after 3 months. It is completed after 3 + 4 = 7 months.
Course 5 can be taken only after courses 1, 2, 3, and 4 have been completed, i.e., after max(1,2,3,7) = 7 months.
Thus, the minimum time needed to complete all the courses is 7 + 5 = 12 months.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Parallel Courses III**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, relations = [[1,3],[2,3]], time = [3,2,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The figure above represents the given graph and the time required to complete each course. 
We start course 1 and course 2 simultaneously at month 0.
Course 1 takes 3 months and course 2 takes 2 months to complete respectively.
Thus, the earliest time we can start course 3 is at month 3, and the total time required is 3 + 5 = 8 months.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number[]} time
 * @return {number}
 */
var minimumTime = function (n, relations, time) {
    const adj = Array.from({ length: n }, () => []);
    const indeg = new Int32Array(n);
    for (const [a, b] of relations) {
        adj[a - 1].push(b - 1);
        indeg[b - 1]++;
    }

    const start = new Int32Array(n);
    const queue = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) queue.push(i);

    let head = 0, ans = 0;
    while (head < queue.length) {
        const u = queue[head++];
        const fin = start[u] + time[u];
        if (fin > ans) ans = fin;
        for (const v of adj[u]) {
            if (fin > start[v]) start[v] = fin;
            if (--indeg[v] === 0) queue.push(v);
        }
    }
    return ans;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1494. Parallel Courses II](../../1501-2000/1587-parallel-courses-ii/)
- [2721. Execute Asynchronous Functions in Parallel](../../2501-3000/2807-execute-asynchronous-functions-in-parallel/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/parallel-courses-iii/)
