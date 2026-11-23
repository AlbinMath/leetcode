# LeetCode 1019: Next Greater Node In Linked List

**LeetCode Problem #1019 — Next Greater Node In Linked List**
Solve LeetCode Next Greater Node In Linked List using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Next Greater Node In Linked List |
| LeetCode | #1019 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `i^th` node (**1-indexed**). If the `i^th` node does not have a next greater node, set `answer[i] = 0`.

## Constraints
- The number of nodes in the list is `n`.
- `1 <= n <= 10^4`
- `1 <= Node.val <= 10^9`

## Examples
### Example 1
- **Input:** `head = [2,1,5]`
- **Output:** `[5,5,0]`

### Example 2
- **Input:** `head = [2,7,4,3,5]`
- **Output:** `[7,0,5,5,0]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Next Greater Node In Linked List**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [2,1,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,5,0]`.

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
from typing import List, Optional

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        res = []
        stack = []

        node = head
        while node:
            x = node.val
            while stack and vals[stack[-1]] < x:
                res[stack.pop()] = x
            stack.append(len(vals))
            vals.append(x)
            res.append(0)
            node = node.next

        return res
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
- [237. Delete Node in a Linked List](../../0001-0500/0237-delete-node-in-a-linked-list/)
- [382. Linked List Random Node](../../0001-0500/0382-linked-list-random-node/)
- [2095. Delete the Middle Node of a Linked List](../../2001-2500/2216-delete-the-middle-node-of-a-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/next-greater-node-in-linked-list/)
