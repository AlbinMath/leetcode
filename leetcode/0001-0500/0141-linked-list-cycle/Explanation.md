# LeetCode 141: Linked List Cycle

**LeetCode Problem #141 — Linked List Cycle**
Solve LeetCode Linked List Cycle using JavaScript, PHP, Python and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Linked List Cycle |
| LeetCode | #141 |
| Difficulty | Easy |
| Language | JavaScript, PHP, Python |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true`* if there is a cycle in the linked list*. Otherwise, return `false`.

## Constraints
- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked-list.

## Examples
### Example 1
- **Input:** `head = [3,2,0,-4], pos = 1`
- **Output:** `true`
- **Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

### Example 2
- **Input:** `head = [1,2], pos = 0`
- **Output:** `true`
- **Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

### Example 3
- **Input:** `head = [1], pos = -1`
- **Output:** `false`
- **Explanation:** There is no cycle in the linked list.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Linked List Cycle**, we observe the problem requirements and utilize the **Fast & Slow Pointers** technique. We iterate through the inputs using **Floyd Cycle Detection**, leveraging a **Linked List / Pointer** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Linked List / Pointer**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [3,2,0,-4], pos = 1`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
JavaScript, PHP, Python

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)
- [solution.py](./solution.py)


### JavaScript
```javascript
var hasCycle = function(head) {
    let slow = head;
    let fast = head;

    while (fast !== null && fast.next !== null) {
        slow = slow.next;           // Move one step
        fast = fast.next.next;      // Move two steps

        if (slow === fast) {
            return true;
        }
    }

    return false;
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
    function hasCycle($head) {
        $slow = $head;
        $fast = $head;

        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;

            // Both pointers meet → cycle exists
            if ($slow === $fast) {
                return true;
            }
        }

        // Fast pointer reached the end → no cycle
        return false;
    }
}
```

### Python
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
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
- [142. Linked List Cycle II](../../0001-0500/0142-linked-list-cycle-ii/)
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/linked-list-cycle/)
