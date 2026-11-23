# LeetCode 112: Path Sum

**LeetCode Problem #112 — Path Sum**
Solve LeetCode Path Sum using PHP and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Path Sum |
| LeetCode | #112 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

## Constraints
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

## Examples
### Example 1
- **Input:** `root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22`
- **Output:** `true`
- **Explanation:** The root-to-leaf path with the target sum is shown.

### Example 2
- **Input:** `root = [1,2,3], targetSum = 5`
- **Output:** `false`
- **Explanation:** There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

### Example 3
- **Input:** `root = [], targetSum = 0`
- **Output:** `false`
- **Explanation:** Since the tree is empty, there are no root-to-leaf paths.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Path Sum**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The root-to-leaf path with the target sum is shown.

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
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function hasPathSum($root, $targetSum) {
        if ($root === null) {
            return false;
        }

        // Leaf node
        if ($root->left === null && $root->right === null) {
            return $root->val == $targetSum;
        }

        $remaining = $targetSum - $root->val;

        return $this->hasPathSum($root->left, $remaining)
            || $this->hasPathSum($root->right, $remaining);
    }
}
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
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [113. Path Sum II](../../0001-0500/0113-path-sum-ii/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/path-sum/)
