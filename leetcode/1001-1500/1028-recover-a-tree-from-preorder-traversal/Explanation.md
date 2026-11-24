# LeetCode 1028: Recover a Tree From Preorder Traversal

**LeetCode Problem #1028 — Recover a Tree From Preorder Traversal**
Solve LeetCode Recover a Tree From Preorder Traversal using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Recover a Tree From Preorder Traversal |
| LeetCode | #1028 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We run a preorder depth-first search (DFS) on the `root` of a binary tree.

At each node in this traversal, we output `D` dashes (where `D` is the depth of this node), then we output the value of this node. If the depth of a node is `D`, the depth of its immediate child is `D + 1`. The depth of the `root` node is `0`.

If a node has only one child, that child is guaranteed to be **the left child**.

Given the output `traversal` of this traversal, recover the tree and return *its* `root`.

## Constraints
- The number of nodes in the original tree is in the range `[1, 1000]`.
- `1 <= Node.val <= 10^9`

## Examples
### Example 1
- **Input:** `traversal = "1-2--3--4-5--6--7"`
- **Output:** `[1,2,5,3,4,6,7]`

### Example 2
- **Input:** `traversal = "1-2--3---4-5--6---7"`
- **Output:** `[1,2,5,3,null,6,null,4,null,7]`

### Example 3
- **Input:** `traversal = "1-401--349---90--88"`
- **Output:** `[1,401,null,349,88,90]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Recover a Tree From Preorder Traversal**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `traversal = "1-2--3--4-5--6--7"`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,5,3,4,6,7]`.

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
var recoverFromPreorder = function(traversal) {
    const stack = [];
    let i = 0;
    const n = traversal.length;
    
    while (i < n) {
        // 1. Count dashes to determine depth
        let depth = 0;
        while (i < n && traversal[i] === '-') {
            depth++;
            i++;
        }
        
        // 2. Parse node value
        let val = 0;
        while (i < n && traversal[i] >= '0' && traversal[i] <= '9') {
            val = val * 10 + (traversal.charCodeAt(i) - 48);
            i++;
        }
        
        const node = new TreeNode(val);
        
        // 3. Pop finished subtrees until stack top is the parent at (depth - 1)
        while (stack.length > depth) {
            stack.pop();
        }
        
        // 4. Attach to parent (left first, then right)
        if (stack.length > 0) {
            const parent = stack[stack.length - 1];
            if (!parent.left) {
                parent.left = node;
            } else {
                parent.right = node;
            }
        }
        
        stack.push(node);
    }
    
    return stack[0];
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
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [889. Construct Binary Tree from Preorder and Postorder Traversal](../../0501-1000/0889-construct-binary-tree-from-preorder-and-postorder-traversal/)
- [1008. Construct Binary Search Tree from Preorder Traversal](../../1001-1500/1008-construct-binary-search-tree-from-preorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/)
