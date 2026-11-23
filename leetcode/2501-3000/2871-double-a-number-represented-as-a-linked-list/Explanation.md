# LeetCode 2816: Double a Number Represented as a Linked List

**LeetCode Problem #2816 — Double a Number Represented as a Linked List**
Solve LeetCode Double a Number Represented as a Linked List using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Double a Number Represented as a Linked List |
| LeetCode | #2816 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given the  head  of a  non-empty  linked list representing a non-negative integer without leading zeroes.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Double a Number Represented as a Linked List**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1290. Convert Binary Number in a Linked List to Integer](../../1001-1500/1411-convert-binary-number-in-a-linked-list-to-integer/)
- [558. Logical OR of Two Binary Grids Represented as Quad-Trees](../../0501-1000/0773-logical-or-of-two-binary-grids-represented-as-quad-trees/)
- [2119. A Number After a Double Reversal](../../2001-2500/2238-a-number-after-a-double-reversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/)
