# LeetCode 3600: Maximize Spanning Tree Stability with Upgrades

**LeetCode Problem #3600 — Maximize Spanning Tree Stability with Upgrades**
Solve LeetCode Maximize Spanning Tree Stability with Upgrades using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Spanning Tree Stability with Upgrades |
| LeetCode | #3600 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`, representing `n` nodes numbered from 0 to `n - 1` and a list of `edges`, where `edges[i] = [u_i, v_i, s_i, must_i]`:

`u_i` and `v_i` indicates an undirected edge between nodes `u_i` and `v_i`. 
 `s_i` is the strength of the edge. 
 `must_i` is an integer (0 or 1). If `must_i == 1`, the edge **must** be included in the** ****spanning tree**. These edges **cannot** be **upgraded**.

You are also given an integer `k`, the **maximum** number of upgrades you can perform. Each upgrade **doubles** the strength of an edge, and each eligible edge (with `must_i == 0`) can be upgraded **at most** once.

The **stability** of a spanning tree is defined as the **minimum** strength score among all edges included in it.

Return the **maximum** possible stability of any valid spanning tree. If it is impossible to connect all nodes, return `-1`.

**Note**: A **spanning tree** of a graph with `n` nodes is a subset of the edges that connects all nodes together (i.e. the graph is **connected**) *without* forming any cycles, and uses **exactly** `n - 1` edges.

## Constraints
- `2 <= n <= 10^5`
- `1 <= edges.length <= 10^5`
- `edges[i] = [u_i, v_i, s_i, must_i]`
- `0 <= u_i, v_i < n`
- `u_i != v_i`
- `1 <= s_i <= 10^5`
- `must_i` is either `0` or `1`.
- `0 <= k <= n`
- There are no duplicate edges.

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1`
- **Output:** `2`
- **Explanation:** Edge `[0,1]` with strength = 2 must be included in the spanning tree. 
 Edge `[1,2]` is optional and can be upgraded from 3 to 6 using one upgrade. 
 The resulting spanning tree includes these two edges with strengths 2 and 6. 
 The minimum strength in the spanning tree is 2, which is the maximum possible stability.

### Example 2
- **Input:** `n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2`
- **Output:** `6`
- **Explanation:** Since all edges are optional and up to `k = 2` upgrades are allowed. 
 Upgrade edges `[0,1]` from 4 to 8 and `[1,2]` from 3 to 6. 
 The resulting spanning tree includes these two edges with strengths 8 and 6. 
 The minimum strength in the tree is 6, which is the maximum possible stability.

### Example 3
- **Input:** `n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0`
- **Output:** `-1`
- **Explanation:** All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Maximize Spanning Tree Stability with Upgrades**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Edge `[0,1]` with strength = 2 must be included in the spanning tree. 
 Edge `[1,2]` is optional and can be upgraded from 3 to 6 using one upgrade. 
 The resulting spanning tree includes these two edges with strengths 2 and 6. 
 The minimum strength in the spanning tree is 2, which is the maximum possible stability.

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
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} k
 * @return {number}
 */
var maxStability = function(n, edges, k) {
    class DSU {
        constructor(n) {
            this.parent = Array.from({ length: n }, (_, i) => i);
            this.rank = new Array(n).fill(0);
            this.components = n;
        }

        find(x) {
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
            return this.parent[x];
        }

        union(a, b) {
            a = this.find(a);
            b = this.find(b);

            if (a === b) return false;

            if (this.rank[a] < this.rank[b]) {
                [a, b] = [b, a];
            }

            this.parent[b] = a;

            if (this.rank[a] === this.rank[b]) {
                this.rank[a]++;
            }

            this.components--;
            return true;
        }
    }

    const mandatoryDSU = new DSU(n);
    let mandatoryMin = Infinity;

    for (const [u, v, s, must] of edges) {
        if (must === 1) {
            if (!mandatoryDSU.union(u, v)) return -1;
            mandatoryMin = Math.min(mandatoryMin, s);
        }
    }

    function canAchieve(target) {
        if (mandatoryMin < target) return false;

        const dsu = new DSU(n);

        for (const [u, v, s, must] of edges) {
            if (must === 1) {
                dsu.union(u, v);
            }
        }

        for (const [u, v, s, must] of edges) {
            if (must === 0 && s >= target) {
                dsu.union(u, v);
            }
        }

        let upgrades = 0;

        for (const [u, v, s, must] of edges) {
            if (must === 0 && s < target && 2 * s >= target) {
                if (dsu.union(u, v)) {
                    upgrades++;
                }
            }
        }

        return dsu.components === 1 && upgrades <= k;
    }

    let left = 1;
    let right = 200000;
    let answer = -1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (canAchieve(mid)) {
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
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
- [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](../../1501-2000/1613-find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)
- [94. Binary Tree Inorder Traversal](../../0001-0500/0094-binary-tree-inorder-traversal/)
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/)
