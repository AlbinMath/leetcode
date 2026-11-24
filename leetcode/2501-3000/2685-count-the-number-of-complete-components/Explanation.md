# LeetCode 2685: Count the Number of Complete Components

**LeetCode Problem #2685 — Count the Number of Complete Components**
Solve LeetCode Count the Number of Complete Components using Java, Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Complete Components |
| LeetCode | #2685 |
| Difficulty | Medium |
| Language | Java, Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`. There is an **undirected** graph with `n` vertices, numbered from `0` to `n - 1`. You are given a 2D integer array `edges` where `edges[i] = [a_i, b_i]` denotes that there exists an **undirected** edge connecting vertices `a_i` and `b_i`.

Return *the number of **complete connected components** of the graph*.

A **connected component** is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

## Constraints
- `1 <= n <= 50`
- `0 <= edges.length <= n * (n - 1) / 2`
- `edges[i].length == 2`
- `0 <= a_i, b_i <= n - 1`
- `a_i != b_i`
- There are no repeated edges.

## Examples
### Example 1
- **Input:** `n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]`
- **Output:** `3`
- **Explanation:** From the picture above, one can see that all of the components of this graph are complete.

### Example 2
- **Input:** `n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]`
- **Output:** `1`
- **Explanation:** The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Use **BFS/DFS or Union-Find** to find connected components. For each component with `v` vertices and `e` edges, it's complete if `e == v*(v-1)/2`.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** From the picture above, one can see that all of the components of this graph are complete.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Java, Python

## Source Code
- [solution.java](./solution.java)
- [solution.py](./solution.py)


### Java
```java
import java.util.*;

class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        List<Integer>[] graph = new ArrayList[n];

        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        boolean[] visited = new boolean[n];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }

            int vertices = 0;
            int edgeCount = 0;

            Queue<Integer> queue = new LinkedList<>();
            queue.offer(i);
            visited[i] = true;

            while (!queue.isEmpty()) {
                int node = queue.poll();
                vertices++;
                edgeCount += graph[node].size();

                for (int next : graph[node]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        queue.offer(next);
                    }
                }
            }

            // Every pair of vertices must have an edge.
            // A complete graph with k vertices has k*(k-1)/2 edges.
            edgeCount /= 2;

            if (edgeCount == vertices * (vertices - 1) / 2) {
                answer++;
            }
        }

        return answer;
    }
}
```

### Python
```python
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        seen = set()
        ans = 0

        for i in range(n):
            if i in seen:
                continue

            stack = [i]
            seen.add(i)
            nodes = []

            while stack:
                u = stack.pop()
                nodes.append(u)
                for v in g[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)

            if all(len(g[u]) == len(nodes) - 1 for u in nodes):
                ans += 1

        return ans
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
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)
- [2799. Count Complete Subarrays in an Array](../../2501-3000/2799-count-complete-subarrays-in-an-array/)
- [2953. Count Complete Substrings](../../2501-3000/2953-count-complete-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-complete-components/)
