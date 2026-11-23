# LeetCode 3203: Find Minimum Diameter After Merging Two Trees

**LeetCode Problem #3203 — Find Minimum Diameter After Merging Two Trees**
Solve LeetCode Find Minimum Diameter After Merging Two Trees using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Minimum Diameter After Merging Two Trees |
| LeetCode | #3203 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There exist two  undirected  trees with  n  and  m  nodes, numbered from  0  to  n - 1  and from  0  to  m - 1 , respectively. You are given two 2D integer arrays  edges1  and  edges2  of lengths  n - 1  and  m - 1 , respectively, where  edges1[i] = [a i , b i ]  indicates that there is an edge between nodes  a i   and  b i   in the first tree and  edges2[i] = [u i , v i ]  indicates that there is an edge between nodes  u i   and  v i   in the second tree.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Minimum Diameter After Merging Two Trees**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [1750. Minimum Length of String After Deleting Similar Ends](../1850-minimum-length-of-string-after-deleting-similar-ends/)
- [2089. Find Target Indices After Sorting Array](../2210-find-target-indices-after-sorting-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/)
