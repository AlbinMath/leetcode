# LeetCode 57: Insert Interval

**LeetCode Problem #57 — Insert Interval**
Solve LeetCode Insert Interval using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Insert Interval |
| LeetCode | #57 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array of non-overlapping intervals  intervals  where  intervals[i] = [start i , end i ]  represent the start and the end of the  i th   interval and  intervals  is sorted in ascending order by  start i  . You are also given an interval  newInterval = [start, end]  that represents the start and end of another interval.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Insert Interval**. Applying **Min/Max Heap Priority Selection** yields the target result step by step.

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
- [35. Search Insert Position](../0035-search-insert-position/)
- [1523. Count Odd Numbers in an Interval Range](../1630-count-odd-numbers-in-an-interval-range/)
- [2725. Interval Cancellation](../2862-interval-cancellation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/insert-interval/)
