# LeetCode 24: Swap Nodes in Pairs

**LeetCode Problem #24 — Swap Nodes in Pairs**
Solve LeetCode Swap Nodes in Pairs using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Swap Nodes in Pairs |
| LeetCode | #24 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list&#39;s nodes (i.e., only nodes themselves may be changed.)

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Swap Nodes in Pairs**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [25. Reverse Nodes in k-Group](../0025-reverse-nodes-in-k-group/)
- [627. Swap Sex of Employees](../0627-swap-sex-of-employees/)
- [1807. Evaluate the Bracket Pairs of a String](../1934-evaluate-the-bracket-pairs-of-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/)
