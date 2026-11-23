# LeetCode 998: Maximum Binary Tree II

**LeetCode Problem #998 — Maximum Binary Tree II**
Solve LeetCode Maximum Binary Tree II using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Binary Tree II |
| LeetCode | #998 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A **maximum tree** is a tree where every node has a value greater than any other value in its subtree.

You are given the `root` of a maximum binary tree and an integer `val`.

Just as in the previous problem , the given tree was constructed from a list `a` (`root = Construct(a)`) recursively with the following `Construct(a)` routine:

If `a` is empty, return `null`. 
 Otherwise, let `a[i]` be the largest element of `a`. Create a `root` node with the value `a[i]`. 
 The left child of `root` will be `Construct([a[0], a[1], ..., a[i - 1]])`. 
 The right child of `root` will be `Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]])`. 
 Return `root`.

Note that we were not given `a` directly, only a root node `root = Construct(a)`.

Suppose `b` is a copy of `a` with the value `val` appended to it. It is guaranteed that `b` has unique values.

Return `Construct(b)`.

## Constraints
- The number of nodes in the tree is in the range `[1, 100]`.
- `1 <= Node.val <= 100`
- All the values of the tree are **unique**.
- `1 <= val <= 100`

## Examples
### Example 1
- **Input:** `root = [4,1,3,null,null,2], val = 5`
- **Output:** `[5,4,null,1,3,null,null,2]`
- **Explanation:** a = [1,4,2,3], b = [1,4,2,3,5]

### Example 2
- **Input:** `root = [5,2,4,null,1], val = 3`
- **Output:** `[5,2,4,null,1,null,3]`
- **Explanation:** a = [2,1,5,4], b = [2,1,5,4,3]

### Example 3
- **Input:** `root = [5,2,3,null,1], val = 4`
- **Output:** `[5,2,4,null,1,3]`
- **Explanation:** a = [2,1,5,3], b = [2,1,5,3,4]

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Binary Tree II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [4,1,3,null,null,2], val = 5`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,4,null,1,3,null,null,2]`.
4. **Verification:** a = [1,4,2,3], b = [1,4,2,3,5]

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import Optional

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or val > root.val:
            return TreeNode(val, root, None)
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [654. Maximum Binary Tree](../../0501-1000/0654-maximum-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-binary-tree-ii/)
