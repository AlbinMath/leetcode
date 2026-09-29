# Remove Nth Node From End Of List

## Problem Explanation
Given the `head` of a linked list, remove the `n`th node from the **end** of the list and return the head of the modified list.

For example, if the list is `[1, 2, 3, 4, 5]` and `n = 2`:
- The 2nd node from the end is `4`.
- After removing it, the list becomes `[1, 2, 3, 5]`.

## How the Code Works
The code uses the **Two Pointer (Fast & Slow)** technique to find the target node in a single pass.

1. **Dummy Node:** A `dummy` node is created before the `head`. This handles the edge case where the head itself needs to be removed.
2. **Advance Fast Pointer:** The `fast` pointer is moved `n` steps ahead from `dummy`.
3. **Move Both Pointers:** Both `fast` and `slow` are moved one step at a time until `fast.next` becomes `null`. At this point, `slow` is exactly one node **before** the node that needs to be removed.
4. **Remove the Node:** The target node is skipped by setting `slow.next = slow.next.next`.
5. It returns `dummy.next`, which is the new head of the list.

Time complexity is $O(L)$ where $L$ is the length of the list. Space complexity is $O(1)$.
