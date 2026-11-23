# LeetCode 2646: Minimize the Total Price of the Trips

**LeetCode Problem #2646 — Minimize the Total Price of the Trips**
Solve LeetCode Minimize the Total Price of the Trips using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize the Total Price of the Trips |
| LeetCode | #2646 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There exists an undirected and unrooted tree with  n  nodes indexed from  0  to  n - 1 . You are given the integer  n  and a 2D integer array  edges  of length  n - 1 , where  edges[i] = [a i , b i ]  indicates that there is an edge between nodes  a i   and  b i   in the tree.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimize the Total Price of the Trips**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1164. Product Price at a Given Date](../1278-product-price-at-a-given-date/)
- [1251. Average Selling Price](../1390-average-selling-price/)
- [2034. Stock Price Fluctuation ](../2161-stock-price-fluctuation-/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-the-total-price-of-the-trips/)
