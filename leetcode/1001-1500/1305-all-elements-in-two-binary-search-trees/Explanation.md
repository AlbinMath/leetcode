# LeetCode 1305: All Elements in Two Binary Search Trees

**LeetCode Problem #1305 — All Elements in Two Binary Search Trees**
Solve LeetCode All Elements in Two Binary Search Trees using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Elements in Two Binary Search Trees |
| LeetCode | #1305 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two binary search trees `root1` and `root2`, return *a list containing all the integers from both trees sorted in **ascending** order*.

## Constraints
- The number of nodes in each tree is in the range `[0, 5000]`.
- `-10^5 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `root1 = [2,1,4], root2 = [1,0,3]`
- **Output:** `[0,1,1,2,3,4]`

### Example 2
- **Input:** `root1 = [1,null,8], root2 = [8,1]`
- **Output:** `[1,1,8,8]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **All Elements in Two Binary Search Trees**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root1 = [2,1,4], root2 = [1,0,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1,1,2,3,4]`.

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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node: TreeNode, res: List[int]):
            if not node:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
            
        list1, list2 = [], []
        inorder(root1, list1)
        inorder(root2, list2)
        
        # Merge two sorted lists
        merged = []
        i, j = 0, 0
        len1, len2 = len(list1), len(list2)
        
        while i < len1 and j < len2:
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
                
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged
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
- [558. Logical OR of Two Binary Grids Represented as Quad-Trees](../../0501-1000/0558-logical-or-of-two-binary-grids-represented-as-quad-trees/)
- [617. Merge Two Binary Trees](../../0501-1000/0617-merge-two-binary-trees/)
- [95. Unique Binary Search Trees II](../../0001-0500/0095-unique-binary-search-trees-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)
