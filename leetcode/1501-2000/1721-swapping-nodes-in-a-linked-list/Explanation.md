# LeetCode 1721: Swapping Nodes in a Linked List

**LeetCode Problem #1721 — Swapping Nodes in a Linked List**
Solve LeetCode Swapping Nodes in a Linked List using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Swapping Nodes in a Linked List |
| LeetCode | #1721 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `head` of a linked list, and an integer `k`.

Return *the head of the linked list after **swapping** the values of the *`k^th` *node from the beginning and the *`k^th` *node from the end (the list is **1-indexed**).*

## Constraints
- The number of nodes in the list is `n`.
- `1 <= k <= n <= 10^5`
- `0 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `head = [1,2,3,4,5], k = 2`
- **Output:** `[1,4,3,2,5]`

### Example 2
- **Input:** `head = [7,9,6,6,7,8,3,0,9,5], k = 5`
- **Output:** `[7,9,6,6,8,7,3,0,9,5]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Swapping Nodes in a Linked List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,3,4,5], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,4,3,2,5]`.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var swapNodes = function(head, k) {
    let first = head;

    // Step 1: Find kth node from beginning
    for (let i = 1; i < k; i++) {
        first = first.next;
    }

    // Save kth node from beginning
    let node1 = first;

    // Step 2: Find kth node from end
    let second = head;
    let current = first;

    while (current.next) {
        current = current.next;
        second = second.next;
    }

    // Step 3: Swap values
    let temp = node1.val;
    node1.val = second.val;
    second.val = temp;

    return head;
};
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
- [1171. Remove Zero Sum Consecutive Nodes from Linked List](../../1001-1500/1171-remove-zero-sum-consecutive-nodes-from-linked-list/)
- [2487. Remove Nodes From Linked List](../../2001-2500/2487-remove-nodes-from-linked-list/)
- [3217. Delete Nodes From Linked List Present in Array](../../3001-3500/3217-delete-nodes-from-linked-list-present-in-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)
