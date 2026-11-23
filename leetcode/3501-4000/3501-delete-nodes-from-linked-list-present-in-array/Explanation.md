# LeetCode 3217: Delete Nodes From Linked List Present in Array

**LeetCode Problem #3217 — Delete Nodes From Linked List Present in Array**
Solve LeetCode Delete Nodes From Linked List Present in Array using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Nodes From Linked List Present in Array |
| LeetCode | #3217 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums` and the `head` of a linked list. Return the `head` of the modified linked list after **removing** all nodes from the linked list that have a value that exists in `nums`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- All elements in `nums` are unique.
- The number of nodes in the given list is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`
- The input is generated such that there is at least one node in the linked list that has a value not present in `nums`.

## Examples
### Example 1
- **Input:** `nums = [1,2,3], head = [1,2,3,4,5]`
- **Output:** `[4,5]`

### Example 2
- **Input:** `nums = [1], head = [1,2,1,2,1,2]`
- **Output:** `[2,2,2]`
- **Explanation:** Remove the nodes with value 1.

### Example 3
- **Input:** `nums = [5], head = [1,2,3,4]`
- **Output:** `[1,2,3,4]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Delete Nodes From Linked List Present in Array**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], head = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,5]`.

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
var modifiedList = function(nums, head) {

    // Step 1: Store nums in a Set
    let set = new Set(nums);

    // Step 2: Create a dummy node
    let dummy = new ListNode(0);
    dummy.next = head;

    let current = dummy;

    // Step 3: Traverse and delete matching nodes
    while (current.next) {

        if (set.has(current.next.val)) {
            // Skip the node
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }

    return dummy.next;
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
- [1171. Remove Zero Sum Consecutive Nodes from Linked List](../../1001-1500/1267-remove-zero-sum-consecutive-nodes-from-linked-list/)
- [2487. Remove Nodes From Linked List](../../2501-3000/2573-remove-nodes-from-linked-list/)
- [237. Delete Node in a Linked List](../../0001-0500/0237-delete-node-in-a-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/)
