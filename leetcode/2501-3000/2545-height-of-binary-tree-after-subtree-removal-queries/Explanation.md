# LeetCode 2458: Height of Binary Tree After Subtree Removal Queries

**LeetCode Problem #2458 — Height of Binary Tree After Subtree Removal Queries**
Solve LeetCode Height of Binary Tree After Subtree Removal Queries using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Height of Binary Tree After Subtree Removal Queries |
| LeetCode | #2458 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a **binary tree** with `n` nodes. Each node is assigned a unique value from `1` to `n`. You are also given an array `queries` of size `m`.

You have to perform `m` **independent** queries on the tree where in the `i^th` query you do the following:

**Remove** the subtree rooted at the node with the value `queries[i]` from the tree. It is **guaranteed** that `queries[i]` will **not** be equal to the value of the root.

Return *an array *`answer`* of size *`m`* where *`answer[i]`* is the height of the tree after performing the *`i^th`* query*.

**Note**:

The queries are independent, so the tree returns to its **initial** state after each query. 
 The height of a tree is the **number of edges in the longest simple path** from the root to some node in the tree.

## Constraints
- The number of nodes in the tree is `n`.
- `2 <= n <= 10^5`
- `1 <= Node.val <= n`
- All the values in the tree are **unique**.
- `m == queries.length`
- `1 <= m <= min(n, 10^4)`
- `1 <= queries[i] <= n`
- `queries[i] != root.val`

## Examples
### Example 1
- **Input:** `root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]`
- **Output:** `[2]`
- **Explanation:** The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).

### Example 2
- **Input:** `root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]`
- **Output:** `[3,2,3,2]`
- **Explanation:** We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Height of Binary Tree After Subtree Removal Queries**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2]`.
4. **Verification:** The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).

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
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth = {}
        height = {}
        order = []
        stack = [(root, 0)]
        while stack:
            node, d = stack.pop()
            depth[node] = d
            order.append(node)
            if node.left:
                stack.append((node.left, d + 1))
            if node.right:
                stack.append((node.right, d + 1))

        for node in reversed(order):
            hl = height[node.left] if node.left else -1
            hr = height[node.right] if node.right else -1
            height[node] = max(hl, hr) + 1

        res = {}
        best = {root: 0}
        for node in order:  # parents appear before children
            b = best[node]
            d = depth[node]
            hl = height[node.left] if node.left else -1
            hr = height[node.right] if node.right else -1
            if node.left:
                best[node.left] = max(b, d + 1 + hr)
                res[node.left.val] = best[node.left]
            if node.right:
                best[node.right] = max(b, d + 1 + hl)
                res[node.right.val] = best[node.right]

        return [res[q] for q in queries]
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
- [3319. K-th Largest Perfect Subtree Size in Binary Tree](../../3501-4000/3509-k-th-largest-perfect-subtree-size-in-binary-tree/)
- [2476. Closest Nodes Queries in a Binary Search Tree](../../2501-3000/2567-closest-nodes-queries-in-a-binary-search-tree/)
- [572. Subtree of Another Tree](../../0501-1000/0572-subtree-of-another-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/)
