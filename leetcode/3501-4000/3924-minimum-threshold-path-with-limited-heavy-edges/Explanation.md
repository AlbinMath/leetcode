# LeetCode 3924: Minimum Threshold Path With Limited Heavy Edges

**LeetCode Problem #3924 — Minimum Threshold Path With Limited Heavy Edges**
Solve LeetCode Minimum Threshold Path With Limited Heavy Edges using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Threshold Path With Limited Heavy Edges |
| LeetCode | #3924 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an undirected weighted graph with `n` nodes labeled from 0 to `n - 1`.

The graph is represented by a 2D integer array `edges`, where each edge `edges[i] = [u_i, v_i, w_​​​​​​​i]` indicates that there is an undirected edge between nodes `u_i` and `v_i` with weight `w_​​​​​​​i`.

You are also given integers `source`, `target` and `k`.

A `threshold` value determines whether an edge is considered **light** or **heavy**:

An edge is **light** if its weight is **less than** or **equal** to `threshold`.

An edge is **heavy** if its weight is **greater than** `threshold`.

A path from `source` to `target` is **valid** if it contains **at most** `k` heavy edges.

Return the **minimum integer **`threshold` such that **at least** one **valid** path exists from `source` to `target`. If no such path exists, return -1.

## Constraints
- `1 <= n <= 10^3​​​​​​​`
- `0 <= edges.length <= 10^3​​​​​​​`
- `edges[i] = [u_i, v_i, w_i]`
- `0 <= u_i, v_i​​​​​​​ <= n - 1`
- `1 <= w_i​​​​​​​ <= 10^9`
- `0 <= source, target <= n - 1`
- `0 <= k <= edges.length`

## Examples
### Example 1
- **Input:** `n = 6, edges = [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], source = 0, target = 3, k = 1`
- **Output:** `4`
- **Explanation:** The minimum `threshold` such that a path from node 0 to node 3 uses at most 1 heavy edge is 4. 

 
 
 Light edges: `[1, 2, 3]`, `[3, 4, 4]`, `[4, 5, 1]`, `[1, 4, 2]` 
 
 
 Heavy edges: `[0, 1, 5]` 
 
 

 A valid path is `0 &rarr; 1 &rarr; 4 &rarr; 3`. It uses only 1 heavy edge (`[0, 1, 5]`), which satisfies the limit `k = 1`. 

 Any smaller `threshold` would make it impossible to reach node 3 without exceeding 1 heavy edge.

### Example 2
- **Input:** `n = 6, edges = [[0,1,3],[1,2,4],[3,4,5],[4,5,6]], source = 0, target = 4, k = 1`
- **Output:** `-1`
- **Explanation:** There is no path from node 0 to node 4. Since the target cannot be reached, the output is -1.

### Example 3
- **Input:** `n = 4, edges = [[0,1,2],[1,2,2],[2,3,2],[3,0,2]], source = 0, target = 0, k = 0`
- **Output:** `0`
- **Explanation:** The source and target are the same node. No edges need to be traversed, so the minimum `threshold` is 0.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Minimum Threshold Path With Limited Heavy Edges**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, edges = [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], source = 0, target = 3, k = 1`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The minimum `threshold` such that a path from node 0 to node 3 uses at most 1 heavy edge is 4. 

 
 
 Light edges: `[1, 2, 3]`, `[3, 4, 4]`, `[4, 5, 1]`, `[1, 4, 2]` 
 
 
 Heavy edges: `[0, 1, 5]` 
 
 

 A valid path is `0 &rarr; 1 &rarr; 4 &rarr; 3`. It uses only 1 heavy edge (`[0, 1, 5]`), which satisfies the limit `k = 1`. 

 Any smaller `threshold` would make it impossible to reach node 3 without exceeding 1 heavy edge.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minimumThreshold = function(n, edges, source, target, k) {
    if (source === target) return 0;

    // Build adjacency list
    const graph = Array.from({ length: n }, () => []);
    let maxWeight = 0;

    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);

        maxWeight = Math.max(maxWeight, w);
    }

    // Check if target can be reached using at most k heavy edges
    function canReach(threshold) {
        const dist = new Array(n).fill(Infinity);
        const visited = new Array(n).fill(false);

        dist[source] = 0;

        // Dijkstra: minimize the number of heavy edges
        for (let i = 0; i < n; i++) {
            let u = -1;

            for (let j = 0; j < n; j++) {
                if (
                    !visited[j] &&
                    (u === -1 || dist[j] < dist[u])
                ) {
                    u = j;
                }
            }

            if (u === -1 || dist[u] === Infinity) {
                break;
            }

            if (u === target) {
                return dist[u] <= k;
            }

            visited[u] = true;

            for (const [v, w] of graph[u]) {
                if (visited[v]) continue;

                const cost = w > threshold ? 1 : 0;
                const newDist = dist[u] + cost;

                if (newDist < dist[v]) {
                    dist[v] = newDist;
                }
            }
        }

        return dist[target] <= k;
    }

    // Check whether a path exists at the maximum threshold
    if (!canReach(maxWeight)) {
        return -1;
    }

    // Binary search from 0 to maximum edge weight
    let left = 0;
    let right = maxWeight;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (canReach(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3977. Minimum Time to Reach Target With Limited Power](../../3501-4000/3977-minimum-time-to-reach-target-with-limited-power/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [931. Minimum Falling Path Sum](../../0501-1000/0931-minimum-falling-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/)
