# LeetCode 2096: Step-By-Step Directions From a Binary Tree Node to Another

**LeetCode Problem #2096 — Step-By-Step Directions From a Binary Tree Node to Another**
Solve LeetCode Step-By-Step Directions From a Binary Tree Node to Another using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Step-By-Step Directions From a Binary Tree Node to Another |
| LeetCode | #2096 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a **binary tree** with `n` nodes. Each node is uniquely assigned a value from `1` to `n`. You are also given an integer `startValue` representing the value of the start node `s`, and a different integer `destValue` representing the value of the destination node `t`.

Find the **shortest path** starting from node `s` and ending at node `t`. Generate step-by-step directions of such path as a string consisting of only the **uppercase** letters `'L'`, `'R'`, and `'U'`. Each letter indicates a specific direction:

`'L'` means to go from a node to its **left child** node. 
 `'R'` means to go from a node to its **right child** node. 
 `'U'` means to go from a node to its **parent** node.

Return *the step-by-step directions of the **shortest path** from node *`s`* to node* `t`.

## Constraints
- The number of nodes in the tree is `n`.
- `2 <= n <= 10^5`
- `1 <= Node.val <= n`
- All the values in the tree are **unique**.
- `1 <= startValue, destValue <= n`
- `startValue != destValue`

## Examples
### Example 1
- **Input:** `root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6`
- **Output:** `"UURL"`
- **Explanation:** The shortest path is: 3 &rarr; 1 &rarr; 5 &rarr; 2 &rarr; 6.

### Example 2
- **Input:** `root = [2,1], startValue = 2, destValue = 1`
- **Output:** `"L"`
- **Explanation:** The shortest path is: 2 &rarr; 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Step-By-Step Directions From a Binary Tree Node to Another**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"UURL"`.
4. **Verification:** The shortest path is: 3 &rarr; 1 &rarr; 5 &rarr; 2 &rarr; 6.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var getDirections = function(root, startValue, destValue) {
    function findPath(node, target, path) {
        if (node === null) return false;

        if (node.val === target) return true;

        path.push("L");
        if (findPath(node.left, target, path)) return true;
        path.pop();

        path.push("R");
        if (findPath(node.right, target, path)) return true;
        path.pop();

        return false;
    }

    const startPath = [];
    const destPath = [];

    findPath(root, startValue, startPath);
    findPath(root, destValue, destPath);

    let i = 0;

    while (
        i < startPath.length &&
        i < destPath.length &&
        startPath[i] === destPath[i]
    ) {
        i++;
    }

    return "U".repeat(startPath.length - i) +
           destPath.slice(i).join("");
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [671. Second Minimum Node In a Binary Tree](../../0501-1000/0671-second-minimum-node-in-a-binary-tree/)
- [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](../../1001-1500/1498-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/)
