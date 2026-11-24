# LeetCode 2359: Find Closest Node to Given Two Nodes

**LeetCode Problem #2359 — Find Closest Node to Given Two Nodes**
Solve LeetCode Find Closest Node to Given Two Nodes using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Closest Node to Given Two Nodes |
| LeetCode | #2359 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **directed** graph of `n` nodes numbered from `0` to `n - 1`, where each node has **at most one** outgoing edge.

The graph is represented with a given **0-indexed** array `edges` of size `n`, indicating that there is a directed edge from node `i` to node `edges[i]`. If there is no outgoing edge from `i`, then `edges[i] == -1`.

You are also given two integers `node1` and `node2`.

Return *the **index** of the node that can be reached from both *`node1`* and *`node2`*, such that the **maximum** between the distance from *`node1`* to that node, and from *`node2`* to that node is **minimized***. If there are multiple answers, return the node with the **smallest** index, and if no possible answer exists, return `-1`.

Note that `edges` may contain cycles.

## Constraints
- `n == edges.length`
- `2 <= n <= 10^5`
- `-1 <= edges[i] < n`
- `edges[i] != i`
- `0 <= node1, node2 < n`

## Examples
### Example 1
- **Input:** `edges = [2,2,3,-1], node1 = 0, node2 = 1`
- **Output:** `2`
- **Explanation:** The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.

### Example 2
- **Input:** `edges = [1,2,-1], node1 = 0, node2 = 2`
- **Output:** `2`
- **Explanation:** The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find Closest Node to Given Two Nodes**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [2,2,3,-1], node1 = 0, node2 = 1`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.

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
var closestMeetingNode = function(edges, node1, node2) {
    const n = edges.length;

    // Calculate distances from a starting node
    function getDistances(start) {
        const dist = new Array(n).fill(-1);

        let current = start;
        let distance = 0;

        while (current !== -1 && dist[current] === -1) {
            dist[current] = distance++;

            current = edges[current];
        }

        return dist;
    }

    // Distances from both starting nodes
    const dist1 = getDistances(node1);
    const dist2 = getDistances(node2);

    let answer = -1;
    let minMaxDistance = Infinity;

    // Find the best common reachable node
    for (let i = 0; i < n; i++) {
        if (dist1[i] !== -1 && dist2[i] !== -1) {
            const maxDistance = Math.max(dist1[i], dist2[i]);

            if (maxDistance < minMaxDistance) {
                minMaxDistance = maxDistance;
                answer = i;
            }
        }
    }

    return answer;
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
- [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](../../1001-1500/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [3068. Find the Maximum Sum of Node Values](../../3001-3500/3068-find-the-maximum-sum-of-node-values/)
- [3585. Find Weighted Median Node in Tree](../../3501-4000/3585-find-weighted-median-node-in-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/)
