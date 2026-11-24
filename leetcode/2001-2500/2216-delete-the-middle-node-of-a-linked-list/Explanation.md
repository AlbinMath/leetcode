# LeetCode 2095: Delete the Middle Node of a Linked List

**LeetCode Problem #2095 — Delete the Middle Node of a Linked List**
Solve LeetCode Delete the Middle Node of a Linked List using Java, JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete the Middle Node of a Linked List |
| LeetCode | #2095 |
| Difficulty | Medium |
| Language | Java, JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `head` of a linked list. **Delete** the **middle node**, and return *the* `head` *of the modified linked list*.

The **middle node** of a linked list of size `n` is the `&lfloor;n / 2&rfloor;^th` node from the start using **0-based indexing**, where `&lfloor;x&rfloor;` denotes the largest integer less than or equal to `x`.

For `n` = `1`, `2`, `3`, `4`, and `5`, the middle nodes are `0`, `1`, `1`, `2`, and `2`, respectively.

## Constraints
- The number of nodes in the list is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `head = [1,3,4,7,1,2,6]`
- **Output:** `[1,3,4,1,2,6]`
- **Explanation:** The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.

### Example 2
- **Input:** `head = [1,2,3,4]`
- **Output:** `[1,2,4]`
- **Explanation:** The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

### Example 3
- **Input:** `head = [2,1]`
- **Output:** `[2]`
- **Explanation:** The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Use **fast and slow pointers**. Fast moves 2 steps while slow moves 1. When fast reaches the end, slow is just before the middle. Delete the middle by setting `slow.next = slow.next.next`.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Pointer**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,3,4,7,1,2,6]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,4,1,2,6]`.
4. **Verification:** The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
Java, JavaScript

## Source Code
- [solution.java](./solution.java)
- [solution.js](./solution.js)


### Java
```java
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        // If there is only one node
        if (head.next == null) {
            return null;
        }

        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;

        // Find the middle node
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        // Delete the middle node
        prev.next = slow.next;

        return head;
    }
}
```

### JavaScript
```javascript
var deleteMiddle = function(head) {
    if (head === null || head.next === null) {
        return null;
    }

    let slow = head;
    let fast = head;
    let prev = null;

    while (fast !== null && fast.next !== null) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }

    prev.next = slow.next;

    return head;
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
- [237. Delete Node in a Linked List](../../0001-0500/0237-delete-node-in-a-linked-list/)
- [382. Linked List Random Node](../../0001-0500/0382-linked-list-random-node/)
- [876. Middle of the Linked List](../../0501-1000/0908-middle-of-the-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)
