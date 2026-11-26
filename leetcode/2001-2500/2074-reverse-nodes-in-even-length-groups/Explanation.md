# LeetCode 2074: Reverse Nodes in Even Length Groups

**LeetCode Problem #2074 — Reverse Nodes in Even Length Groups**
Solve LeetCode Reverse Nodes in Even Length Groups using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Nodes in Even Length Groups |
| LeetCode | #2074 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `head` of a linked list.

The nodes in the linked list are **sequentially** assigned to **non-empty** groups whose lengths form the sequence of the natural numbers (`1, 2, 3, 4, ...`). The **length** of a group is the number of nodes assigned to it. In other words,

The `1^st` node is assigned to the first group. 
 The `2^nd` and the `3^rd` nodes are assigned to the second group. 
 The `4^th`, `5^th`, and `6^th` nodes are assigned to the third group, and so on.

Note that the length of the last group may be less than or equal to `1 + the length of the second to last group`.

**Reverse** the nodes in each group with an **even** length, and return *the* `head` *of the modified linked list*.

## Constraints
- The number of nodes in the list is in the range `[1, 10^5]`.
- `0 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `head = [5,2,6,3,9,1,7,3,8,4]`
- **Output:** `[5,6,2,3,9,1,4,8,3,7]`
- **Explanation:** - The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.

### Example 2
- **Input:** `head = [1,1,0,6]`
- **Output:** `[1,0,1,6]`
- **Explanation:** - The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.

### Example 3
- **Input:** `head = [1,1,0,6,5]`
- **Output:** `[1,0,1,5,6]`
- **Explanation:** - The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Reverse Nodes in Even Length Groups**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [5,2,6,3,9,1,7,3,8,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,6,2,3,9,1,4,8,3,7]`.
4. **Verification:** - The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.

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
var reverseEvenLengthGroups = function(head) {
    let current = head;
    let groupSize = 1;
    let prevGroupTail = null;

    while (current) {
        // Find actual group length
        let count = 0;
        let temp = current;

        while (temp && count < groupSize) {
            count++;
            temp = temp.next;
        }

        // Reverse only even-length groups
        if (count % 2 === 0) {
            let prev = temp;
            let node = current;

            // Reverse current group
            for (let i = 0; i < count; i++) {
                let nextNode = node.next;
                node.next = prev;
                prev = node;
                node = nextNode;
            }

            // Connect previous group to reversed group
            if (prevGroupTail) {
                prevGroupTail.next = prev;
            } else {
                head = prev;
            }

            prevGroupTail = current;
            current = temp;

        } else {
            // Odd group: no reversal
            for (let i = 0; i < count; i++) {
                prevGroupTail = current;
                current = current.next;
            }
        }

        groupSize++;
    }

    return head;
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
- [25. Reverse Nodes in k-Group](../../0001-0500/0025-reverse-nodes-in-k-group/)
- [2790. Maximum Number of Groups With Increasing Length](../../2501-3000/2790-maximum-number-of-groups-with-increasing-length/)
- [1315. Sum of Nodes with Even-Valued Grandparent](../../1001-1500/1315-sum-of-nodes-with-even-valued-grandparent/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/)
