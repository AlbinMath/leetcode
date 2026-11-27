# LeetCode 147: Insertion Sort List

**LeetCode Problem #147 — Insertion Sort List**
Solve LeetCode Insertion Sort List using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Insertion Sort List |
| LeetCode | #147 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a singly linked list, sort the list using **insertion sort**, and return *the sorted list's head*.

The steps of the **insertion sort** algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list. 
 At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there. 
 It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

## Constraints
- The number of nodes in the list is in the range `[1, 5000]`.
- `-5000 <= Node.val <= 5000`

## Examples
### Example 1
- **Input:** `head = [4,2,1,3]`
- **Output:** `[1,2,3,4]`

### Example 2
- **Input:** `head = [-1,5,3,4,0]`
- **Output:** `[-1,0,3,4,5]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Insertion Sort List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [4,2,1,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,4]`.

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
    def insertionSortList(self, head):
        dummy = ListNode(0)
        while head:
            cur = dummy
            while cur.next and cur.next.val <= head.val:
                cur = cur.next
            nxt = head.next
            head.next = cur.next
            cur.next = head
            head = nxt
        return dummy.next
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
- [148. Sort List](../../0001-0500/0148-sort-list/)
- [19. Remove Nth Node From End of List](../../0001-0500/0019-remove-nth-node-from-end-of-list/)
- [61. Rotate List](../../0001-0500/0061-rotate-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/insertion-sort-list/)
