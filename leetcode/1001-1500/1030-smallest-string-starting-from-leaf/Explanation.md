# LeetCode 988: Smallest String Starting From Leaf

**LeetCode Problem #988 — Smallest String Starting From Leaf**
Solve LeetCode Smallest String Starting From Leaf using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest String Starting From Leaf |
| LeetCode | #988 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a binary tree where each node has a value in the range `[0, 25]` representing the letters `'a'` to `'z'`.

Return *the **lexicographically smallest** string that starts at a leaf of this tree and ends at the root*.

As a reminder, any shorter prefix of a string is **lexicographically smaller**.

For example, `"ab"` is lexicographically smaller than `"aba"`.

A leaf of a node is a node that has no children.

## Constraints
- The number of nodes in the tree is in the range `[1, 8500]`.
- `0 <= Node.val <= 25`

## Examples
### Example 1
- **Input:** `root = [0,1,2,3,4,3,4]`
- **Output:** `"dba"`

### Example 2
- **Input:** `root = [25,1,3,1,3,0,2]`
- **Output:** `"adz"`

### Example 3
- **Input:** `root = [2,2,1,null,1,0,null,0]`
- **Output:** `"abc"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Smallest String Starting From Leaf**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [0,1,2,3,4,3,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"dba"`.

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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        best = None

        def dfs(node, suffix: str) -> None:
            nonlocal best
            if not node:
                return
            cur = chr(node.val + 97) + suffix  # prepend: path now reads node -> root
            if not node.left and not node.right:
                if best is None or cur < best:
                    best = cur
                return
            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, "")
        return best
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
- [2375. Construct Smallest Number From DI String](../../2001-2500/2456-construct-smallest-number-from-di-string/)
- [606. Construct String from Binary Tree](../../0501-1000/0606-construct-string-from-binary-tree/)
- [1061. Lexicographically Smallest Equivalent String](../../1001-1500/1058-lexicographically-smallest-equivalent-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-string-starting-from-leaf/)
