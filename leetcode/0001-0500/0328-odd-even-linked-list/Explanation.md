# LeetCode 328: Odd Even Linked List

**LeetCode Problem #328 — Odd Even Linked List**
Solve LeetCode Odd Even Linked List using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Odd Even Linked List |
| LeetCode | #328 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

## Constraints
- The number of nodes in the linked list is in the range `[0, 10^4]`.
- `-10^6 <= Node.val <= 10^6`

## Examples
### Example 1
- **Input:** `head = [1,2,3,4,5]`
- **Output:** `[1,3,5,2,4]`

### Example 2
- **Input:** `head = [2,1,3,5,6,4,7]`
- **Output:** `[2,3,6,7,1,5,4]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Odd Even Linked List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,5,2,4]`.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var oddEvenList = function(head) {
    if (head === null || head.next === null) {
        return head;
    }

    let odd = head;
    let even = head.next;
    let evenHead = even;

    while (even !== null && even.next !== null) {
        odd.next = even.next;
        odd = odd.next;

        even.next = odd.next;
        even = even.next;
    }

    odd.next = evenHead;

    return head;
};
```

### Python
```python
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd, even, evenHead = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
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
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)
- [141. Linked List Cycle](../../0001-0500/0141-linked-list-cycle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/odd-even-linked-list/)
