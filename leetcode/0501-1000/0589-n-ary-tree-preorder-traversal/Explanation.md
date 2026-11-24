# LeetCode 589: N-ary Tree Preorder Traversal

**LeetCode Problem #589 — N-ary Tree Preorder Traversal**
Solve LeetCode N-ary Tree Preorder Traversal using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | N-ary Tree Preorder Traversal |
| LeetCode | #589 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of an n-ary tree, return *the preorder traversal of its nodes' values*.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `0 <= Node.val <= 10^4`
- The height of the n-ary tree is less than or equal to `1000`.

## Examples
### Example 1
- **Input:** `root = [1,null,3,2,4,null,5,6]`
- **Output:** `[1,3,5,6,2,4]`

### Example 2
- **Input:** `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`
- **Output:** `[1,2,3,6,7,11,14,4,8,12,5,9,13,10]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **N-ary Tree Preorder Traversal**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,null,3,2,4,null,5,6]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,5,6,2,4]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def preorder(self, root):
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Add children in reverse order
            for child in reversed(node.children):
                stack.append(child)

        return result
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
- [429. N-ary Tree Level Order Traversal](../../0001-0500/0429-n-ary-tree-level-order-traversal/)
- [590. N-ary Tree Postorder Traversal](../../0501-1000/0590-n-ary-tree-postorder-traversal/)
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
