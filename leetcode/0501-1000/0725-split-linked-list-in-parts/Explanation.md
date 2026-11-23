# LeetCode 725: Split Linked List in Parts

**LeetCode Problem #725 — Split Linked List in Parts**
Solve LeetCode Split Linked List in Parts using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Linked List in Parts |
| LeetCode | #725 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a singly linked list and an integer `k`, split the linked list into `k` consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return *an array of the *`k`* parts*.

## Constraints
- The number of nodes in the list is in the range `[0, 1000]`.
- `0 <= Node.val <= 1000`
- `1 <= k <= 50`

## Examples
### Example 1
- **Input:** `head = [1,2,3], k = 5`
- **Output:** `[[1],[2],[3],[],[]]`
- **Explanation:** The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

### Example 2
- **Input:** `head = [1,2,3,4,5,6,7,8,9,10], k = 3`
- **Output:** `[[1,2,3,4],[5,6,7],[8,9,10]]`
- **Explanation:** The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Split Linked List in Parts**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,3], k = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1],[2],[3],[],[]]`.
4. **Verification:** The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

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
var splitListToParts = function(head, k) {
    // Step 1: Count total nodes
    let length = 0;
    let current = head;

    while (current) {
        length++;
        current = current.next;
    }

    // Step 2: Calculate part sizes
    let size = Math.floor(length / k);
    let extra = length % k;

    let result = [];
    current = head;

    // Step 3: Split into k parts
    for (let i = 0; i < k; i++) {
        let partHead = current;
        let partSize = size + (i < extra ? 1 : 0);

        // Move to the end of the current part
        for (let j = 0; j < partSize - 1; j++) {
            if (current) {
                current = current.next;
            }
        }

        // Separate the current part
        if (current) {
            let nextPart = current.next;
            current.next = null;
            current = nextPart;
        }

        result.push(partHead);
    }

    return result;
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
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)
- [141. Linked List Cycle](../../0001-0500/0141-linked-list-cycle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-linked-list-in-parts/)
