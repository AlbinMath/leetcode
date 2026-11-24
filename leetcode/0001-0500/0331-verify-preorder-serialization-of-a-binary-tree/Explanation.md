# LeetCode 331: Verify Preorder Serialization of a Binary Tree

**LeetCode Problem #331 — Verify Preorder Serialization of a Binary Tree**
Solve LeetCode Verify Preorder Serialization of a Binary Tree using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Verify Preorder Serialization of a Binary Tree |
| LeetCode | #331 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
One way to serialize a binary tree is to use **preorder traversal**. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as `'#'`.

For example, the above binary tree can be serialized to the string `"9,3,4,#,#,1,#,#,2,#,6,#,#"`, where `'#'` represents a null node.

Given a string of comma-separated values `preorder`, return `true` if it is a correct preorder traversal serialization of a binary tree.

It is **guaranteed** that each comma-separated value in the string must be either an integer or a character `'#'` representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as `"1,,3"`.

**Note: **You are not allowed to reconstruct the tree.

## Constraints
- `1 <= preorder.length <= 10^4`
- `preorder` consist of integers in the range `[0, 100]` and `'#'` separated by commas `','`.

## Examples
### Example 1
- **Input:** `preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"`
- **Output:** `true`

### Example 2
- **Input:** `preorder = "1,#"`
- **Output:** `false`

### Example 3
- **Input:** `preorder = "9,#,#,1"`
- **Output:** `false`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Verify Preorder Serialization of a Binary Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var isValidSerialization = function(preorder) {
    let slots = 1;

    const nodes = preorder.split(',');

    for (let node of nodes) {
        // No available slot for this node
        if (slots === 0) {
            return false;
        }

        // Consume one slot
        slots--;

        // Non-null node creates two child slots
        if (node !== '#') {
            slots += 2;
        }
    }

    // All slots must be filled
    return slots === 0;
};
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
- [144. Binary Tree Preorder Traversal](../../0001-0500/0144-binary-tree-preorder-traversal/)
- [889. Construct Binary Tree from Preorder and Postorder Traversal](../../0501-1000/0889-construct-binary-tree-from-preorder-and-postorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/)
