# LeetCode 1530: Number of Good Leaf Nodes Pairs

**LeetCode Problem #1530 — Number of Good Leaf Nodes Pairs**
Solve LeetCode Number of Good Leaf Nodes Pairs using JavaScript and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Good Leaf Nodes Pairs |
| LeetCode | #1530 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given the  root  of a binary tree and an integer  distance . A pair of two different  leaf  nodes of a binary tree is said to be good if the length of  the shortest path  between them is less than or equal to  distance .

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Good Leaf Nodes Pairs**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1512. Number of Good Pairs](../1635-number-of-good-pairs/)
- [1080. Insufficient Nodes in Root to Leaf Paths](../1157-insufficient-nodes-in-root-to-leaf-paths/)
- [1448. Count Good Nodes in Binary Tree](../1544-count-good-nodes-in-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/)
