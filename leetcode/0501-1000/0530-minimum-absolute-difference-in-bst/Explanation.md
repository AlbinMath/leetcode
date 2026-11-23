# LeetCode 530: Minimum Absolute Difference in BST

**LeetCode Problem #530 — Minimum Absolute Difference in BST**
Solve LeetCode Minimum Absolute Difference in BST using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Absolute Difference in BST |
| LeetCode | #530 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a Binary Search Tree (BST), return *the minimum absolute difference between the values of any two different nodes in the tree*.

## Constraints
- The number of nodes in the tree is in the range `[2, 10^4]`.
- `0 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `root = [4,2,6,1,3]`
- **Output:** `1`

### Example 2
- **Input:** `root = [1,0,48,null,null,12,49]`
- **Output:** `1`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Minimum Absolute Difference in BST**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [4,2,6,1,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

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
    def getMinimumDifference(self, root):
        prev = None
        minimum = float('inf')

        def inorder(node):
            nonlocal prev, minimum

            if node is None:
                return

            inorder(node.left)

            if prev is not None:
                minimum = min(minimum, node.val - prev)

            prev = node.val

            inorder(node.right)

        inorder(root)

        return minimum
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
- [1200. Minimum Absolute Difference](../../1001-1500/1306-minimum-absolute-difference/)
- [3880. Minimum Absolute Difference Between Two Values](../../4001-4500/4255-minimum-absolute-difference-between-two-values/)
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0799-minimum-distance-between-bst-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
