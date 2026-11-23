# LeetCode 237: Delete Node in a Linked List

**LeetCode Problem #237 — Delete Node in a Linked List**
Solve LeetCode Delete Node in a Linked List using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Node in a Linked List |
| LeetCode | #237 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a singly-linked list `head` and we want to delete a node `node` in it.

You are given the node to be deleted `node`. You will **not be given access** to the first node of `head`.

All the values of the linked list are **unique**, and it is guaranteed that the given node `node` is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list. 
 The number of nodes in the linked list should decrease by one. 
 All the values before `node` should be in the same order. 
 All the values after `node` should be in the same order.

**Custom testing:**

For the input, you should provide the entire linked list `head` and the node to be given `node`. `node` should not be the last node of the list and should be an actual node in the list. 
 We will build the linked list and pass the node to your function. 
 The output will be the entire list after calling your function.

## Constraints
- The number of the nodes in the given list is in the range `[2, 1000]`.
- `-1000 <= Node.val <= 1000`
- The value of each node in the list is **unique**.
- The `node` to be deleted is **in the list** and is **not a tail** node.

## Examples
### Example 1
- **Input:** `head = [4,5,1,9], node = 5`
- **Output:** `[4,1,9]`
- **Explanation:** You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

### Example 2
- **Input:** `head = [4,5,1,9], node = 1`
- **Output:** `[4,5,9]`
- **Explanation:** You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Delete Node in a Linked List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [4,5,1,9], node = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,1,9]`.
4. **Verification:** You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

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
var deleteNode = function(node) {
    node.val = node.next.val;
    node.next = node.next.next;
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
- [2095. Delete the Middle Node of a Linked List](../../2001-2500/2216-delete-the-middle-node-of-a-linked-list/)
- [3217. Delete Nodes From Linked List Present in Array](../../3501-4000/3501-delete-nodes-from-linked-list-present-in-array/)
- [382. Linked List Random Node](../../0001-0500/0382-linked-list-random-node/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-node-in-a-linked-list/)
