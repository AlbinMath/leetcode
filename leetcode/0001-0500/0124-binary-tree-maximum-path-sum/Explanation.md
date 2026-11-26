# LeetCode 124: Binary Tree Maximum Path Sum

**LeetCode Problem #124 — Binary Tree Maximum Path Sum**
Solve LeetCode Binary Tree Maximum Path Sum using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Tree Maximum Path Sum |
| LeetCode | #124 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum **path sum** of any **non-empty** path*.

## Constraints
- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- `-1000 <= Node.val <= 1000`

## Examples
### Example 1
- **Input:** `root = [1,2,3]`
- **Output:** `6`
- **Explanation:** The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

### Example 2
- **Input:** `root = [-10,9,20,null,null,15,7]`
- **Output:** `42`
- **Explanation:** The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Binary Tree Maximum Path Sum**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

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
var maxPathSum = function(root) {
    let maxSum = -Infinity;

    function dfs(node) {
        if (node === null) {
            return 0;
        }

        // Ignore negative contributions
        const leftGain = Math.max(0, dfs(node.left));
        const rightGain = Math.max(0, dfs(node.right));

        // Maximum path passing through this node
        const pathSum = node.val + leftGain + rightGain;

        maxSum = Math.max(maxSum, pathSum);

        // Return the best single branch to the parent
        return node.val + Math.max(leftGain, rightGain);
    }

    dfs(root);

    return maxSum;
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
- [1161. Maximum Level Sum of a Binary Tree](../../1001-1500/1161-maximum-level-sum-of-a-binary-tree/)
- [1373. Maximum Sum BST in Binary Tree](../../1001-1500/1373-maximum-sum-bst-in-binary-tree/)
- [1104. Path In Zigzag Labelled Binary Tree](../../1001-1500/1104-path-in-zigzag-labelled-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
