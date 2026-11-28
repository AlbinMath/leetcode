# LeetCode 1171: Remove Zero Sum Consecutive Nodes from Linked List

**LeetCode Problem #1171 — Remove Zero Sum Consecutive Nodes from Linked List**
Solve LeetCode Remove Zero Sum Consecutive Nodes from Linked List using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Zero Sum Consecutive Nodes from Linked List |
| LeetCode | #1171 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list. You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

## Constraints
- The given linked list will contain between `1` and `1000` nodes.
- Each node in the linked list has `-1000 <= node.val <= 1000`.

## Examples
### Example 1
- **Input:** `head = [1,2,-3,3,1]`
- **Output:** `[3,1]`

### Example 2
- **Input:** `head = [1,2,3,-3,4]`
- **Output:** `[1,2,4]`

### Example 3
- **Input:** `head = [1,2,3,-3,-2]`
- **Output:** `[1]`

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove Zero Sum Consecutive Nodes from Linked List**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,-3,3,1]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,1]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var removeZeroSumSublists = function(head) {
    // Dummy node handles cases where the head must be removed
    let dummy = new ListNode(0);
    dummy.next = head;

    let map = new Map();
    let sum = 0;
    let current = dummy;

    // First pass: store the last node for each prefix sum
    while (current) {
        sum += current.val;
        map.set(sum, current);
        current = current.next;
    }

    // Second pass: skip zero-sum sequences
    sum = 0;
    current = dummy;

    while (current) {
        sum += current.val;
        current.next = map.get(sum).next;
        current = current.next;
    }

    return dummy.next;
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2487. Remove Nodes From Linked List](../../2001-2500/2487-remove-nodes-from-linked-list/)
- [3217. Delete Nodes From Linked List Present in Array](../../3001-3500/3217-delete-nodes-from-linked-list-present-in-array/)
- [19. Remove Nth Node From End of List](../../0001-0500/0019-remove-nth-node-from-end-of-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)
