# LeetCode 3715: Sum of Perfect Square Ancestors

**LeetCode Problem #3715 — Sum of Perfect Square Ancestors**
Solve LeetCode Sum of Perfect Square Ancestors using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Perfect Square Ancestors |
| LeetCode | #3715 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and an undirected tree rooted at node 0 with `n` nodes numbered from 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an undirected edge between nodes `u_i` and `v_i`.

You are also given an integer array `nums`, where `nums[i]` is the positive integer assigned to node `i`.

Define a value `t_i` as the number of **ancestors** of node `i` such that the product `nums[i] * nums[ancestor]` is a ** perfect square **.

Return the sum of all `t_i` values for all nodes `i` in range `[1, n - 1]`.

**Note**:

In a rooted tree, the **ancestors** of node `i` are all nodes on the path from node `i` to the root node 0, **excluding** `i` itself.

## Constraints
- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i] = [u_i, v_i]`
- `0 <= u_i, v_i <= n - 1`
- `nums.length == n`
- `1 <= nums[i] <= 10^5`
- The input is generated such that `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1],[1,2]], nums = [2,8,2]`
- **Output:** `3`

### Example 2
- **Input:** `n = 3, edges = [[0,1],[0,2]], nums = [1,2,4]`
- **Output:** `1`

### Example 3
- **Input:** `n = 4, edges = [[0,1],[0,2],[1,3]], nums = [1,2,9,4]`
- **Output:** `2`
- **Explanation:** `i`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Perfect Square Ancestors**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1],[1,2]], nums = [2,8,2]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} nums
 * @return {number}
 */
var sumOfAncestors = function(n, edges, nums) {
    const MAX_VAL = 100000;

    // 1. Build Smallest Prime Factor (SPF) sieve up to 100,000
    const spf = new Int32Array(MAX_VAL + 1);
    for (let i = 2; i <= MAX_VAL; i++) {
        if (spf[i] === 0) {
            for (let j = i; j <= MAX_VAL; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }

    // Helper to compute the square-free kernel of x
    const getKernel = (x) => {
        let kernel = 1;
        while (x > 1) {
            const p = spf[x];
            let odd = false;
            while (x % p === 0) {
                x = Math.floor(x / p);
                odd = !odd;
            }
            if (odd) kernel *= p;
        }
        return kernel;
    };

    // 2. Transform nums[i] into its square-free kernel
    const kernels = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        kernels[i] = getKernel(nums[i]);
    }

    // 3. Build adjacency list for the tree
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < edges.length; i++) {
        const [u, v] = edges[i];
        adj[u].push(v);
        adj[v].push(u);
    }

    // 4. Iterative DFS with backtracking to avoid call stack limits on deep trees
    const freq = new Int32Array(MAX_VAL + 1);
    const parent = new Int32Array(n).fill(-1);
    const edgeIdx = new Int32Array(n);
    const stack = [0];

    let total = 0;

    // Enter root 0 (root has no ancestors, so it adds 0 to total)
    freq[kernels[0]]++;

    while (stack.length > 0) {
        const u = stack[stack.length - 1];
        const neighbors = adj[u];

        if (edgeIdx[u] < neighbors.length) {
            const v = neighbors[edgeIdx[u]++];
            if (v === parent[u]) continue;

            parent[v] = u;
            const k = kernels[v];
            total += freq[k];
            freq[k]++;
            stack.push(v);
        } else {
            // Backtrack: remove u from the active ancestor path
            freq[kernels[u]]--;
            stack.pop();
        }
    }

    return total;
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [367. Valid Perfect Square](../../0001-0500/0367-valid-perfect-square/)
- [633. Sum of Square Numbers](../../0501-1000/0633-sum-of-square-numbers/)
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](../../1001-1500/1292-maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-perfect-square-ancestors/)
