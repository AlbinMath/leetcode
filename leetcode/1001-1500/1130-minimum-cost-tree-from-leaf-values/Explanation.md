# LeetCode 1130: Minimum Cost Tree From Leaf Values

**LeetCode Problem #1130 — Minimum Cost Tree From Leaf Values**
Solve LeetCode Minimum Cost Tree From Leaf Values using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Tree From Leaf Values |
| LeetCode | #1130 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `arr` of positive integers, consider all binary trees such that:

Each node has either `0` or `2` children; 
 The values of `arr` correspond to the values of each **leaf** in an in-order traversal of the tree. 
 The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.

Among all possible binary trees considered, return *the smallest possible sum of the values of each non-leaf node*. It is guaranteed this sum fits into a **32-bit** integer.

A node is a **leaf** if and only if it has zero children.

## Constraints
- `2 <= arr.length <= 40`
- `1 <= arr[i] <= 15`
- It is guaranteed that the answer fits into a **32-bit** signed integer (i.e., it is less than 2^31).

## Examples
### Example 1
- **Input:** `arr = [6,2,4]`
- **Output:** `32`
- **Explanation:** There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

### Example 2
- **Input:** `arr = [4,11]`
- **Output:** `44`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost Tree From Leaf Values**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [6,2,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `32`.
4. **Verification:** There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        cost = 0
        for x in arr:
            while stack[-1] <= x:
                mid = stack.pop()
                cost += mid * min(stack[-1], x)
            stack.append(x)

        while len(stack) > 2:
            cost += stack.pop() * stack[-1]

        return cost
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [988. Smallest String Starting From Leaf](../../0501-1000/0988-smallest-string-starting-from-leaf/)
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](../../0001-0500/0106-construct-binary-tree-from-inorder-and-postorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/)
