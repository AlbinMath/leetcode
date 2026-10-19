# LeetCode 3036: Number of Subarrays That Match a Pattern II

**LeetCode Problem #3036 — Number of Subarrays That Match a Pattern II**
Solve LeetCode Number of Subarrays That Match a Pattern II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Subarrays That Match a Pattern II |
| LeetCode | #3036 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  integer array  nums  of size  n , and a  0-indexed  integer array  pattern  of size  m  consisting of integers  -1 ,  0 , and  1 .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Subarrays That Match a Pattern II**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3034. Number of Subarrays That Match a Pattern I](../3269-number-of-subarrays-that-match-a-pattern-i/)
- [137. Single Number II](../0137-single-number-ii/)
- [375. Guess Number Higher or Lower II](../0375-guess-number-higher-or-lower-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/)
