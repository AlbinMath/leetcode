# LeetCode 436: Find Right Interval

**LeetCode Problem #436 — Find Right Interval**
Solve LeetCode Find Right Interval using JavaScript and Greedy. This solution finds the optimal result using Greedy Choice Strategy in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Right Interval |
| LeetCode | #436 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Greedy Choice Strategy |
| Data Structure | Array / Priority Queue |
| Pattern | Greedy |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of  intervals , where  intervals[i] = [start i , end i ]  and each  start i   is  unique .

## Key Insight
Leverage **Greedy** with **Array / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Priority Queue**).
2. Process elements sequentially using **Greedy Choice Strategy**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Right Interval**. Applying **Greedy Choice Strategy** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Greedy**

## Topics
- Greedy
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [28. Find the Index of the First Occurrence in a String](../0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [34. Find First and Last Position of Element in Sorted Array](../0034-find-first-and-last-position-of-element-in-sorted-array/)
- [57. Insert Interval](../0057-insert-interval/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-right-interval/)
