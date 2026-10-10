# LeetCode 1422: Maximum Score After Splitting a String

**LeetCode Problem #1422 — Maximum Score After Splitting a String**
Solve LeetCode Maximum Score After Splitting a String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score After Splitting a String |
| LeetCode | #1422 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s  of zeros and ones,  return the maximum score after splitting the string into two  non-empty  substrings  (i.e.  left  substring and  right  substring).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Score After Splitting a String**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1846. Maximum Element After Decreasing and Rearranging](../1956-maximum-element-after-decreasing-and-rearranging/)
- [1945. Sum of Digits of String After Convert](../2076-sum-of-digits-of-string-after-convert/)
- [3414. Maximum Score of Non-overlapping Intervals](../3562-maximum-score-of-non-overlapping-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-after-splitting-a-string/)
