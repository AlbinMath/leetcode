# LeetCode 1932: Merge BSTs to Create Single BST

**LeetCode Problem #1932 — Merge BSTs to Create Single BST**
Solve LeetCode Merge BSTs to Create Single BST using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge BSTs to Create Single BST |
| LeetCode | #1932 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given `n` **BST (binary search tree) root nodes** for `n` separate BSTs stored in an array `trees` (**0-indexed**). Each BST in `trees` has **at most 3 nodes**, and no two roots have the same value. In one operation, you can:

Select two **distinct** indices `i` and `j` such that the value stored at one of the **leaves **of `trees[i]` is equal to the **root value** of `trees[j]`. 
 Replace the leaf node in `trees[i]` with `trees[j]`. 
 Remove `trees[j]` from `trees`.

Return* the **root** of the resulting BST if it is possible to form a valid BST after performing *`n - 1`* operations, or** *`null` if it is impossible to create a valid BST .

A BST (binary search tree) is a binary tree where each node satisfies the following property:

Every node in the node's left subtree has a value **strictly less** than the node's value. 
 Every node in the node's right subtree has a value **strictly greater** than the node's value.

A leaf is a node that has no children.

## Constraints
- `n == trees.length`
- `1 <= n <= 5 * 10^4`
- The number of nodes in each tree is in the range `[1, 3]`.
- Each node in the input may have children but no grandchildren.
- No two roots of `trees` have the same value.
- All the trees in the input are **valid BSTs**.
- `1 <= TreeNode.val <= 5 * 10^4`.

## Examples
### Example 1
- **Input:** `trees = [[2,1],[3,2,5],[5,4]]`
- **Output:** `[3,2,5,1,null,4]`
- **Explanation:** In the first operation, pick i=1 and j=0, and merge trees[0] into trees[1].
Delete trees[0], so trees = [[3,2,5,1],[5,4]].
 
In the second operation, pick i=0 and j=1, and merge trees[1] into trees[0].
Delete trees[1], so trees = [[3,2,5,1,null,4]].
 
The resulting tree, shown above, is a valid BST, so return its root.

### Example 2
- **Input:** `trees = [[5,3,8],[3,2,6]]`
- **Output:** `[]`
- **Explanation:** Pick i=0 and j=1 and merge trees[1] into trees[0].
Delete trees[1], so trees = [[5,3,8,2,6]].
 
The resulting tree is shown above. This is the only valid operation that can be performed, but the resulting tree is not a valid BST, so return null.

### Example 3
- **Input:** `trees = [[5,4],[3]]`
- **Output:** `[]`
- **Explanation:** It is impossible to perform any operations.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Merge BSTs to Create Single BST**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `trees = [[2,1],[3,2,5],[5,4]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2,5,1,null,4]`.
4. **Verification:** In the first operation, pick i=1 and j=0, and merge trees[0] into trees[1].
Delete trees[0], so trees = [[3,2,5,1],[5,4]].
 
In the second operation, pick i=0 and j=1, and merge trees[1] into trees[0].
Delete trees[1], so trees = [[3,2,5,1,null,4]].
 
The resulting tree, shown above, is a valid BST, so return its root.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        val_to_tree = {}
        leaf_counts = collections.defaultdict(int)

        # 1. Map root values and count all leaf occurrences
        for tree in trees:
            val_to_tree[tree.val] = tree
            if tree.left:
                leaf_counts[tree.left.val] += 1
            if tree.right:
                leaf_counts[tree.right.val] += 1

        # 2. Find the unique global root candidate
        global_root = None
        for tree in trees:
            if tree.val not in leaf_counts:
                if global_root is not None:
                    return None  # Multiple candidates -> disjoint components
                global_root = tree

        if not global_root:
            return None

        # 3. Merge and validate BST via DFS with range limits (lower, upper)
        def validate_and_merge(node: Optional[TreeNode], lower: float, upper: float) -> bool:
            if not node:
                return True

            if not (lower < node.val < upper):
                return False

            # If it's a leaf and can be expanded with another tree
            if not node.left and not node.right:
                if node.val in val_to_tree and node != global_root:
                    attached = val_to_tree.pop(node.val)
                    node.left = attached.left
                    node.right = attached.right

            return (validate_and_merge(node.left, lower, node.val) and
                    validate_and_merge(node.right, node.val, upper))

        # Check if BST properties hold during traversal & expansion
        if not validate_and_merge(global_root, float('-inf'), float('inf')):
            return None

        # All trees except the global_root must have been merged and removed
        return global_root if len(val_to_tree) == 1 else None
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
- [136. Single Number](../../0001-0500/0136-single-number/)
- [137. Single Number II](../../0001-0500/0137-single-number-ii/)
- [260. Single Number III](../../0001-0500/0260-single-number-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-bsts-to-create-single-bst/)
