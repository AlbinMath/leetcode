# LeetCode 352: Data Stream as Disjoint Intervals

**LeetCode Problem #352 — Data Stream as Disjoint Intervals**
Solve LeetCode Data Stream as Disjoint Intervals using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Data Stream as Disjoint Intervals |
| LeetCode | #352 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a data stream input of non-negative integers  a 1 , a 2 , ..., a n  , summarize the numbers seen so far as a list of disjoint intervals.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Data Stream as Disjoint Intervals**. Applying **Min/Max Heap Priority Selection** yields the target result step by step.

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
- [295. Find Median from Data Stream](../0295-find-median-from-data-stream/)
- [56. Merge Intervals](../0056-merge-intervals/)
- [211. Design Add and Search Words Data Structure](../0211-design-add-and-search-words-data-structure/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)
