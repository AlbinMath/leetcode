# LeetCode 116: Populating Next Right Pointers in Each Node

**LeetCode Problem #116 — Populating Next Right Pointers in Each Node**
Solve LeetCode Populating Next Right Pointers in Each Node using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Populating Next Right Pointers in Each Node |
| LeetCode | #116 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  perfect binary tree  where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Stack Push / Pop Parsing**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Populating Next Right Pointers in Each Node**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [117. Populating Next Right Pointers in Each Node II](../0117-populating-next-right-pointers-in-each-node-ii/)
- [1019. Next Greater Node In Linked List](../1072-next-greater-node-in-linked-list/)
- [2516. Take K of Each Character From Left and Right](../2599-take-k-of-each-character-from-left-and-right/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
