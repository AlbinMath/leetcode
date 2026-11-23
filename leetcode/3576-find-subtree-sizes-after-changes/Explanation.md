# LeetCode 3331: Find Subtree Sizes After Changes

**LeetCode Problem #3331 — Find Subtree Sizes After Changes**
Solve LeetCode Find Subtree Sizes After Changes using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Subtree Sizes After Changes |
| LeetCode | #3331 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a tree rooted at node 0 that consists of  n  nodes numbered from  0  to  n - 1 . The tree is represented by an array  parent  of size  n , where  parent[i]  is the parent of node  i . Since node 0 is the root,  parent[0] == -1 .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Subtree Sizes After Changes**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2089. Find Target Indices After Sorting Array](../2210-find-target-indices-after-sorting-array/)
- [2458. Height of Binary Tree After Subtree Removal Queries](../2545-height-of-binary-tree-after-subtree-removal-queries/)
- [2593. Find Score of an Array After Marking All Elements](../2695-find-score-of-an-array-after-marking-all-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-subtree-sizes-after-changes/)
