# LeetCode 834: Sum of Distances in Tree

**LeetCode Problem #834 — Sum of Distances in Tree**
Solve LeetCode Sum of Distances in Tree using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Distances in Tree |
| LeetCode | #834 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

You are given the integer `n` and the array `edges` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

Return an array `answer` of length `n` where `answer[i]` is the sum of the distances between the `i^th` node in the tree and all other nodes.

## Constraints
- `1 <= n <= 3 * 10^4`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- The given input represents a valid tree.

## Examples
### Example 1
- **Input:** `n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]`
- **Output:** `[8,12,6,10,10,10]`
- **Explanation:** The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

### Example 2
- **Input:** `n = 1, edges = []`
- **Output:** `[0]`

### Example 3
- **Input:** `n = 2, edges = [[1,0]]`
- **Output:** `[1,1]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Sum of Distances in Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[8,12,6,10,10,10]`.
4. **Verification:** The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

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
var sumOfDistancesInTree = function(n, edges) {
    // Step 1: Build adjacency list
    let graph = Array.from({ length: n }, () => []);

    for (let [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    let parent = new Array(n).fill(-1);
    let size = new Array(n).fill(1);
    let answer = new Array(n).fill(0);
    let order = [0];

    parent[0] = -2;

    // Step 2: Build traversal order and calculate depths
    for (let i = 0; i < order.length; i++) {
        let node = order[i];

        for (let child of graph[node]) {
            if (child === parent[node]) continue;

            parent[child] = node;
            order.push(child);

            answer[0] += 1;
        }
    }

    // Calculate total distance from root
    // using each node's depth
    let depth = new Array(n).fill(0);

    for (let node of order) {
        if (parent[node] >= 0) {
            depth[node] = depth[parent[node]] + 1;
        }
    }

    answer[0] = depth.reduce((sum, d) => sum + d, 0);

    // Step 3: Calculate subtree sizes (bottom-up)
    for (let i = n - 1; i > 0; i--) {
        let node = order[i];
        size[parent[node]] += size[node];
    }

    // Step 4: Reroot DP (top-down)
    for (let i = 1; i < n; i++) {
        let node = order[i];
        let p = parent[node];

        answer[node] = answer[p] - size[node] + (n - size[node]);
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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [1038. Binary Search Tree to Greater Sum Tree](../../1001-1500/1114-binary-search-tree-to-greater-sum-tree/)
- [1161. Maximum Level Sum of a Binary Tree](../../1001-1500/1116-maximum-level-sum-of-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-distances-in-tree/)
