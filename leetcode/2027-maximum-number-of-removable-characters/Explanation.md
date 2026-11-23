# LeetCode 1898: Maximum Number of Removable Characters

**LeetCode Problem #1898 — Maximum Number of Removable Characters**
Solve LeetCode Maximum Number of Removable Characters using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Removable Characters |
| LeetCode | #1898 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two strings  s  and  p  where  p  is a  subsequence  of  s . You are also given a  distinct 0-indexed  integer array  removable  containing a subset of indices of  s  ( s  is also  0-indexed ).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Number of Removable Characters**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [321. Create Maximum Number](../0321-create-maximum-number/)
- [414. Third Maximum Number](../0414-third-maximum-number/)
- [1072. Flip Columns For Maximum Number of Equal Rows](../1147-flip-columns-for-maximum-number-of-equal-rows/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-removable-characters/)
