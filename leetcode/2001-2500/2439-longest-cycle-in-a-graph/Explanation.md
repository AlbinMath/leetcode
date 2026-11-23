# LeetCode 2360: Longest Cycle in a Graph

**LeetCode Problem #2360 — Longest Cycle in a Graph**
Solve LeetCode Longest Cycle in a Graph using JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Cycle in a Graph |
| LeetCode | #2360 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  directed  graph of  n  nodes numbered from  0  to  n - 1 , where each node has  at most one  outgoing edge.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Floyd Cycle Detection**. By maintaining state efficiently in a **Linked List / Pointer**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Pointer**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Cycle in a Graph**. Applying **Floyd Cycle Detection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2608. Shortest Cycle in a Graph](../../2501-3000/2671-shortest-cycle-in-a-graph/)
- [3615. Longest Palindromic Path in Graph](../../3501-4000/3930-longest-palindromic-path-in-graph/)
- [141. Linked List Cycle](../../0001-0500/0141-linked-list-cycle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-cycle-in-a-graph/)
