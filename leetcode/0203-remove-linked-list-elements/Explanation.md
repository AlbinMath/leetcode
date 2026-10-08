# LeetCode 203: Remove Linked List Elements

**LeetCode Problem #203 — Remove Linked List Elements**
Solve LeetCode Remove Linked List Elements using PHP and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Linked List Elements |
| LeetCode | #203 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  head  of a linked list and an integer  val , remove all the nodes of the linked list that has  Node.val == val , and return  the new head .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Remove Linked List Elements**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
PHP

## Source Code
- [solution.php](./solution.php)

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
- [19. Remove Nth Node From End of List](../0019-remove-nth-node-from-end-of-list/)
- [82. Remove Duplicates from Sorted List II](../0082-remove-duplicates-from-sorted-list-ii/)
- [83. Remove Duplicates from Sorted List](../0083-remove-duplicates-from-sorted-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-linked-list-elements/)
