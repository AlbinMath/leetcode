# LeetCode 2: Add Two Numbers

**LeetCode Problem #2 — Add Two Numbers**
Solve LeetCode Add Two Numbers using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Add Two Numbers |
| LeetCode | #2 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Constraints
- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Examples
### Example 1
- **Input:** `l1 = [2,4,3], l2 = [5,6,4]`
- **Output:** `[7,0,8]`
- **Explanation:** 342 + 465 = 807.

### Example 2
- **Input:** `l1 = [0], l2 = [0]`
- **Output:** `[0]`

### Example 3
- **Input:** `l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]`
- **Output:** `[8,9,9,9,0,0,0,1]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
The code uses a simulated digit-by-digit addition, similar to how you would add numbers on paper:
1. It initializes a `dummy` node to act as the head of the result list, and a `current` pointer to build the new list.
2. It uses a `carry` variable (initially 0) to keep track of values that carry over to the next place value (e.g., if sum >= 10).
3. A `while` loop runs as long as there is a node in `l1`, a node in `l2`, or a remaining `carry` greater than 0.
4. Inside the loop, it safely extracts the values from `l1` and `l2` (defaulting to 0 if one list is shorter than the other).
5. It calculates the `total` sum for the current position (`val1 + val2 + carry`).
6. The `digit` to store in the new node is `total % 10`, and the new `carry` for the next iteration is `total // 10`.
7. It creates a new node with this `digit`, attaches it to the result list, and moves all pointers (`l1`, `l2`, and `current`) forward.
8. Finally, it returns `dummy.next`, which is the head of the newly constructed sum list.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `l1 = [2,4,3], l2 = [5,6,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[7,0,8]`.
4. **Verification:** 342 + 465 = 807.

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
var addTwoNumbers = function(l1, l2) {
    const dummy = new ListNode(0);
    let current = dummy;
    let carry = 0;

    while (l1 !== null || l2 !== null || carry > 0) {
        const x = l1 !== null ? l1.val : 0;
        const y = l2 !== null ? l2.val : 0;

        const sum = x + y + carry;
        carry = Math.floor(sum / 10);

        current.next = new ListNode(sum % 10);
        current = current.next;

        if (l1 !== null) l1 = l1.next;
        if (l2 !== null) l2 = l2.next;
    }

    return dummy.next;
};
```

### Python
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values from the two lists
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add values + carry
            total = val1 + val2 + carry

            # Calculate digit and carry
            digit = total % 10
            carry = total // 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

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
- [445. Add Two Numbers II](../../0001-0500/0445-add-two-numbers-ii/)
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [2723. Add Two Promises](../../2501-3000/2723-add-two-promises/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/add-two-numbers/)
