# LeetCode 1986: Minimum Number of Work Sessions to Finish the Tasks

**LeetCode Problem #1986 — Minimum Number of Work Sessions to Finish the Tasks**
Solve LeetCode Minimum Number of Work Sessions to Finish the Tasks using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Work Sessions to Finish the Tasks |
| LeetCode | #1986 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There are  n  tasks assigned to you. The task times are represented as an integer array  tasks  of length  n , where the  i th   task takes  tasks[i]  hours to finish. A  work session  is when you work for  at most   sessionTime  consecutive hours and then take a break.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Number of Work Sessions to Finish the Tasks**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1665. Minimum Initial Energy to Finish Tasks](../1784-minimum-initial-energy-to-finish-tasks/)
- [1723. Find Minimum Time to Finish All Jobs](../1825-find-minimum-time-to-finish-all-jobs/)
- [452. Minimum Number of Arrows to Burst Balloons](../0452-minimum-number-of-arrows-to-burst-balloons/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/)
