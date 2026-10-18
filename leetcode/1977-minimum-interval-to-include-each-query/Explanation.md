# LeetCode 1851: Minimum Interval to Include Each Query

**LeetCode Problem #1851 — Minimum Interval to Include Each Query**
Solve LeetCode Minimum Interval to Include Each Query using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Interval to Include Each Query |
| LeetCode | #1851 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a 2D integer array  intervals , where  intervals[i] = [left i , right i ]  describes the  i th   interval starting at  left i   and ending at  right i    (inclusive) . The  size  of an interval is defined as the number of integers it contains, or more formally  right i  - left i  + 1 .

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Interval to Include Each Query**. Applying **Min/Max Heap Priority Selection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [57. Insert Interval](../0057-insert-interval/)
- [64. Minimum Path Sum](../0064-minimum-path-sum/)
- [76. Minimum Window Substring](../0076-minimum-window-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-interval-to-include-each-query/)
