# LeetCode 2492: Minimum Score of a Path Between Two Cities

**LeetCode Problem #2492 — Minimum Score of a Path Between Two Cities**
Solve LeetCode Minimum Score of a Path Between Two Cities using Java, Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Score of a Path Between Two Cities |
| LeetCode | #2492 |
| Difficulty | Medium |
| Language | Java, Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a **2D** array `roads` where `roads[i] = [a_i, b_i, distance_i]` indicates that there is a **bidirectional **road between cities `a_i` and `b_i` with a distance equal to `distance_i`. The cities graph is not necessarily connected.

The **score** of a path between two cities is defined as the **minimum **distance of a road in this path.

Return the **minimum **possible score of a path between cities 1 and `n`.

**Note**:

A path is a sequence of roads between two cities. 
 It is allowed for a path to contain the same road **multiple** times, and you can visit cities 1 and `n` multiple times along the path. 
 The test cases are generated such that there is **at least** one path between 1 and `n`.

## Constraints
- `2 <= n <= 10^5`
- `1 <= roads.length <= 10^5`
- `roads[i].length == 3`
- `1 <= a_i, b_i <= n`
- `a_i != b_i`
- `1 <= distance_i <= 10^4`
- There are no repeated edges.
- There is at least one path between `1` and `n`.

## Examples
### Example 1
- **Input:** `n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]`
- **Output:** `5`
- **Explanation:** The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

### Example 2
- **Input:** `n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]`
- **Output:** `2`
- **Explanation:** The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Since you can traverse any edge multiple times, the answer is the minimum edge weight in the connected component containing cities 1 and n. Use **BFS/DFS** or **Union-Find** to find all reachable nodes from city 1 and track the minimum edge weight.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

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
Java, Python

## Source Code
- [solution.java](./solution.java)
- [solution.py](./solution.py)


### Java
```java
import java.util.*;

class Solution {
    public int minScore(int n, int[][] roads) {
        List<int[]>[] graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] road : roads) {
            int u = road[0];
            int v = road[1];
            int d = road[2];

            graph[u].add(new int[]{v, d});
            graph[v].add(new int[]{u, d});
        }

        boolean[] visited = new boolean[n + 1];
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(1);
        visited[1] = true;

        int answer = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            int city = queue.poll();

            for (int[] edge : graph[city]) {
                int next = edge[0];
                int distance = edge[1];

                // Every edge in this component can affect the answer
                answer = Math.min(answer, distance);

                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(next);
                }
            }
        }

        return answer;
    }
}
```

### Python
```python
from typing import List
from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]

        for u, v, d in roads:
            g[u].append((v, d))
            g[v].append((u, d))

        ans = float('inf')
        seen = {1}
        q = deque([1])

        while q:
            u = q.popleft()
            for v, d in g[u]:
                ans = min(ans, d)
                if v not in seen:
                    seen.add(v)
                    q.append(v)

        return ans
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
- [2567. Minimum Score by Changing Two Elements](../../2501-3000/2567-minimum-score-by-changing-two-elements/)
- [3880. Minimum Absolute Difference Between Two Values](../../3501-4000/3880-minimum-absolute-difference-between-two-values/)
- [1617. Count Subtrees With Max Distance Between Cities](../../1501-2000/1617-count-subtrees-with-max-distance-between-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)
