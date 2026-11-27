# LeetCode 558: Logical OR of Two Binary Grids Represented as Quad-Trees

**LeetCode Problem #558 — Logical OR of Two Binary Grids Represented as Quad-Trees**
Solve LeetCode Logical OR of Two Binary Grids Represented as Quad-Trees using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Logical OR of Two Binary Grids Represented as Quad-Trees |
| LeetCode | #558 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A Binary Matrix is a matrix in which all the elements are either **0** or **1**.

Given `quadTree1` and `quadTree2`. `quadTree1` represents a `n * n` binary matrix and `quadTree2` represents another `n * n` binary matrix.

Return *a Quad-Tree* representing the `n * n` binary matrix which is the result of **logical bitwise OR** of the two binary matrixes represented by `quadTree1` and `quadTree2`.

Notice that you can assign the value of a node to **True** or **False** when `isLeaf` is **False**, and both are **accepted** in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

`val`: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
 `isLeaf`: True if the node is leaf node on the tree or False if the node has the four children.

class Node {
 public boolean val;
 public boolean isLeaf;
 public Node topLeft;
 public Node topRight;
 public Node bottomLeft;
 public Node bottomRight;
}

We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all `1's` or all `0's`) set `isLeaf` True and set `val` to the value of the grid and set the four children to Null and stop. 
 If the current grid has different values, set `isLeaf` to False and set `val` to any value and divide the current grid into four sub-grids as shown in the photo. 
 Recurse for each of the children with the proper sub-grid. 
 
 
 If you want to know more about the Quad-Tree, you can refer to the wiki .

**Quad-Tree format:**

The input/output represents the serialized format of a Quad-Tree using level order traversal, where `null` signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list `[isLeaf, val]`.

If the value of `isLeaf` or `val` is True we represent it as **1** in the list `[isLeaf, val]` and if the value of `isLeaf` or `val` is False we represent it as **0**.

## Constraints
- `quadTree1` and `quadTree2` are both **valid** Quad-Trees each representing a `n * n` grid.
- `n == 2^x` where `0 <= x <= 9`.

## Examples
### Example 1
- **Input:** `quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
, quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]`
- **Output:** `[[0,0],[1,1],[1,1],[1,1],[1,0]]`
- **Explanation:** quadTree1 and quadTree2 are shown above. You can see the binary matrix which is represented by each Quad-Tree.
If we apply logical bitwise OR on the two binary matrices we get the binary matrix below which is represented by the result Quad-Tree.
Notice that the binary matrices shown are only for illustration, you don't have to construct the binary matrix to get the result tree.

### Example 2
- **Input:** `quadTree1 = [[1,0]], quadTree2 = [[1,0]]`
- **Output:** `[[1,0]]`
- **Explanation:** Each tree represents a binary matrix of size 1*1. Each matrix contains only zero.
The resulting matrix is of size 1*1 with also zero.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Logical OR of Two Binary Grids Represented as Quad-Trees**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
, quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,0],[1,1],[1,1],[1,1],[1,0]]`.
4. **Verification:** quadTree1 and quadTree2 are shown above. You can see the binary matrix which is represented by each Quad-Tree.
If we apply logical bitwise OR on the two binary matrices we get the binary matrix below which is represented by the result Quad-Tree.
Notice that the binary matrices shown are only for illustration, you don't have to construct the binary matrix to get the result tree.

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
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None,
                 bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        a, b = quadTree1, quadTree2

        if a.isLeaf:
            return a if a.val else b
        if b.isLeaf:
            return b if b.val else a

        tl = self.intersect(a.topLeft, b.topLeft)
        tr = self.intersect(a.topRight, b.topRight)
        bl = self.intersect(a.bottomLeft, b.bottomLeft)
        br = self.intersect(a.bottomRight, b.bottomRight)

        if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
                and tl.val == tr.val == bl.val == br.val):
            return Node(tl.val, True)

        return Node(False, False, tl, tr, bl, br)
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
- [617. Merge Two Binary Trees](../../0501-1000/0617-merge-two-binary-trees/)
- [1305. All Elements in Two Binary Search Trees](../../1001-1500/1305-all-elements-in-two-binary-search-trees/)
- [2816. Double a Number Represented as a Linked List](../../2501-3000/2816-double-a-number-represented-as-a-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/)
