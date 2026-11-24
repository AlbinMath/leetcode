# LeetCode 24: Swap Nodes in Pairs

**LeetCode Problem #24 — Swap Nodes in Pairs**
Solve LeetCode Swap Nodes in Pairs using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Swap Nodes in Pairs |
| LeetCode | #24 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

## Constraints
- The number of nodes in the list is in the range `[0, 100]`.
- `0 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `head = [1,2,3,4]`
- **Output:** `[2,1,4,3]`

### Example 2
- **Input:** `head = []`
- **Output:** `[]`

### Example 3
- **Input:** `head = [1]`
- **Output:** `[1]`

### Example 4
- **Input:** `head = [1,2,3]`
- **Output:** `[2,1,3]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Swap Nodes in Pairs**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,3,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1,4,3]`.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var swapPairs = function(head) {
    const dummy = new ListNode(0);
    dummy.next = head;

    let prev = dummy;

    while (prev.next !== null && prev.next.next !== null) {
        let first = prev.next;
        let second = first.next;

        // Swap the two nodes
        first.next = second.next;
        second.next = first;
        prev.next = second;

        // Move to the next pair
        prev = first;
    }

    return dummy.next;
};
```

### Python
```python
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swap the two nodes
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next
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
- [1530. Number of Good Leaf Nodes Pairs](../../1501-2000/1530-number-of-good-leaf-nodes-pairs/)
- [1782. Count Pairs Of Nodes](../../1501-2000/1782-count-pairs-of-nodes/)
- [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](../../2001-2500/2316-count-unreachable-pairs-of-nodes-in-an-undirected-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/)
