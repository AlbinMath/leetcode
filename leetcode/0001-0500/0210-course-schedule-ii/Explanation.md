# LeetCode 210: Course Schedule II

**LeetCode Problem #210 — Course Schedule II**
Solve LeetCode Course Schedule II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Course Schedule II |
| LeetCode | #210 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return *the ordering of courses you should take to finish all courses*. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

## Constraints
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < numCourses`
- `a_i != b_i`
- All the pairs `[a_i, b_i]` are **distinct**.

## Examples
### Example 1
- **Input:** `numCourses = 2, prerequisites = [[1,0]]`
- **Output:** `[0,1]`
- **Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

### Example 2
- **Input:** `numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
- **Output:** `[0,2,1,3]`
- **Explanation:** There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

### Example 3
- **Input:** `numCourses = 1, prerequisites = []`
- **Output:** `[0]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Course Schedule II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numCourses = 2, prerequisites = [[1,0]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1]`.
4. **Verification:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

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
var findOrder = function(numCourses, prerequisites) {
    const graph = Array.from(
        { length: numCourses },
        () => []
    );

    const indegree = new Array(numCourses).fill(0);

    // Build the graph
    for (const [course, prerequisite] of prerequisites) {
        graph[prerequisite].push(course);
        indegree[course]++;
    }

    // Find courses with no prerequisites
    const queue = [];

    for (let i = 0; i < numCourses; i++) {
        if (indegree[i] === 0) {
            queue.push(i);
        }
    }

    const order = [];
    let front = 0;

    // Process courses in topological order
    while (front < queue.length) {
        const course = queue[front++];
        order.push(course);

        for (const nextCourse of graph[course]) {
            indegree[nextCourse]--;

            if (indegree[nextCourse] === 0) {
                queue.push(nextCourse);
            }
        }
    }

    // If a cycle exists, not all courses can be completed
    return order.length === numCourses ? order : [];
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
- [630. Course Schedule III](../../0501-1000/0630-course-schedule-iii/)
- [1462. Course Schedule IV](../../1001-1500/1462-course-schedule-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/course-schedule-ii/)
