# LeetCode 2360: Longest Cycle in a Graph

**LeetCode Problem #2360 — Longest Cycle in a Graph**
Solve LeetCode Longest Cycle in a Graph using JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Cycle in a Graph |
| LeetCode | #2360 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **directed** graph of `n` nodes numbered from `0` to `n - 1`, where each node has **at most one** outgoing edge.

The graph is represented with a given **0-indexed** array `edges` of size `n`, indicating that there is a directed edge from node `i` to node `edges[i]`. If there is no outgoing edge from node `i`, then `edges[i] == -1`.

Return *the length of the **longest** cycle in the graph*. If no cycle exists, return `-1`.

A cycle is a path that starts and ends at the **same** node.

## Constraints
- `n == edges.length`
- `2 <= n <= 10^5`
- `-1 <= edges[i] < n`
- `edges[i] != i`

## Examples
### Example 1
- **Input:** `edges = [3,3,4,2,3]`
- **Output:** `3`
- **Explanation:** The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.

### Example 2
- **Input:** `edges = [2,-1,3,1]`
- **Output:** `-1`
- **Explanation:** There are no cycles in this graph.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Cycle in a Graph**, we observe the problem requirements and utilize the **Fast & Slow Pointers** technique. We iterate through the inputs using **Floyd Cycle Detection**, leveraging a **Linked List / Pointer** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Linked List / Pointer**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [3,3,4,2,3]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} edges
 * @return {number}
 */
var longestCycle = function (edges) {
    const n = edges.length;
    const walk = new Int32Array(n).fill(-1); // id of the walk that first visited the node
    const dist = new Int32Array(n);          // step index within that walk
    let ans = -1;

    for (let s = 0; s < n; s++) {
        if (walk[s] !== -1) continue;
        let cur = s, step = 0;
        while (cur !== -1 && walk[cur] === -1) {
            walk[cur] = s;
            dist[cur] = step++;
            cur = edges[cur];
        }
        if (cur !== -1 && walk[cur] === s) {
            const len = step - dist[cur];
            if (len > ans) ans = len;
        }
    }
    return ans;
};
```

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2608. Shortest Cycle in a Graph](../../2501-3000/2671-shortest-cycle-in-a-graph/)
- [3615. Longest Palindromic Path in Graph](../../3501-4000/3930-longest-palindromic-path-in-graph/)
- [133. Clone Graph](../../0001-0500/0133-clone-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-cycle-in-a-graph/)
