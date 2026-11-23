# LeetCode 1857: Largest Color Value in a Directed Graph

**LeetCode Problem #1857 — Largest Color Value in a Directed Graph**
Solve LeetCode Largest Color Value in a Directed Graph using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Color Value in a Directed Graph |
| LeetCode | #1857 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a  directed graph  of  n  colored nodes and  m  edges. The nodes are numbered from  0  to  n - 1 .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Color Value in a Directed Graph**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2192. All Ancestors of a Node in a Directed Acyclic Graph](../../1001-1500/1431-all-ancestors-of-a-node-in-a-directed-acyclic-graph/)
- [2876. Count Visited Nodes in a Directed Graph](../../3001-3500/3140-count-visited-nodes-in-a-directed-graph/)
- [3604. Minimum Time to Reach Destination in Directed Graph](../../3501-4000/3916-minimum-time-to-reach-destination-in-directed-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/)
