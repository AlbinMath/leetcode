# LeetCode 3770: Largest Prime from Consecutive Prime Sum

**LeetCode Problem #3770 — Largest Prime from Consecutive Prime Sum**
Solve LeetCode Largest Prime from Consecutive Prime Sum using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Prime from Consecutive Prime Sum |
| LeetCode | #3770 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Prime from Consecutive Prime Sum**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1171. Remove Zero Sum Consecutive Nodes from Linked List](../../1001-1500/1267-remove-zero-sum-consecutive-nodes-from-linked-list/)
- [3556. Sum of Largest Prime Substrings](../../3501-4000/3815-sum-of-largest-prime-substrings/)
- [829. Consecutive Numbers Sum](../../0501-1000/0856-consecutive-numbers-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/)
