# LeetCode 1325: Delete Leaves With a Given Value

**LeetCode Problem #1325 — Delete Leaves With a Given Value**
Solve LeetCode Delete Leaves With a Given Value using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Leaves With a Given Value |
| LeetCode | #1325 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a binary tree `root` and an integer `target`, delete all the **leaf nodes** with value `target`.

Note that once you delete a leaf node with value `target`**, **if its parent node becomes a leaf node and has the value `target`, it should also be deleted (you need to continue doing that until you cannot).

## Constraints
- The number of nodes in the tree is in the range `[1, 3000]`.
- `1 <= Node.val, target <= 1000`

## Examples
### Example 1
- **Input:** `root = [1,2,3,2,null,2,4], target = 2`
- **Output:** `[1,null,3,null,4]`
- **Explanation:** Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

### Example 2
- **Input:** `root = [1,3,3,3,2], target = 3`
- **Output:** `[1,3,null,null,2]`

### Example 3
- **Input:** `root = [1,2,null,2,null,2], target = 2`
- **Output:** `[1]`
- **Explanation:** Leaf nodes in green with value (target = 2) are removed at each step.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Delete Leaves With a Given Value**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,3,2,null,2,4], target = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,null,3,null,4]`.
4. **Verification:** Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

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
var removeLeafNodes = function(root, target) {
    if (!root) return null;
    
    // Prune children first (post-order)
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);
    
    // If current node is now a leaf with value === target, delete it
    if (!root.left && !root.right && root.val === target) {
        return null;
    }
    
    return root;
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
- [1663. Smallest String With A Given Numeric Value](../../1501-2000/1663-smallest-string-with-a-given-numeric-value/)
- [2156. Find Substring With Given Hash Value](../../2001-2500/2156-find-substring-with-given-hash-value/)
- [3393. Count Paths With the Given XOR Value](../../3001-3500/3393-count-paths-with-the-given-xor-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-leaves-with-a-given-value/)
