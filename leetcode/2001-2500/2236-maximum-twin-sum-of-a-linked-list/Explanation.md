# LeetCode 2130: Maximum Twin Sum of a Linked List

**LeetCode Problem #2130 — Maximum Twin Sum of a Linked List**
Solve LeetCode Maximum Twin Sum of a Linked List using Java, JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Twin Sum of a Linked List |
| LeetCode | #2130 |
| Difficulty | Medium |
| Language | Java, JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
In a linked list of size `n`, where `n` is **even**, the `i^th` node (**0-indexed**) of the linked list is known as the **twin** of the `(n-1-i)^th` node, if `0 <= i <= (n / 2) - 1`.

For example, if `n = 4`, then node `0` is the twin of node `3`, and node `1` is the twin of node `2`. These are the only nodes with twins for `n = 4`.

The **twin sum **is defined as the sum of a node and its twin.

Given the `head` of a linked list with even length, return *the **maximum twin sum** of the linked list*.

## Constraints
- The number of nodes in the list is an **even** integer in the range `[2, 10^5]`.
- `1 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `head = [5,4,2,1]`
- **Output:** `6`
- **Explanation:** Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.

### Example 2
- **Input:** `head = [4,2,2,3]`
- **Output:** `7`
- **Explanation:** The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7.

### Example 3
- **Input:** `head = [1,100000]`
- **Output:** `100001`
- **Explanation:** There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Find the middle using fast/slow pointers, reverse the second half, then iterate both halves simultaneously to compute twin sums and track the maximum.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Pointer**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `head = [5,4,2,1]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.

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
    public int pairSum(ListNode head) {
        // Find middle
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse second half
        ListNode prev = null;
        ListNode curr = slow;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // Calculate maximum twin sum
        int maxSum = 0;
        ListNode first = head;
        ListNode second = prev;

        while (second != null) {
            maxSum = Math.max(maxSum, first.val + second.val);
            first = first.next;
            second = second.next;
        }

        return maxSum;
    }
}
```

### JavaScript
```javascript
var pairSum = function(head) {
    let slow = head;
    let fast = head;

    // Find the middle of the linked list
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Reverse the second half
    let prev = null;
    let curr = slow;

    while (curr !== null) {
        let next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    // Calculate the maximum twin sum
    let left = head;
    let right = prev;
    let maxSum = 0;

    while (right !== null) {
        maxSum = Math.max(maxSum, left.val + right.val);
        left = left.next;
        right = right.next;
    }

    return maxSum;
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
- [1171. Remove Zero Sum Consecutive Nodes from Linked List](../../1001-1500/1267-remove-zero-sum-consecutive-nodes-from-linked-list/)
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)
