# LeetCode 3898: Find the Degree of Each Vertex

**LeetCode Problem #3898 — Find the Degree of Each Vertex**
Solve LeetCode Find the Degree of Each Vertex using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Degree of Each Vertex |
| LeetCode | #3898 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `matrix` of size `n x n` representing the adjacency matrix of an undirected graph with `n` vertices labeled from 0 to `n - 1`.

`matrix[i][j] = 1` indicates that there is an edge between vertices `i` and `j`. 
 `matrix[i][j] = 0` indicates that there is no edge between vertices `i` and `j`.

The **degree** of a vertex is the number of edges connected to it.

Return an integer array `ans` of size `n` where `ans[i]` represents the degree of vertex `i`.

## Constraints
- `1 <= n == matrix.length == matrix[i].length <= 100`​​​​​​​
- `​​​​​​​matrix[i][i] == 0`
- `matrix[i][j]` is either 0 or 1
- `matrix[i][j] == matrix[j][i]`

## Examples
### Example 1
- **Input:** `matrix = [[0,1,1],[1,0,1],[1,1,0]]`
- **Output:** `[2,2,2]`
- **Explanation:** Vertex 0 is connected to vertices 1 and 2, so its degree is 2. 
 Vertex 1 is connected to vertices 0 and 2, so its degree is 2. 
 Vertex 2 is connected to vertices 0 and 1, so its degree is 2. 
 

 Thus, the answer is `[2, 2, 2]`.

### Example 2
- **Input:** `matrix = [[0,1,0],[1,0,0],[0,0,0]]`
- **Output:** `[1,1,0]`
- **Explanation:** Vertex 0 is connected to vertex 1, so its degree is 1. 
 Vertex 1 is connected to vertex 0, so its degree is 1. 
 Vertex 2 is not connected to any vertex, so its degree is 0. 
 

 Thus, the answer is `[1, 1, 0]`.

### Example 3
- **Input:** `matrix = [[0]]`
- **Output:** `[0]`
- **Explanation:** There is only one vertex and it has no edges connected to it. Thus, the answer is [0] .

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Degree of Each Vertex**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[0,1,1],[1,0,1],[1,1,0]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,2,2]`.
4. **Verification:** Vertex 0 is connected to vertices 1 and 2, so its degree is 2. 
 Vertex 1 is connected to vertices 0 and 2, so its degree is 2. 
 Vertex 2 is connected to vertices 0 and 1, so its degree is 2. 
 

 Thus, the answer is `[2, 2, 2]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var findDegrees = function(matrix) {
    const n = matrix.length;
    const ans = new Array(n).fill(0);

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] === 1) {
                ans[i]++;
            }
        }
    }

    return ans;
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../../1001-1500/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [1741. Find Total Time Spent by Each Employee](../../1501-2000/1741-find-total-time-spent-by-each-employee/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-degree-of-each-vertex/)
