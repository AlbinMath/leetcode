# LeetCode 2784: Check if Array is Good

**LeetCode Problem #2784 — Check if Array is Good**
Solve LeetCode Check if Array is Good using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Array is Good |
| LeetCode | #2784 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums . We consider an array  good  if it is a permutation of an array  base[n] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Sort the array. The maximum value should be `n = arr.length - 1`. Check that the last two elements equal `n` and elements 0 through n-2 equal 1 through n-1 respectively.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check if Array is Good**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1752. Check if Array Is Sorted and Rotated](../1878-check-if-array-is-sorted-and-rotated/)
- [1961. Check If String Is a Prefix of Array](../2093-check-if-string-is-a-prefix-of-array/)
- [1232. Check If It Is a Straight Line](../1349-check-if-it-is-a-straight-line/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-array-is-good/)
