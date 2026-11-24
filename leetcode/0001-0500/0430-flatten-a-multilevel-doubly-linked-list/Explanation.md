# LeetCode 430: Flatten a Multilevel Doubly Linked List

**LeetCode Problem #430 — Flatten a Multilevel Doubly Linked List**
Solve LeetCode Flatten a Multilevel Doubly Linked List using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flatten a Multilevel Doubly Linked List |
| LeetCode | #430 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional **child pointer**. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a **multilevel data structure** as shown in the example below.

Given the `head` of the first level of the list, **flatten** the list so that all the nodes appear in a single-level, doubly linked list. Let `curr` be a node with a child list. The nodes in the child list should appear **after** `curr` and **before** `curr.next` in the flattened list.

Return *the *`head`* of the flattened list. The nodes in the list must have **all** of their child pointers set to *`null`.

## Constraints
- The number of Nodes will not exceed `1000`.
- `1 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]`
- **Output:** `[1,2,3,7,8,11,12,9,10,4,5,6]`
- **Explanation:** The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

### Example 2
- **Input:** `head = [1,2,null,3]`
- **Output:** `[1,3,2]`
- **Explanation:** The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

### Example 3
- **Input:** `head = []`
- **Output:** `[]`
- **Explanation:** There could be empty list in the input.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Flatten a Multilevel Doubly Linked List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,7,8,11,12,9,10,4,5,6]`.
4. **Verification:** The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

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
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        stack = []
        curr = head
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            if not curr.next and stack:
                nxt = stack.pop()
                curr.next = nxt
                nxt.prev = curr
            curr = curr.next
        return head
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
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)
- [141. Linked List Cycle](../../0001-0500/0141-linked-list-cycle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)
