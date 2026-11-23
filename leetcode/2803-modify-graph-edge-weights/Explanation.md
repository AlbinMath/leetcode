# LeetCode 2699: Modify Graph Edge Weights

**LeetCode Problem #2699 — Modify Graph Edge Weights**
Solve LeetCode Modify Graph Edge Weights using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Modify Graph Edge Weights |
| LeetCode | #2699 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an  undirected weighted   connected  graph containing  n  nodes labeled from  0  to  n - 1 , and an integer array  edges  where  edges[i] = [a i , b i , w i ]  indicates that there is an edge between nodes  a i   and  b i   with weight  w i  .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Modify Graph Edge Weights**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3419. Minimize the Maximum Edge Weight of Graph](../3720-minimize-the-maximum-edge-weight-of-graph/)
- [3547. Maximum Sum of Edge Values in a Graph](../3845-maximum-sum-of-edge-values-in-a-graph/)
- [3558. Number of Ways to Assign Edge Weights I](../3844-number-of-ways-to-assign-edge-weights-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/modify-graph-edge-weights/)
