# LeetCode 1124: Longest Well-Performing Interval

**LeetCode Problem #1124 — Longest Well-Performing Interval**
Solve LeetCode Longest Well-Performing Interval using Python and Greedy. This solution finds the optimal result using Greedy Choice Strategy in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Well-Performing Interval |
| LeetCode | #1124 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Greedy Choice Strategy |
| Data Structure | Array / Priority Queue |
| Pattern | Greedy |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
We are given  hours , a list of the number of hours worked per day for a given employee.

## Key Insight
Leverage **Greedy** with **Array / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Priority Queue**).
2. Process elements sequentially using **Greedy Choice Strategy**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Well-Performing Interval**. Applying **Greedy Choice Strategy** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Greedy**

## Topics
- Greedy
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Greedy**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [57. Insert Interval](../0057-insert-interval/)
- [436. Find Right Interval](../0436-find-right-interval/)
- [986. Interval List Intersections](../1028-interval-list-intersections/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-well-performing-interval/)
