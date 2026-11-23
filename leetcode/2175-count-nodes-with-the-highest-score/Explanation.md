# LeetCode 2049: Count Nodes With the Highest Score

**LeetCode Problem #2049 — Count Nodes With the Highest Score**
Solve LeetCode Count Nodes With the Highest Score using JavaScript and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Nodes With the Highest Score |
| LeetCode | #2049 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a  binary  tree rooted at  0  consisting of  n  nodes. The nodes are labeled from  0  to  n - 1 . You are given a  0-indexed  integer array  parents  representing the tree, where  parents[i]  is the parent of node  i . Since node  0  is the root,  parents[0] == -1 .

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Nodes With the Highest Score**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [222. Count Complete Tree Nodes](../0222-count-complete-tree-nodes/)
- [1448. Count Good Nodes in Binary Tree](../1544-count-good-nodes-in-binary-tree/)
- [1782. Count Pairs Of Nodes](../1891-count-pairs-of-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-nodes-with-the-highest-score/)
