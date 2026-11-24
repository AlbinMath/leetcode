# LeetCode 1609: Even Odd Tree

**LeetCode Problem #1609 — Even Odd Tree**
Solve LeetCode Even Odd Tree using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Even Odd Tree |
| LeetCode | #1609 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A binary tree is named **Even-Odd** if it meets the following conditions:

The root of the binary tree is at level index `0`, its children are at level index `1`, their children are at level index `2`, etc. 
 For every **even-indexed** level, all nodes at the level have **odd** integer values in **strictly increasing** order (from left to right). 
 For every odd-indexed level, all nodes at the level have even integer values in **strictly decreasing** order (from left to right).

Given the `root` of a binary tree, *return *`true`* if the binary tree is **Even-Odd**, otherwise return *`false`*.*

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^6`

## Examples
### Example 1
- **Input:** `root = [1,10,4,3,null,7,9,12,8,6,null,null,2]`
- **Output:** `true`
- **Explanation:** The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

### Example 2
- **Input:** `root = [5,4,2,3,3,7]`
- **Output:** `false`
- **Explanation:** The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.

### Example 3
- **Input:** `root = [5,9,1,3,5,7]`
- **Output:** `false`
- **Explanation:** Node values in the level 1 should be even integers.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Even Odd Tree**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,10,4,3,null,7,9,12,8,6,null,null,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

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
from collections import deque
from typing import Optional
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            prev = 0 if level % 2 == 0 else float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                v = node.val
                if level % 2 == 0:
                    if v % 2 == 0 or v <= prev:
                        return False
                else:
                    if v % 2 == 1 or v >= prev:
                        return False
                prev = v
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True
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
- [2415. Reverse Odd Levels of Binary Tree](../../2001-2500/2415-reverse-odd-levels-of-binary-tree/)
- [328. Odd Even Linked List](../../0001-0500/0328-odd-even-linked-list/)
- [975. Odd Even Jump](../../0501-1000/0975-odd-even-jump/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/even-odd-tree/)
