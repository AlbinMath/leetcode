# LeetCode 863: All Nodes Distance K in Binary Tree

**LeetCode Problem #863 — All Nodes Distance K in Binary Tree**
Solve LeetCode All Nodes Distance K in Binary Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Nodes Distance K in Binary Tree |
| LeetCode | #863 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return *an array of the values of all nodes that have a distance *`k`* from the target node.*

You can return the answer in **any order**.

## Constraints
- The number of nodes in the tree is in the range `[1, 500]`.
- `0 <= Node.val <= 500`
- All the values `Node.val` are **unique**.
- `target` is the value of one of the nodes in the tree.
- `0 <= k <= 1000`

## Examples
### Example 1
- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2`
- **Output:** `[7,4,1]`

### Example 2
- **Input:** `root = [1], target = 1, k = 3`
- **Output:** `[]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **All Nodes Distance K in Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[7,4,1]`.

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
from typing import List, Optional
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []

        def collect(node: Optional[TreeNode], dist: int) -> None:
            if not node or dist < 0:
                return
            if dist == 0:
                ans.append(node.val)
                return
            collect(node.left, dist - 1)
            collect(node.right, dist - 1)

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            if node is target:
                collect(node, k)
                return 0

            left_dist = dfs(node.left)
            if left_dist != -1:
                d = left_dist + 1
                if d == k:
                    ans.append(node.val)
                elif d < k:
                    collect(node.right, k - d - 1)
                return d

            right_dist = dfs(node.right)
            if right_dist != -1:
                d = right_dist + 1
                if d == k:
                    ans.append(node.val)
                elif d < k:
                    collect(node.left, k - d - 1)
                return d

            return -1

        dfs(root)
        return ans
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
- [1361. Validate Binary Tree Nodes](../../1001-1500/1361-validate-binary-tree-nodes/)
- [1448. Count Good Nodes in Binary Tree](../../1001-1500/1448-count-good-nodes-in-binary-tree/)
- [2476. Closest Nodes Queries in a Binary Search Tree](../../2001-2500/2476-closest-nodes-queries-in-a-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
