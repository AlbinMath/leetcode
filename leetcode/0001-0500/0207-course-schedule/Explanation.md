# LeetCode 207: Course Schedule

**LeetCode Problem #207 — Course Schedule**
Solve LeetCode Course Schedule using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Course Schedule |
| LeetCode | #207 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

## Constraints
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < numCourses`
- All the pairs prerequisites[i] are **unique**.

## Examples
### Example 1
- **Input:** `numCourses = 2, prerequisites = [[1,0]]`
- **Output:** `true`
- **Explanation:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

### Example 2
- **Input:** `numCourses = 2, prerequisites = [[1,0],[0,1]]`
- **Output:** `false`
- **Explanation:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Course Schedule**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numCourses = 2, prerequisites = [[1,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var canFinish = function(numCourses, prerequisites) {
    const graph = Array.from(
        { length: numCourses },
        () => []
    );

    const indegree = new Array(numCourses).fill(0);

    // Build the graph and count prerequisites
    for (const [course, prerequisite] of prerequisites) {
        graph[prerequisite].push(course);
        indegree[course]++;
    }

    // Start with courses that have no prerequisites
    const queue = [];

    for (let i = 0; i < numCourses; i++) {
        if (indegree[i] === 0) {
            queue.push(i);
        }
    }

    let completed = 0;
    let front = 0;

    while (front < queue.length) {
        const course = queue[front++];
        completed++;

        // Remove this course as a prerequisite
        for (const nextCourse of graph[course]) {
            indegree[nextCourse]--;

            if (indegree[nextCourse] === 0) {
                queue.push(nextCourse);
            }
        }
    }

    // All courses must be completed
    return completed === numCourses;
};
```

### Python
```python
from collections import deque
from typing import List

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build the graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Start with courses having no prerequisites
        queue = deque(
            course for course in range(numCourses)
            if indegree[course] == 0
        )

        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            # Remove this course's dependency from its neighbors
            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses
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
- [210. Course Schedule II](../../0001-0500/0210-course-schedule-ii/)
- [630. Course Schedule III](../../0501-1000/0630-course-schedule-iii/)
- [1462. Course Schedule IV](../../1001-1500/1462-course-schedule-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/course-schedule/)
