# LeetCode 872: Leaf-Similar Trees

**LeetCode Problem #872 — Leaf-Similar Trees**
Solve LeetCode Leaf-Similar Trees using JavaScript, Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Leaf-Similar Trees |
| LeetCode | #872 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence***.*

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered *leaf-similar* if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.

## Constraints
- The number of nodes in each tree will be in the range `[1, 200]`.
- Both of the given trees will have values in the range `[0, 200]`.

## Examples
### Example 1
- **Input:** `root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]`
- **Output:** `true`

### Example 2
- **Input:** `root1 = [1,2,3], root2 = [1,3,2]`
- **Output:** `false`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Leaf-Similar Trees**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
var leafSimilar = function(root1, root2) {
    function getLeaves(root, leaves) {
        if (root === null) {
            return;
        }

        if (root.left === null && root.right === null) {
            leaves.push(root.val);
            return;
        }

        getLeaves(root.left, leaves);
        getLeaves(root.right, leaves);
    }

    const leaves1 = [];
    const leaves2 = [];

    getLeaves(root1, leaves1);
    getLeaves(root2, leaves2);

    if (leaves1.length !== leaves2.length) {
        return false;
    }

    for (let i = 0; i < leaves1.length; i++) {
        if (leaves1[i] !== leaves2[i]) {
            return false;
        }
    }

    return true;
};
```

### Python
```python
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            if root is None:
                return []

            if root.left is None and root.right is None:
                return [root.val]

            return get_leaves(root.left) + get_leaves(root.right)

        return get_leaves(root1) == get_leaves(root2)
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
- [839. Similar String Groups](../../0501-1000/0869-similar-string-groups/)
- [854. K-Similar Strings](../../0501-1000/0884-k-similar-strings/)
- [1750. Minimum Length of String After Deleting Similar Ends](../../1501-2000/1850-minimum-length-of-string-after-deleting-similar-ends/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/leaf-similar-trees/)
