# LeetCode 144: Binary Tree Preorder Traversal

**LeetCode Problem #144 — Binary Tree Preorder Traversal**
Solve LeetCode Binary Tree Preorder Traversal using PHP and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Tree Preorder Traversal |
| LeetCode | #144 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of a binary tree, return *the preorder traversal of its nodes' values*.

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [1,null,2,3]`
- **Output:** `[1,2,3]`

### Example 2
- **Input:** `root = [1,2,3,4,5,null,8,null,null,6,7,9]`
- **Output:** `[1,2,4,5,6,7,3,8,9]`

### Example 3
- **Input:** `root = []`
- **Output:** `[]`

### Example 4
- **Input:** `root = [1]`
- **Output:** `[1]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Binary Tree Preorder Traversal**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,null,2,3]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3]`.

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
    function preorderTraversal($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $stack = [$root];

        while (!empty($stack)) {
            // Take the top node
            $node = array_pop($stack);

            // Visit root
            $result[] = $node->val;

            // Push right first
            if ($node->right !== null) {
                $stack[] = $node->right;
            }

            // Push left second
            if ($node->left !== null) {
                $stack[] = $node->left;
            }
        }

        return $result;
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
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [889. Construct Binary Tree from Preorder and Postorder Traversal](../../0501-1000/0925-construct-binary-tree-from-preorder-and-postorder-traversal/)
- [971. Flip Binary Tree To Match Preorder Traversal](../../1001-1500/1011-flip-binary-tree-to-match-preorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/)
