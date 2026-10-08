# LeetCode 56: Merge Intervals

**LeetCode Problem #56 — Merge Intervals**
Solve LeetCode Merge Intervals using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge Intervals |
| LeetCode | #56 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an array of  intervals  where  intervals[i] = [start i , end i ] , merge all overlapping intervals, and return  an array of the non-overlapping intervals that cover all the intervals in the input .

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Merge Intervals**. Applying **Min/Max Heap Priority Selection** yields the target result step by step.

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
- [21. Merge Two Sorted Lists](../0021-merge-two-sorted-lists/)
- [23. Merge k Sorted Lists](../0023-merge-k-sorted-lists/)
- [88. Merge Sorted Array](../0088-merge-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-intervals/)
