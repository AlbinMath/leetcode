# LeetCode 3604: Minimum Time to Reach Destination in Directed Graph

**LeetCode Problem #3604 — Minimum Time to Reach Destination in Directed Graph**
Solve LeetCode Minimum Time to Reach Destination in Directed Graph using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Reach Destination in Directed Graph |
| LeetCode | #3604 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n  and a  directed  graph with  n  nodes labeled from 0 to  n - 1 . This is represented by a 2D array  edges , where  edges[i] = [u i , v i , start i , end i ]  indicates an edge from node  u i   to  v i   that can  only  be used at any integer time  t  such that  start i  <= t <= end i  .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Time to Reach Destination in Directed Graph**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1928. Minimum Cost to Reach Destination in Time](../2040-minimum-cost-to-reach-destination-in-time/)
- [2045. Second Minimum Time to Reach Destination](../2171-second-minimum-time-to-reach-destination/)
- [3341. Find Minimum Time to Reach Last Room I](../3627-find-minimum-time-to-reach-last-room-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/)
