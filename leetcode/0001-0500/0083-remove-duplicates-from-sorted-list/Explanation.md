# LeetCode 83: Remove Duplicates from Sorted List

**LeetCode Problem #83 — Remove Duplicates from Sorted List**
Solve LeetCode Remove Duplicates from Sorted List using PHP, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Duplicates from Sorted List |
| LeetCode | #83 |
| Difficulty | Easy |
| Language | PHP, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return *the linked list **sorted** as well*.

## Constraints
- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.

## Examples
### Example 1
- **Input:** `head = [1,1,2]`
- **Output:** `[1,2]`

### Example 2
- **Input:** `head = [1,1,2,3,3]`
- **Output:** `[1,2,3]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Remove Duplicates from Sorted List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,1,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.

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
PHP, Python

## Source Code
- [solution.php](./solution.php)
- [solution.py](./solution.py)


### PHP
```php
class Solution {
    function deleteDuplicates($head) {
        $current = $head;

        while ($current !== null && $current->next !== null) {

            if ($current->val == $current->next->val) {
                // Skip duplicate node
                $current->next = $current->next->next;
            } else {
                // Move to next node
                $current = $current->next;
            }
        }

        return $head;
    }
}
```

### Python
```python
class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
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
- [82. Remove Duplicates from Sorted List II](../../0001-0500/0082-remove-duplicates-from-sorted-list-ii/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](../../0001-0500/0080-remove-duplicates-from-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
