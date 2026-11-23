# LeetCode 1379: Find a Corresponding Node of a Binary Tree in a Clone of That Tree

**LeetCode Problem #1379 — Find a Corresponding Node of a Binary Tree in a Clone of That Tree**
Solve LeetCode Find a Corresponding Node of a Binary Tree in a Clone of That Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find a Corresponding Node of a Binary Tree in a Clone of That Tree |
| LeetCode | #1379 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two binary trees `original` and `cloned` and given a reference to a node `target` in the original tree.

The `cloned` tree is a **copy of** the `original` tree.

Return *a reference to the same node* in the `cloned` tree.

**Note** that you are **not allowed** to change any of the two trees or the `target` node and the answer **must be** a reference to a node in the `cloned` tree.

## Constraints
- The number of nodes in the `tree` is in the range `[1, 10^4]`.
- The values of the nodes of the `tree` are unique.
- `target` node is a node from the `original` tree and is not `null`.

## Examples
### Example 1
- **Input:** `tree = [7,4,3,null,null,6,19], target = 3`
- **Output:** `3`
- **Explanation:** In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

### Example 2
- **Input:** `tree = [7], target = 7`
- **Output:** `7`

### Example 3
- **Input:** `tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4`
- **Output:** `4`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find a Corresponding Node of a Binary Tree in a Clone of That Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tree = [7,4,3,null,null,6,19], target = 3`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

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
    def getTargetCopy(self, original, cloned, target):
        if original is None:
            return None

        if original is target:
            return cloned

        left = self.getTargetCopy(
            original.left, cloned.left, target
        )

        if left is not None:
            return left

        return self.getTargetCopy(
            original.right, cloned.right, target
        )
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
- [501. Find Mode in Binary Search Tree](../../0501-1000/0501-find-mode-in-binary-search-tree/)
- [1261. Find Elements in a Contaminated Binary Tree](../../1001-1500/1387-find-elements-in-a-contaminated-binary-tree/)
- [3585. Find Weighted Median Node in Tree](../../3501-4000/3900-find-weighted-median-node-in-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
