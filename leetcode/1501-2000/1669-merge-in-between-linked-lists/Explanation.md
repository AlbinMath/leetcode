# LeetCode 1669: Merge In Between Linked Lists

**LeetCode Problem #1669 — Merge In Between Linked Lists**
Solve LeetCode Merge In Between Linked Lists using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge In Between Linked Lists |
| LeetCode | #1669 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two linked lists: `list1` and `list2` of sizes `n` and `m` respectively.

Remove `list1`'s nodes from the `a^th` node to the `b^th` node, and put `list2` in their place.

The blue edges and nodes in the following figure indicate the result:

*Build the result list and return its head.*

## Constraints
- `3 <= list1.length <= 10^4`
- `1 <= a <= b < list1.length - 1`
- `1 <= list2.length <= 10^4`

## Examples
### Example 1
- **Input:** `list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]`
- **Output:** `[10,1,13,1000000,1000001,1000002,5]`
- **Explanation:** We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

### Example 2
- **Input:** `list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]`
- **Output:** `[0,1,1000000,1000001,1000002,1000003,1000004,6]`
- **Explanation:** The blue edges and nodes in the above figure indicate the result.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Merge In Between Linked Lists**, we observe the problem requirements and utilize the **Linked List** technique. We iterate through the inputs using **Pointer Traversal & Node Manipulation**, leveraging a **Linked List** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Linked List**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]`.
2. **Processing Steps:** We apply **Pointer Traversal & Node Manipulation** using our **Linked List**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[10,1,13,1000000,1000001,1000002,5]`.
4. **Verification:** We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List.

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next
            
        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next
            
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
            
        prev_a.next = list2
        tail2.next = after_b
        
        return list1
```

## Why This Works
By utilizing **Linked List**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [21. Merge Two Sorted Lists](../../0001-0500/0021-merge-two-sorted-lists/)
- [23. Merge k Sorted Lists](../../0001-0500/0023-merge-k-sorted-lists/)
- [2181. Merge Nodes in Between Zeros](../../2001-2500/2181-merge-nodes-in-between-zeros/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-in-between-linked-lists/)
