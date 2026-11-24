# LeetCode 109: Convert Sorted List to Binary Search Tree

**LeetCode Problem #109 — Convert Sorted List to Binary Search Tree**
Solve LeetCode Convert Sorted List to Binary Search Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Convert Sorted List to Binary Search Tree |
| LeetCode | #109 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a singly linked list where elements are sorted in **ascending order**, convert *it to a * ***height-balanced*** *binary search tree*.

## Constraints
- The number of nodes in `head` is in the range `[0, 2 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `head = [-10,-3,0,5,9]`
- **Output:** `[0,-3,9,-10,null,5]`
- **Explanation:** One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

### Example 2
- **Input:** `head = []`
- **Output:** `[]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Convert Sorted List to Binary Search Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [-10,-3,0,5,9]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,-3,9,-10,null,5]`.
4. **Verification:** One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

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
class Solution(object):
    def sortedListToBST(self, head):
        # Count nodes
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        self.cur = head

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            left = build(lo, mid - 1)        # consume left half first
            root = TreeNode(self.cur.val)    # current list node is the root
            self.cur = self.cur.next
            root.left = left
            root.right = build(mid + 1, hi)  # then the right half
            return root

        return build(0, n - 1)
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
- [108. Convert Sorted Array to Binary Search Tree](../../0001-0500/0108-convert-sorted-array-to-binary-search-tree/)
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)
- [99. Recover Binary Search Tree](../../0001-0500/0099-recover-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)
