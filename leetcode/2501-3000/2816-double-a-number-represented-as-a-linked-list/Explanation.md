# LeetCode 2816: Double a Number Represented as a Linked List

**LeetCode Problem #2816 — Double a Number Represented as a Linked List**
Solve LeetCode Double a Number Represented as a Linked List using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Double a Number Represented as a Linked List |
| LeetCode | #2816 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `head` of a **non-empty** linked list representing a non-negative integer without leading zeroes.

Return *the *`head`* of the linked list after **doubling** it*.

## Constraints
- The number of nodes in the list is in the range `[1, 10^4]`
- `0 <= Node.val <= 9`
- The input is generated such that the list represents a number that does not have leading zeros, except the number `0` itself.

## Examples
### Example 1
- **Input:** `head = [1,8,9]`
- **Output:** `[3,7,8]`
- **Explanation:** The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

### Example 2
- **Input:** `head = [9,9,9]`
- **Output:** `[1,9,9,8]`
- **Explanation:** The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Double a Number Represented as a Linked List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,8,9]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,7,8]`.
4. **Verification:** The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

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
var doubleIt = function(head) {

    function reverse(node) {
        let prev = null;
        let current = node;

        while (current) {
            let nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }

        return prev;
    }

    // Reverse the linked list
    head = reverse(head);

    let current = head;
    let carry = 0;

    // Double each digit
    while (current) {
        let sum = current.val * 2 + carry;

        current.val = sum % 10;
        carry = Math.floor(sum / 10);

        if (!current.next && carry > 0) {
            current.next = new ListNode(carry);
            break; // Important: don't process the new node again
        }

        current = current.next;
    }

    // Reverse back
    return reverse(head);
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
- [1290. Convert Binary Number in a Linked List to Integer](../../1001-1500/1290-convert-binary-number-in-a-linked-list-to-integer/)
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/)
