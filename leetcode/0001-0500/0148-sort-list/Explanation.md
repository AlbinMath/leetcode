# LeetCode 148: Sort List

**LeetCode Problem #148 — Sort List**
Solve LeetCode Sort List using JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort List |
| LeetCode | #148 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a linked list, return *the list after sorting it in **ascending order***.

## Constraints
- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `head = [4,2,1,3]`
- **Output:** `[1,2,3,4]`

### Example 2
- **Input:** `head = [-1,5,3,4,0]`
- **Output:** `[-1,0,3,4,5]`

### Example 3
- **Input:** `head = []`
- **Output:** `[]`

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sort List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [4,2,1,3]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,4]`.

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
var sortList = function(head) {
    if (head === null || head.next === null) {
        return head;
    }

    // Find the middle and split the list
    let slow = head;
    let fast = head;
    let prev = null;

    while (fast !== null && fast.next !== null) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }

    // Break the list into two halves
    prev.next = null;

    const left = sortList(head);
    const right = sortList(slow);

    // Merge the sorted halves
    return merge(left, right);
};

function merge(left, right) {
    const dummy = new ListNode(0);
    let tail = dummy;

    while (left !== null && right !== null) {
        if (left.val <= right.val) {
            tail.next = left;
            left = left.next;
        } else {
            tail.next = right;
            right = right.next;
        }

        tail = tail.next;
    }

    tail.next = left !== null ? left : right;

    return dummy.next;
}
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
- [147. Insertion Sort List](../../0001-0500/0147-insertion-sort-list/)
- [19. Remove Nth Node From End of List](../../0001-0500/0019-remove-nth-node-from-end-of-list/)
- [61. Rotate List](../../0001-0500/0061-rotate-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-list/)
