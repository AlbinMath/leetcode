# LeetCode 862: Shortest Subarray with Sum at Least K

**LeetCode Problem #862 — Shortest Subarray with Sum at Least K**
Solve LeetCode Shortest Subarray with Sum at Least K using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Subarray with Sum at Least K |
| LeetCode | #862 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums  and an integer  k , return  the length of the shortest non-empty  subarray  of   nums   with a sum of at least   k . If there is no such  subarray , return  -1 .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Shortest Subarray with Sum at Least K**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3095. Shortest Subarray With OR at Least K I](../3381-shortest-subarray-with-or-at-least-k-i/)
- [3097. Shortest Subarray With OR at Least K II](../3380-shortest-subarray-with-or-at-least-k-ii/)
- [3795. Minimum Subarray Length With Distinct Sum At Least K](../4152-minimum-subarray-length-with-distinct-sum-at-least-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)
