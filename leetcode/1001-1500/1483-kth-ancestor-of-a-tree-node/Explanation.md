# LeetCode 1483: Kth Ancestor of a Tree Node

**LeetCode Problem #1483 — Kth Ancestor of a Tree Node**
Solve LeetCode Kth Ancestor of a Tree Node using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Ancestor of a Tree Node |
| LeetCode | #1483 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a tree with `n` nodes numbered from `0` to `n - 1` in the form of a parent array `parent` where `parent[i]` is the parent of `i^th` node. The root of the tree is node `0`. Find the `k^th` ancestor of a given node.

The `k^th` ancestor of a tree node is the `k^th` node in the path from that node to the root node.

Implement the `TreeAncestor` class:

`TreeAncestor(int n, int[] parent)` Initializes the object with the number of nodes in the tree and the parent array. 
 `int getKthAncestor(int node, int k)` return the `k^th` ancestor of the given node `node`. If there is no such ancestor, return `-1`.

## Constraints
- `1 <= k <= n <= 5 * 10^4`
- `parent.length == n`
- `parent[0] == -1`
- `0 <= parent[i] < n` for all `0 < i < n`
- `0 <= node < n`
- There will be at most `5 * 10^4` queries.

## Examples
### Example 1
- **Input:** `["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
[[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]`
- **Output:** `[null, 1, 0, -1]`
- **Explanation:** TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Kth Ancestor of a Tree Node**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
[[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 1, 0, -1]`.
4. **Verification:** TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor

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
var TreeAncestor = function(n, parent) {
    this.LOG = 16;
    this.up = Array.from(
        { length: n },
        () => Array(this.LOG).fill(-1)
    );

    for (let i = 0; i < n; i++) {
        this.up[i][0] = parent[i];
    }

    for (let j = 1; j < this.LOG; j++) {
        for (let i = 0; i < n; i++) {
            const prev = this.up[i][j - 1];

            if (prev !== -1) {
                this.up[i][j] = this.up[prev][j - 1];
            }
        }
    }
};

TreeAncestor.prototype.getKthAncestor = function(node, k) {
    let bit = 0;

    while (k > 0 && node !== -1) {
        if (k & 1) {
            node = this.up[node][bit];
        }

        k >>= 1;
        bit++;
    }

    return node;
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
- [608. Tree Node](../../0501-1000/0608-tree-node/)
- [671. Second Minimum Node In a Binary Tree](../../0501-1000/0671-second-minimum-node-in-a-binary-tree/)
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1026-maximum-difference-between-node-and-ancestor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/)
