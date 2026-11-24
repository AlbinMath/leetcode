# LeetCode 203: Remove Linked List Elements

**LeetCode Problem #203 — Remove Linked List Elements**
Solve LeetCode Remove Linked List Elements using PHP and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Linked List Elements |
| LeetCode | #203 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return *the new head*.

## Constraints
- The number of nodes in the list is in the range `[0, 10^4]`.
- `1 <= Node.val <= 50`
- `0 <= val <= 50`

## Examples
### Example 1
- **Input:** `head = [1,2,6,3,4,5,6], val = 6`
- **Output:** `[1,2,3,4,5]`

### Example 2
- **Input:** `head = [], val = 1`
- **Output:** `[]`

### Example 3
- **Input:** `head = [7,7,7,7], val = 7`
- **Output:** `[]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Remove Linked List Elements**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,6,3,4,5,6], val = 6`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,4,5]`.

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
PHP

## Source Code
- [solution.php](./solution.php)


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
    function removeElements($head, $val) {
        // Dummy node handles deletion of the head
        $dummy = new ListNode(0);
        $dummy->next = $head;

        $current = $dummy;

        while ($current->next !== null) {
            if ($current->next->val == $val) {
                // Remove the next node
                $current->next = $current->next->next;
            } else {
                $current = $current->next;
            }
        }

        return $dummy->next;
    }
}
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
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-linked-list-elements/)
