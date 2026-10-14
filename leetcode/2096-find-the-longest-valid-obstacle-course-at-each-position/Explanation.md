# LeetCode 1964: Find the Longest Valid Obstacle Course at Each Position

**LeetCode Problem #1964 — Find the Longest Valid Obstacle Course at Each Position**
Solve LeetCode Find the Longest Valid Obstacle Course at Each Position using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Longest Valid Obstacle Course at Each Position |
| LeetCode | #1964 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You want to build some obstacle courses. You are given a  0-indexed  integer array  obstacles  of length  n , where  obstacles[i]  describes the height of the  i th   obstacle.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Longest Valid Obstacle Course at Each Position**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [32. Longest Valid Parentheses](../0032-longest-valid-parentheses/)
- [34. Find First and Last Position of Element in Sorted Array](../0034-find-first-and-last-position-of-element-in-sorted-array/)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/)
