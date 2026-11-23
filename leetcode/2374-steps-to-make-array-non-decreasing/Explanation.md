# LeetCode 2289: Steps to Make Array Non-decreasing

**LeetCode Problem #2289 — Steps to Make Array Non-decreasing**
Solve LeetCode Steps to Make Array Non-decreasing using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Steps to Make Array Non-decreasing |
| LeetCode | #2289 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  integer array  nums . In one step,  remove  all elements  nums[i]  where  nums[i - 1] > nums[i]  for all  0 < i < nums.length .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Steps to Make Array Non-decreasing**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [3326. Minimum Division Operations to Make Array Non Decreasing](../3607-minimum-division-operations-to-make-array-non-decreasing/)
- [3523. Make Array Non-decreasing](../3738-make-array-non-decreasing/)
- [2945. Find Maximum Non-decreasing Array Length](../3211-find-maximum-non-decreasing-array-length/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/steps-to-make-array-non-decreasing/)
