# LeetCode 2589: Minimum Time to Complete All Tasks

**LeetCode Problem #2589 — Minimum Time to Complete All Tasks**
Solve LeetCode Minimum Time to Complete All Tasks using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Complete All Tasks |
| LeetCode | #2589 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a computer that can run an unlimited number of tasks  at the same time . You are given a 2D integer array  tasks  where  tasks[i] = [start i , end i , duration i ]  indicates that the  i th   task should run for a total of  duration i   seconds (not necessarily continuous) within the  inclusive  time range  [start i , end i ] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Time to Complete All Tasks**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1266. Minimum Time Visiting All Points](../1395-minimum-time-visiting-all-points/)
- [1443. Minimum Time to Collect All Apples in a Tree](../1554-minimum-time-to-collect-all-apples-in-a-tree/)
- [1723. Find Minimum Time to Finish All Jobs](../1825-find-minimum-time-to-finish-all-jobs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/)
