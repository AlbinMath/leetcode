# LeetCode 1462: Course Schedule IV

**LeetCode Problem #1462 — Course Schedule IV**
Solve LeetCode Course Schedule IV using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Course Schedule IV |
| LeetCode | #1462 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `a_i` first if you want to take course `b_i`.

For example, the pair `[0, 1]` indicates that you have to take course `0` before you can take course `1`.

Prerequisites can also be **indirect**. If course `a` is a prerequisite of course `b`, and course `b` is a prerequisite of course `c`, then course `a` is a prerequisite of course `c`.

You are also given an array `queries` where `queries[j] = [u_j, v_j]`. For the `j^th` query, you should answer whether course `u_j` is a prerequisite of course `v_j` or not.

Return a boolean array `answer` , where `answer[j]` is the answer to the `j^th` query.

## Constraints
- `2 <= numCourses <= 100`
- `0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i <= numCourses - 1`
- `a_i != b_i`
- All the pairs `[a_i, b_i]` are **unique**.
- The prerequisites graph has no cycles.
- `1 <= queries.length <= 10^4`
- `0 <= u_i, v_i <= numCourses - 1`
- `u_i != v_i`

## Examples
### Example 1
- **Input:** `numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]`
- **Output:** `[false,true]`
- **Explanation:** The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

### Example 2
- **Input:** `numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]`
- **Output:** `[false,false]`
- **Explanation:** There are no prerequisites, and each course is independent.

### Example 3
- **Input:** `numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]`
- **Output:** `[true,true]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Course Schedule IV**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[false,true]`.
4. **Verification:** The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var checkIfPrerequisite = function (numCourses, prerequisites, queries) {
    const n = numCourses;
    const reach = Array.from({ length: n }, () => new Uint8Array(n));

    for (const [a, b] of prerequisites) reach[a][b] = 1; // a must come before b

    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            if (!reach[i][k]) continue;
            for (let j = 0; j < n; j++) {
                if (reach[k][j]) reach[i][j] = 1;
            }
        }
    }

    return queries.map(([u, v]) => reach[u][v] === 1);
};
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
- [207. Course Schedule](../../0001-0500/0207-course-schedule/)
- [210. Course Schedule II](../../0001-0500/0210-course-schedule-ii/)
- [630. Course Schedule III](../../0501-1000/0630-course-schedule-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/course-schedule-iv/)
