# LeetCode 1104: Path In Zigzag Labelled Binary Tree

**LeetCode Problem #1104 — Path In Zigzag Labelled Binary Tree**
Solve LeetCode Path In Zigzag Labelled Binary Tree using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Path In Zigzag Labelled Binary Tree |
| LeetCode | #1104 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the `label` of a node in this tree, return the labels in the path from the root of the tree to the node with that `label`.

## Constraints
- `1 <= label <= 10^6`

## Examples
### Example 1
- **Input:** `label = 14`
- **Output:** `[1,3,4,14]`

### Example 2
- **Input:** `label = 26`
- **Output:** `[1,2,6,10,26]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Path In Zigzag Labelled Binary Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `label = 14`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,4,14]`.

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
var pathInZigZagTree = function(label) {
    let depth = Math.floor(Math.log2(label));
    const path = [];
    
    while (label >= 1) {
        path.push(label);
        const levelMin = 1 << depth;
        const levelMax = (1 << (depth + 1)) - 1;
        
        // Mirror current label across its row, then divide by 2 for its parent
        label = Math.floor((levelMin + levelMax - label) / 2);
        depth--;
    }
    
    return path.reverse();
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
- [1372. Longest ZigZag Path in a Binary Tree](../../1001-1500/1372-longest-zigzag-path-in-a-binary-tree/)
- [103. Binary Tree Zigzag Level Order Traversal](../../0001-0500/0103-binary-tree-zigzag-level-order-traversal/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/)
