# LeetCode 206: Reverse Linked List

**LeetCode Problem #206 — Reverse Linked List**
Solve LeetCode Reverse Linked List using JavaScript, PHP, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Linked List |
| LeetCode | #206 |
| Difficulty | Easy |
| Language | JavaScript, PHP, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

## Constraints
- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

## Examples
### Example 1
- **Input:** `head = [1,2,3,4,5]`
- **Output:** `[5,4,3,2,1]`

### Example 2
- **Input:** `head = [1,2]`
- **Output:** `[2,1]`

### Example 3
- **Input:** `head = []`
- **Output:** `[]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Reverse Linked List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

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
3. **Result:** Arrive at the expected output `[5,4,3,2,1]`.

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
JavaScript, PHP, Python

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)
- [solution.py](./solution.py)


### JavaScript
```javascript
var reverseList = function(head) {
    let prev = null;
    let curr = head;

    while (curr !== null) {
        let nextNode = curr.next; // Save the next node
        curr.next = prev;         // Reverse the link
        prev = curr;              // Move prev forward
        curr = nextNode;          // Move curr forward
    }

    return prev;
};
```

### PHP
```php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */

class Solution {
    function reverseList($head) {
        $prev = null;
        $current = $head;

        while ($current !== null) {
            // Save the next node
            $next = $current->next;

            // Reverse the link
            $current->next = $prev;

            // Move prev forward
            $prev = $current;

            // Move current forward
            $current = $next;
        }

        return $prev;
    }
}
```

### Python
```python
class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
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
[View problem on LeetCode](https://leetcode.com/problems/reverse-linked-list/)
