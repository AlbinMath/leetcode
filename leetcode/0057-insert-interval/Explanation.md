# LeetCode 57: Insert Interval

**LeetCode Problem #57 — Insert Interval**
Solve LeetCode Insert Interval using Python and Greedy. This solution finds the optimal result using Greedy Choice Strategy in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Insert Interval |
| LeetCode | #57 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Greedy Choice Strategy |
| Data Structure | Array / Priority Queue |
| Pattern | Greedy |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of non-overlapping intervals  intervals  where  intervals[i] = [start i , end i ]  represent the start and the end of the  i th   interval and  intervals  is sorted in ascending order by  start i  . You are also given an interval  newInterval = [start, end]  that represents the start and end of another interval.

## Key Insight
Leverage **Greedy** with **Array / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Priority Queue**).
2. Process elements sequentially using **Greedy Choice Strategy**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Insert Interval**. Applying **Greedy Choice Strategy** yields the target result step by step.

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
- [35. Search Insert Position](../0035-search-insert-position/)
- [2725. Interval Cancellation](../2862-interval-cancellation/)
- [56. Merge Intervals](../0056-merge-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/insert-interval/)
