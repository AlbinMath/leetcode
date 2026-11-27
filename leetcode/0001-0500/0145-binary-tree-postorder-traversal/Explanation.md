# LeetCode 145: Binary Tree Postorder Traversal

**LeetCode Problem #145 — Binary Tree Postorder Traversal**
Solve LeetCode Binary Tree Postorder Traversal using PHP and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Tree Postorder Traversal |
| LeetCode | #145 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of a binary tree, return *the postorder traversal of its nodes' values*.

## Constraints
- The number of the nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [1,null,2,3]`
- **Output:** `[3,2,1]`

### Example 2
- **Input:** `root = [1,2,3,4,5,null,8,null,null,6,7,9]`
- **Output:** `[4,6,7,5,2,9,8,3,1]`

### Example 3
- **Input:** `root = []`
- **Output:** `[]`

### Example 4
- **Input:** `root = [1]`
- **Output:** `[1]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Binary Tree Postorder Traversal**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,null,2,3]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2,1]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = 0;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */

class Solution {
    function postorderTraversal($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $stack = [$root];

        while (!empty($stack)) {
            $node = array_pop($stack);

            // Add root first
            $result[] = $node->val;

            // Push left first
            if ($node->left !== null) {
                $stack[] = $node->left;
            }

            // Push right second
            if ($node->right !== null) {
                $stack[] = $node->right;
            }
        }

        // Root → Right → Left
        // Reverse → Left → Right → Root
        return array_reverse($result);
    }
}
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [106. Construct Binary Tree from Inorder and Postorder Traversal](../../0001-0500/0106-construct-binary-tree-from-inorder-and-postorder-traversal/)
- [889. Construct Binary Tree from Preorder and Postorder Traversal](../../0501-1000/0889-construct-binary-tree-from-preorder-and-postorder-traversal/)
- [590. N-ary Tree Postorder Traversal](../../0501-1000/0590-n-ary-tree-postorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-tree-postorder-traversal/)
