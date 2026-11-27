# LeetCode 623: Add One Row to Tree

**LeetCode Problem #623 — Add One Row to Tree**
Solve LeetCode Add One Row to Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Add One Row to Tree |
| LeetCode | #623 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree and two integers `val` and `depth`, add a row of nodes with value `val` at the given depth `depth`.

Note that the `root` node is at depth `1`.

The adding rule is:

Given the integer `depth`, for each not null tree node `cur` at the depth `depth - 1`, create two tree nodes with value `val` as `cur`'s left subtree root and right subtree root. 
 `cur`'s original left subtree should be the left subtree of the new left subtree root. 
 `cur`'s original right subtree should be the right subtree of the new right subtree root. 
 If `depth == 1` that means there is no depth `depth - 1` at all, then create a tree node with value `val` as the new root of the whole original tree, and the original tree is the new root's left subtree.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- The depth of the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`
- `-10^5 <= val <= 10^5`
- `1 <= depth <= the depth of tree + 1`

## Examples
### Example 1
- **Input:** `root = [4,2,6,3,1,5], val = 1, depth = 2`
- **Output:** `[4,1,1,2,null,null,6,3,1,5]`

### Example 2
- **Input:** `root = [4,2,null,3,1], val = 1, depth = 3`
- **Output:** `[4,2,null,1,1,3,null,null,1]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Add One Row to Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [4,2,6,3,1,5], val = 1, depth = 2`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,1,1,2,null,null,6,3,1,5]`.

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
from typing import Optional
from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
            
        queue = deque([root])
        curr_depth = 1
        
        while queue:
            if curr_depth == depth - 1:
                for cur in queue:
                    cur.left = TreeNode(val, cur.left, None)
                    cur.right = TreeNode(val, None, cur.right)
                break
                
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            curr_depth += 1
            
        return root
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
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [67. Add Binary](../../0001-0500/0067-add-binary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/add-one-row-to-tree/)
