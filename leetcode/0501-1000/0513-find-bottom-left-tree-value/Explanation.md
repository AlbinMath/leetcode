# LeetCode 513: Find Bottom Left Tree Value

**LeetCode Problem #513 — Find Bottom Left Tree Value**
Solve LeetCode Find Bottom Left Tree Value using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Bottom Left Tree Value |
| LeetCode | #513 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a binary tree.

Return the **leftmost** value in the **last** row of the tree.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `root = [2,1,3]`
- **Output:** `1`
- **Explanation:** The last row is [1,3], so the leftmost value is 1.

### Example 2
- **Input:** `root = [1,2,3,4,null,5,6,null,null,7]`
- **Output:** `7`
- **Explanation:** The last row contains only the node 7.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find Bottom Left Tree Value**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [2,1,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The last row is [1,3], so the leftmost value is 1.

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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        curr = root
        
        while queue:
            curr = queue.popleft()
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
                
        return curr.val
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
- [501. Find Mode in Binary Search Tree](../../0501-1000/0501-find-mode-in-binary-search-tree/)
- [1261. Find Elements in a Contaminated Binary Tree](../../1001-1500/1261-find-elements-in-a-contaminated-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-bottom-left-tree-value/)
