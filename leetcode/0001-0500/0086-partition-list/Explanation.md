# LeetCode 86: Partition List

**LeetCode Problem #86 — Partition List**
Solve LeetCode Partition List using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition List |
| LeetCode | #86 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a linked list and a value `x`, partition it such that all nodes **less than** `x` come before nodes **greater than or equal** to `x`.

You should **preserve** the original relative order of the nodes in each of the two partitions.

## Constraints
- The number of nodes in the list is in the range `[0, 200]`.
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

## Examples
### Example 1
- **Input:** `head = [1,4,3,2,5,2], x = 3`
- **Output:** `[1,2,2,4,3,5]`

### Example 2
- **Input:** `head = [2,1], x = 2`
- **Output:** `[1,2]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Partition List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,4,3,2,5,2], x = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,2,4,3,5]`.

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
var partition = function(head, x) {
    const lessHead = new ListNode(0);
    const greaterHead = new ListNode(0);

    let less = lessHead;
    let greater = greaterHead;

    while (head !== null) {
        if (head.val < x) {
            less.next = head;
            less = less.next;
        } else {
            greater.next = head;
            greater = greater.next;
        }

        head = head.next;
    }

    // Terminate the greater list
    greater.next = null;

    // Connect both partitions
    less.next = greaterHead.next;

    return lessHead.next;
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
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)
- [561. Array Partition](../../0501-1000/0561-array-partition/)
- [698. Partition to K Equal Sum Subsets](../../0501-1000/0698-partition-to-k-equal-sum-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-list/)
