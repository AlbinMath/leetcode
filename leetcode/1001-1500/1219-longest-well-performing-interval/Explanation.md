# LeetCode 1124: Longest Well-Performing Interval

**LeetCode Problem #1124 — Longest Well-Performing Interval**
Solve LeetCode Longest Well-Performing Interval using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Well-Performing Interval |
| LeetCode | #1124 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
We are given  hours , a list of the number of hours worked per day for a given employee.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Well-Performing Interval**. Applying **Min/Max Heap Priority Selection** yields the target result step by step.

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
- [2011. Final Value of Variable After Performing Operations](../../2001-2500/2137-final-value-of-variable-after-performing-operations/)
- [3080. Mark Elements on Array by Performing Queries](../../3001-3500/3306-mark-elements-on-array-by-performing-queries/)
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3501-4000/3622-maximum-frequency-of-an-element-after-performing-operations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-well-performing-interval/)
