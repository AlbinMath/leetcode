# LeetCode 3604: Minimum Time to Reach Destination in Directed Graph

**LeetCode Problem #3604 — Minimum Time to Reach Destination in Directed Graph**
Solve LeetCode Minimum Time to Reach Destination in Directed Graph using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Reach Destination in Directed Graph |
| LeetCode | #3604 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and a **directed** graph with `n` nodes labeled from 0 to `n - 1`. This is represented by a 2D array `edges`, where `edges[i] = [u_i, v_i, start_i, end_i]` indicates an edge from node `u_i` to `v_i` that can **only** be used at any integer time `t` such that `start_i <= t <= end_i`.

You start at node 0 at time 0.

In one unit of time, you can either:

Wait at your current node without moving, or 
 Travel along an outgoing edge from your current node if the current time `t` satisfies `start_i <= t <= end_i`.

Return the **minimum** time required to reach node `n - 1`. If it is impossible, return `-1`.

## Constraints
- `1 <= n <= 10^5`
- `0 <= edges.length <= 10^5`
- `edges[i] == [u_i, v_i, start_i, end_i]`
- `0 <= u_i, v_i <= n - 1`
- `u_i != v_i`
- `0 <= start_i <= end_i <= 10^9`

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1,0,1],[1,2,2,5]]`
- **Output:** `3`
- **Explanation:** The optimal path is: 

 
 At time `t = 0`, take the edge `(0 &rarr; 1)` which is available from 0 to 1. You arrive at node 1 at time `t = 1`, then wait until `t = 2`. 
 At time `t = 2` , take the edge `(1 &rarr; 2)` which is available from 2 to 5. You arrive at node 2 at time 3. 
 

 Hence, the minimum time to reach node 2 is 3.

### Example 2
- **Input:** `n = 4, edges = [[0,1,0,3],[1,3,7,8],[0,2,1,5],[2,3,4,7]]`
- **Output:** `5`
- **Explanation:** The optimal path is: 

 
 Wait at node 0 until time `t = 1`, then take the edge `(0 &rarr; 2)` which is available from 1 to 5. You arrive at node 2 at `t = 2`. 
 Wait at node 2 until time `t = 4`, then take the edge `(2 &rarr; 3)` which is available from 4 to 7. You arrive at node 3 at `t = 5`. 
 

 Hence, the minimum time to reach node 3 is 5.

### Example 3
- **Input:** `n = 3, edges = [[1,0,1,3],[1,2,3,5]]`
- **Output:** `-1`
- **Explanation:** Since there is no outgoing edge from node 0, it is impossible to reach node 2. Hence, the output is -1.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time to Reach Destination in Directed Graph**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1,0,1],[1,2,2,5]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The optimal path is: 

 
 At time `t = 0`, take the edge `(0 &rarr; 1)` which is available from 0 to 1. You arrive at node 1 at time `t = 1`, then wait until `t = 2`. 
 At time `t = 2` , take the edge `(1 &rarr; 2)` which is available from 2 to 5. You arrive at node 2 at time 3. 
 

 Hence, the minimum time to reach node 2 is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minTime = function (n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, s, e] of edges) adj[u].push([v, s, e]);

    // Min-heap of [time, node]
    const heap = [];
    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p][0] <= heap[i][0]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            const len = heap.length;
            while (true) {
                const l = 2 * i + 1, r = l + 1;
                let s = i;
                if (l < len && heap[l][0] < heap[s][0]) s = l;
                if (r < len && heap[r][0] < heap[s][0]) s = r;
                if (s === i) break;
                [heap[s], heap[i]] = [heap[i], heap[s]];
                i = s;
            }
        }
        return top;
    };

    const dist = new Array(n).fill(Infinity);
    dist[0] = 0;
    push([0, 0]);

    while (heap.length) {
        const [t, u] = pop();
        if (t > dist[u]) continue;
        if (u === n - 1) return t;
        for (const [v, s, e] of adj[u]) {
            if (t > e) continue;
            const nt = Math.max(t, s) + 1;
            if (nt < dist[v]) {
                dist[v] = nt;
                push([nt, v]);
            }
        }
    }
    return -1;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1928. Minimum Cost to Reach Destination in Time](../../1501-2000/1928-minimum-cost-to-reach-destination-in-time/)
- [2045. Second Minimum Time to Reach Destination](../../2001-2500/2045-second-minimum-time-to-reach-destination/)
- [3341. Find Minimum Time to Reach Last Room I](../../3001-3500/3341-find-minimum-time-to-reach-last-room-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/)
