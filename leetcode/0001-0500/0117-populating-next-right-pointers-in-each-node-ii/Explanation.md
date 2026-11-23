# LeetCode 117: Populating Next Right Pointers in Each Node II

**LeetCode Problem #117 — Populating Next Right Pointers in Each Node II**
Solve LeetCode Populating Next Right Pointers in Each Node II using JavaScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Populating Next Right Pointers in Each Node II |
| LeetCode | #117 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to  NULL .

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
We iterate through the input using **Stack Push / Pop Parsing**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Populating Next Right Pointers in Each Node II**. Applying **Monotonic Stack Filtering** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [116. Populating Next Right Pointers in Each Node](../../0001-0500/0116-populating-next-right-pointers-in-each-node/)
- [1019. Next Greater Node In Linked List](../../1001-1500/1072-next-greater-node-in-linked-list/)
- [2516. Take K of Each Character From Left and Right](../../2501-3000/2599-take-k-of-each-character-from-left-and-right/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)
