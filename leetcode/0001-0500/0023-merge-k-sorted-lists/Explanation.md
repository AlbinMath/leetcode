# LeetCode 23: Merge k Sorted Lists

**LeetCode Problem #23 — Merge k Sorted Lists**
Solve LeetCode Merge k Sorted Lists using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge k Sorted Lists |
| LeetCode | #23 |
| Difficulty | Hard |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

## Constraints
- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed `10^4`.

## Examples
### Example 1
- **Input:** `lists = [[1,4,5],[1,3,4],[2,6]]`
- **Output:** `[1,1,2,3,4,4,5,6]`
- **Explanation:** The linked-lists are:
[
 1->4->5,
 1->3->4,
 2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

### Example 2
- **Input:** `lists = []`
- **Output:** `[]`

### Example 3
- **Input:** `lists = [[]]`
- **Output:** `[]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Merge k Sorted Lists**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `lists = [[1,4,5],[1,3,4],[2,6]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,1,2,3,4,4,5,6]`.
4. **Verification:** The linked-lists are:
[
 1->4->5,
 1->3->4,
 2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

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
var mergeKLists = function(lists) {
    if (lists.length === 0) {
        return null;
    }

    // Merge lists in pairs, doubling the interval each round
    for (let interval = 1; interval < lists.length; interval *= 2) {
        for (let i = 0; i + interval < lists.length; i += interval * 2) {
            lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
        }
    }

    return lists[0];
};

function mergeTwoLists(list1, list2) {
    const dummy = new ListNode(0);
    let tail = dummy;

    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) {
            tail.next = list1;
            list1 = list1.next;
        } else {
            tail.next = list2;
            list2 = list2.next;
        }

        tail = tail.next;
    }

    // Attach whichever list still has nodes
    tail.next = list1 !== null ? list1 : list2;

    return dummy.next;
}
```

### Python
```python
import heapq
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Add the first node of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            # Add the next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

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
- [21. Merge Two Sorted Lists](../../0001-0500/0021-merge-two-sorted-lists/)
- [3801. Minimum Cost to Merge Sorted Lists](../../3501-4000/3801-minimum-cost-to-merge-sorted-lists/)
- [632. Smallest Range Covering Elements from K Lists](../../0501-1000/0632-smallest-range-covering-elements-from-k-lists/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)
