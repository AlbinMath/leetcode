# LeetCode 1530: Number of Good Leaf Nodes Pairs

**LeetCode Problem #1530 — Number of Good Leaf Nodes Pairs**
Solve LeetCode Number of Good Leaf Nodes Pairs using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Good Leaf Nodes Pairs |
| LeetCode | #1530 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given the  root  of a binary tree and an integer  distance . A pair of two different  leaf  nodes of a binary tree is said to be good if the length of  the shortest path  between them is less than or equal to  distance .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Good Leaf Nodes Pairs**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1512. Number of Good Pairs](../../1501-2000/1635-number-of-good-pairs/)
- [24. Swap Nodes in Pairs](../../0001-0500/0024-swap-nodes-in-pairs/)
- [1080. Insufficient Nodes in Root to Leaf Paths](../../1001-1500/1157-insufficient-nodes-in-root-to-leaf-paths/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/)
