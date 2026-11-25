# LeetCode 3425: Longest Special Path

**LeetCode Problem #3425 — Longest Special Path**
Solve LeetCode Longest Special Path using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Special Path |
| LeetCode | #3425 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an undirected tree rooted at node `0` with `n` nodes numbered from `0` to `n - 1`, represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, length_i]` indicates an edge between nodes `u_i` and `v_i` with length `length_i`. You are also given an integer array `nums`, where `nums[i]` represents the value at node `i`.

A special path is defined as a downward path from an ancestor node to a descendant node such that all the values of the nodes in that path are unique .

**Note** that a path may start and end at the same node.

Return an array result of size 2, where `result[0]` is the length of the **longest** special path, and `result[1]` is the minimum number of nodes in all possible **longest** special paths.

## Constraints
- `2 <= n <= 5 * 10^ 4 `
- `edges.length == n - 1`
- `edges[i].length == 3`
- `0 <= u_i, v_i < n`
- `1 <= length_i <= 10^3`
- `nums.length == n`
- `0 <= nums[i] <= 5 * 10^4`
- The input is generated such that `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], nums = [2,1,2,1,3,1]`
- **Output:** `[6,2]`
- **Explanation:** In the image below, nodes are colored by their corresponding values in `nums` 

 

 The longest special paths are `2 -> 5` and `0 -> 1 -> 4`, both having a length of 6. The minimum number of nodes across all longest special paths is 2.

### Example 2
- **Input:** `edges = [[1,0,8]], nums = [2,2]`
- **Output:** `[0,1]`
- **Explanation:** The longest special paths are `0` and `1`, both having a length of 0. The minimum number of nodes across all longest special paths is 1.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Special Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], nums = [2,1,2,1,3,1]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,2]`.
4. **Verification:** In the image below, nodes are colored by their corresponding values in `nums` 

 

 The longest special paths are `2 -> 5` and `0 -> 1 -> 4`, both having a length of 6. The minimum number of nodes across all longest special paths is 2.

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
var longestSpecialPath = function(edges, nums) {
    const n = nums.length;
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }
    const lastSeen = new Array(50001).fill(-1);
    const distAtDepth = new Array(n).fill(0);

    let bestLength = -1;
    let minNodes = Infinity;
    const stack = [{
        node: 0,
        parent: -1,
        depth: 0,
        dist: 0,
        left: 0,
        exit: false
    }];

    while (stack.length > 0) {
        const cur = stack.pop();

        const u = cur.node;
        const depth = cur.depth;

        if (cur.exit) {
            if (cur.previous === -1) {
                lastSeen[nums[u]] = -1;
            } else {
                lastSeen[nums[u]] = cur.previous;
            }
            continue;
        }

        const value = nums[u];
        const previous = lastSeen[value];
        let left = cur.left;

        if (previous !== -1) {
            left = Math.max(left, previous + 1);
        }
        lastSeen[value] = depth;
        distAtDepth[depth] = cur.dist;
        const length = cur.dist - distAtDepth[left];
        const nodes = depth - left + 1;

        if (length > bestLength) {
            bestLength = length;
            minNodes = nodes;
        } else if (length === bestLength) {
            minNodes = Math.min(minNodes, nodes);
        }
        stack.push({
            node: u,
            exit: true,
            previous: previous
        });
        for (const [v, w] of graph[u]) {
            if (v === cur.parent) continue;

            stack.push({
                node: v,
                parent: u,
                depth: depth + 1,
                dist: cur.dist + w,
                left: left,
                exit: false
            });
        }
    }

    return [bestLength, minNodes];
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
- [3486. Longest Special Path II](../../3001-3500/3486-longest-special-path-ii/)
- [2662. Minimum Cost of a Path With Special Roads](../../2501-3000/2662-minimum-cost-of-a-path-with-special-roads/)
- [2981. Find Longest Special Substring That Occurs Thrice I](../../2501-3000/2981-find-longest-special-substring-that-occurs-thrice-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-special-path/)
