# LeetCode 3243: Shortest Distance After Road Addition Queries I

**LeetCode Problem #3243 — Shortest Distance After Road Addition Queries I**
Solve LeetCode Shortest Distance After Road Addition Queries I using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Distance After Road Addition Queries I |
| LeetCode | #3243 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` and a 2D integer array `queries`.

There are `n` cities numbered from `0` to `n - 1`. Initially, there is a **unidirectional** road from city `i` to city `i + 1` for all `0 <= i < n - 1`.

`queries[i] = [u_i, v_i]` represents the addition of a new **unidirectional** road from city `u_i` to city `v_i`. After each query, you need to find the **length** of the **shortest path** from city `0` to city `n - 1`.

Return an array `answer` where for each `i` in the range `[0, queries.length - 1]`, `answer[i]` is the *length of the shortest path* from city `0` to city `n - 1` after processing the **first **`i + 1` queries.

## Constraints
- `3 <= n <= 500`
- `1 <= queries.length <= 500`
- `queries[i].length == 2`
- `0 <= queries[i][0] < queries[i][1] < n`
- `1 < queries[i][1] - queries[i][0]`
- There are no repeated roads among the queries.

## Examples
### Example 1
- **Input:** `n = 5, queries = [[2,4],[0,2],[0,4]]`
- **Output:** `[3,2,1]`
- **Explanation:** After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3. 

 

 After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2. 

 

 After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

### Example 2
- **Input:** `n = 4, queries = [[0,3],[0,2]]`
- **Output:** `[1,1]`
- **Explanation:** After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1. 

 

 After the addition of the road from 0 to 2, the length of the shortest path remains 1.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shortest Distance After Road Addition Queries I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, queries = [[2,4],[0,2],[0,4]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2,1]`.
4. **Verification:** After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3. 

 

 After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2. 

 

 After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

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
var shortestDistanceAfterQueries = function(n, queries) {
    const graph = Array.from({ length: n }, () => []);

    // Add the original roads.
    for (let i = 0; i < n - 1; i++) {
        graph[i].push(i + 1);
    }

    const answer = [];

    for (const [u, v] of queries) {
        // Add the new directed road.
        graph[u].push(v);

        // BFS to find shortest distance from 0 to n - 1.
        const dist = new Array(n).fill(-1);
        const queue = [0];

        dist[0] = 0;
        let head = 0;

        while (head < queue.length) {
            const curr = queue[head++];

            if (curr === n - 1) break;

            for (const next of graph[curr]) {
                if (dist[next] === -1) {
                    dist[next] = dist[curr] + 1;
                    queue.push(next);
                }
            }
        }

        answer.push(dist[n - 1]);
    }

    return answer;
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
- [3244. Shortest Distance After Road Addition Queries II](../../3501-4000/3514-shortest-distance-after-road-addition-queries-ii/)
- [821. Shortest Distance to a Character](../../0501-1000/0841-shortest-distance-to-a-character/)
- [985. Sum of Even Numbers After Queries](../../1001-1500/1027-sum-of-even-numbers-after-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/)
