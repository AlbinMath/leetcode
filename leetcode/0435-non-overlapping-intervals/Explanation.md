# LeetCode 435: Non-overlapping Intervals

**LeetCode Problem #435 — Non-overlapping Intervals**
Solve LeetCode Non-overlapping Intervals using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Non-overlapping Intervals |
| LeetCode | #435 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an array of intervals  intervals  where  intervals[i] = [start i , end i ] , return  the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping .

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Non-overlapping Intervals**. Applying **Min/Max Heap Priority Selection** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [3414. Maximum Score of Non-overlapping Intervals](../3562-maximum-score-of-non-overlapping-intervals/)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [1520. Maximum Number of Non-Overlapping Substrings](../1644-maximum-number-of-non-overlapping-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)
