# LeetCode 82: Remove Duplicates from Sorted List II

**LeetCode Problem #82 — Remove Duplicates from Sorted List II**
Solve LeetCode Remove Duplicates from Sorted List II using PHP and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Duplicates from Sorted List II |
| LeetCode | #82 |
| Difficulty | Medium |
| Language | PHP |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `head` of a **sorted** linked list.

Delete all nodes that have **duplicate** numbers, leaving only **distinct** numbers from the original list.

Return the linked list **sorted** as well.

## Constraints
- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.

## Examples
### Example 1
- **Input:** `head = [1,2,3,3,4,4,5]`
- **Output:** `[1,2,5]`

### Example 2
- **Input:** `head = [1,1,1,2,3]`
- **Output:** `[2,3]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Remove Duplicates from Sorted List II**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,3,3,4,4,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,5]`.

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
class Solution {
    function deleteDuplicates($head) {
        // Dummy node handles duplicates at the beginning
        $dummy = new ListNode(0);
        $dummy->next = $head;

        $prev = $dummy;
        $current = $head;

        while ($current !== null) {

            // Check if current node has duplicates
            if ($current->next !== null &&
                $current->val == $current->next->val) {

                $duplicateValue = $current->val;

                // Skip all nodes with this value
                while ($current !== null &&
                       $current->val == $duplicateValue) {
                    $current = $current->next;
                }

                // Connect previous distinct node
                $prev->next = $current;

            } else {
                // Current node is unique
                $prev = $current;
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
- [83. Remove Duplicates from Sorted List](../../0001-0500/0083-remove-duplicates-from-sorted-list/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](../../0001-0500/0080-remove-duplicates-from-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)
