# LeetCode 2476: Closest Nodes Queries in a Binary Search Tree

**LeetCode Problem #2476 — Closest Nodes Queries in a Binary Search Tree**
Solve LeetCode Closest Nodes Queries in a Binary Search Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Closest Nodes Queries in a Binary Search Tree |
| LeetCode | #2476 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a **binary search tree **and an array `queries` of size `n` consisting of positive integers.

Find a **2D** array `answer` of size `n` where `answer[i] = [min_i, max_i]`:

`min_i` is the **largest** value in the tree that is smaller than or equal to `queries[i]`. If a such value does not exist, add `-1` instead. 
 `max_i` is the **smallest** value in the tree that is greater than or equal to `queries[i]`. If a such value does not exist, add `-1` instead.

Return *the array* `answer`.

## Constraints
- The number of nodes in the tree is in the range `[2, 10^5]`.
- `1 <= Node.val <= 10^6`
- `n == queries.length`
- `1 <= n <= 10^5`
- `1 <= queries[i] <= 10^6`

## Examples
### Example 1
- **Input:** `root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]`
- **Output:** `[[2,2],[4,6],[15,-1]]`
- **Explanation:** We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].

### Example 2
- **Input:** `root = [4,null,9], queries = [3]`
- **Output:** `[[-1,4]]`
- **Explanation:** The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4].

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Closest Nodes Queries in a Binary Search Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[2,2],[4,6],[15,-1]]`.
4. **Verification:** We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].

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
import bisect
from typing import List, Optional

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = []
        
        # In-order traversal to extract elements in sorted order
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        m = len(vals)
        res = []
        
        for q in queries:
            # bisect_right finds the insertion point after any existing q
            idx = bisect.bisect_right(vals, q)
            
            # mini is the largest element <= q
            mini = vals[idx - 1] if idx > 0 else -1
            
            # If the exact value q exists, maxi is also q
            if idx > 0 and vals[idx - 1] == q:
                maxi = q
            else:
                # Otherwise, maxi is the element at idx (first element > q)
                maxi = vals[idx] if idx < m else -1
                
            res.append([mini, maxi])
            
        return res
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
- [2458. Height of Binary Tree After Subtree Removal Queries](../../2001-2500/2458-height-of-binary-tree-after-subtree-removal-queries/)
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)
- [99. Recover Binary Search Tree](../../0001-0500/0099-recover-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/)
