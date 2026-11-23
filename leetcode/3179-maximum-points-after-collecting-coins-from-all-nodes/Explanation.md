# LeetCode 2920: Maximum Points After Collecting Coins From All Nodes

**LeetCode Problem #2920 — Maximum Points After Collecting Coins From All Nodes**
Solve LeetCode Maximum Points After Collecting Coins From All Nodes using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Points After Collecting Coins From All Nodes |
| LeetCode | #2920 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There exists an undirected tree rooted at node  0  with  n  nodes labeled from  0  to  n - 1 . You are given a 2D  integer  array  edges  of length  n - 1 , where  edges[i] = [a i , b i ]  indicates that there is an edge between nodes  a i   and  b i   in the tree. You are also given a  0-indexed  array  coins  of size  n  where  coins[i]  indicates the number of coins in the vertex  i , and an integer  k .

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Points After Collecting Coins From All Nodes**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [1423. Maximum Points You Can Obtain from Cards](../1538-maximum-points-you-can-obtain-from-cards/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [2503. Maximum Number of Points From Grid Queries](../2588-maximum-number-of-points-from-grid-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/)
