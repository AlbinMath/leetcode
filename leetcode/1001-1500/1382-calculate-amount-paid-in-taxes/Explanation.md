# LeetCode 2303: Calculate Amount Paid in Taxes

**LeetCode Problem #2303 — Calculate Amount Paid in Taxes**
Solve LeetCode Calculate Amount Paid in Taxes using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Calculate Amount Paid in Taxes |
| LeetCode | #2303 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  2D integer array  brackets  where  brackets[i] = [upper i , percent i ]  means that the  i th   tax bracket has an upper bound of  upper i   and is taxed at a rate of  percent i  . The brackets are  sorted  by upper bound (i.e.  upper i-1  < upper i   for  0 < i < brackets.length ).

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Calculate Amount Paid in Taxes**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2385. Amount of Time for Binary Tree to Be Infected](../../2001-2500/2461-amount-of-time-for-binary-tree-to-be-infected/)
- [3116. Kth Smallest Amount With Single Denomination Combination](../../3001-3500/3375-kth-smallest-amount-with-single-denomination-combination/)
- [3387. Maximize Amount After Two Days of Conversions](../../3501-4000/3613-maximize-amount-after-two-days-of-conversions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/calculate-amount-paid-in-taxes/)
