# LeetCode 1026: Maximum Difference Between Node and Ancestor

**LeetCode Problem #1026 — Maximum Difference Between Node and Ancestor**
Solve LeetCode Maximum Difference Between Node and Ancestor using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Difference Between Node and Ancestor |
| LeetCode | #1026 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, find the maximum value `v` for which there exist **different** nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`.

A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any child of `a` is an ancestor of `b`.

## Constraints
- The number of nodes in the tree is in the range `[2, 5000]`.
- `0 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `root = [8,3,10,1,6,null,14,null,null,4,7,13]`
- **Output:** `7`
- **Explanation:** We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

### Example 2
- **Input:** `root = [1,null,2,null,0,3]`
- **Output:** `3`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Difference Between Node and Ancestor**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [8,3,10,1,6,null,14,null,null,4,7,13]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

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
from typing import Optional

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, root.val, root.val)]  # (node, path min, path max)
        while stack:
            node, lo, hi = stack.pop()
            lo = min(lo, node.val)
            hi = max(hi, node.val)
            ans = max(ans, hi - lo)
            if node.left:
                stack.append((node.left, lo, hi))
            if node.right:
                stack.append((node.right, lo, hi))
        return ans
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
- [1913. Maximum Product Difference Between Two Pairs](../../1501-2000/1913-maximum-product-difference-between-two-pairs/)
- [3442. Maximum Difference Between Even and Odd Frequency I](../../3001-3500/3442-maximum-difference-between-even-and-odd-frequency-i/)
- [3445. Maximum Difference Between Even and Odd Frequency II](../../3001-3500/3445-maximum-difference-between-even-and-odd-frequency-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/)
