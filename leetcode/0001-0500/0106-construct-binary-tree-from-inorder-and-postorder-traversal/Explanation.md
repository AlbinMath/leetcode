# LeetCode 106: Construct Binary Tree from Inorder and Postorder Traversal

**LeetCode Problem #106 — Construct Binary Tree from Inorder and Postorder Traversal**
Solve LeetCode Construct Binary Tree from Inorder and Postorder Traversal using JavaScript, Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct Binary Tree from Inorder and Postorder Traversal |
| LeetCode | #106 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return *the binary tree*.

## Constraints
- `1 <= inorder.length <= 3000`
- `postorder.length == inorder.length`
- `-3000 <= inorder[i], postorder[i] <= 3000`
- `inorder` and `postorder` consist of **unique** values.
- Each value of `postorder` also appears in `inorder`.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.
- `postorder` is **guaranteed** to be the postorder traversal of the tree.

## Examples
### Example 1
- **Input:** `inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]`
- **Output:** `[3,9,20,null,null,15,7]`

### Example 2
- **Input:** `inorder = [-1], postorder = [-1]`
- **Output:** `[-1]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Construct Binary Tree from Inorder and Postorder Traversal**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,9,20,null,null,15,7]`.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var buildTree = function(inorder, postorder) {
    const inorderMap = new Map();

    for (let i = 0; i < inorder.length; i++) {
        inorderMap.set(inorder[i], i);
    }

    let postorderIndex = postorder.length - 1;

    function build(left, right) {
        if (left > right) {
            return null;
        }

        const rootValue = postorder[postorderIndex--];
        const root = new TreeNode(rootValue);

        const mid = inorderMap.get(rootValue);

        // Build right subtree first
        root.right = build(mid + 1, right);
        root.left = build(left, mid - 1);

        return root;
    }

    return build(0, inorder.length - 1);
};
```

### Python
```python
class Solution:
    def buildTree(self, inorder, postorder):
        pos = {v: i for i, v in enumerate(inorder)}
        def build(l, r):
            if l > r:
                return None
            v = postorder.pop()
            root = TreeNode(v)
            m = pos[v]
            root.right = build(m+1, r)
            root.left = build(l, m-1)
            return root
        return build(0, len(inorder)-1)
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
- [889. Construct Binary Tree from Preorder and Postorder Traversal](../../0501-1000/0925-construct-binary-tree-from-preorder-and-postorder-traversal/)
- [1008. Construct Binary Search Tree from Preorder Traversal](../../1001-1500/1050-construct-binary-search-tree-from-preorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
