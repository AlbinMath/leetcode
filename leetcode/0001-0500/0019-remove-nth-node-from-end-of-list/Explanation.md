# LeetCode 19: Remove Nth Node From End of List

**LeetCode Problem #19 — Remove Nth Node From End of List**
Solve LeetCode Remove Nth Node From End of List using JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Nth Node From End of List |
| LeetCode | #19 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a linked list, remove the `n^th` node from the end of the list and return its head.

## Constraints
- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Examples
### Example 1
- **Input:** `head = [1,2,3,4,5], n = 2`
- **Output:** `[1,2,3,5]`

### Example 2
- **Input:** `head = [1], n = 1`
- **Output:** `[]`

### Example 3
- **Input:** `head = [1,2], n = 1`
- **Output:** `[1]`

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses the **Two Pointer (Fast & Slow)** technique to find the target node in a single pass.

1. **Dummy Node:** A `dummy` node is created before the `head`. This handles the edge case where the head itself needs to be removed.
2. **Advance Fast Pointer:** The `fast` pointer is moved `n` steps ahead from `dummy`.
3. **Move Both Pointers:** Both `fast` and `slow` are moved one step at a time until `fast.next` becomes `null`. At this point, `slow` is exactly one node **before** the node that needs to be removed.
4. **Remove the Node:** The target node is skipped by setting `slow.next = slow.next.next`.
5. It returns `dummy.next`, which is the new head of the list.

Time complexity is $O(L)$ where $L$ is the length of the list. Space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Pointer**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,3,4,5], n = 2`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,5]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var removeNthFromEnd = function(head, n) {
    const dummy = new ListNode(0);
    dummy.next = head;

    let fast = dummy;
    let slow = dummy;

    // Move fast n + 1 steps ahead
    for (let i = 0; i <= n; i++) {
        fast = fast.next;
    }

    // Move both pointers until fast reaches the end
    while (fast !== null) {
        fast = fast.next;
        slow = slow.next;
    }

    // Remove the nth node from the end
    slow.next = slow.next.next;

    return dummy.next;
};
```

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [82. Remove Duplicates from Sorted List II](../../0001-0500/0082-remove-duplicates-from-sorted-list-ii/)
- [83. Remove Duplicates from Sorted List](../../0001-0500/0083-remove-duplicates-from-sorted-list/)
- [1171. Remove Zero Sum Consecutive Nodes from Linked List](../../1001-1500/1267-remove-zero-sum-consecutive-nodes-from-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
