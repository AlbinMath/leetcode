# LeetCode 689: Maximum Sum of 3 Non-Overlapping Subarrays

**LeetCode Problem #689 — Maximum Sum of 3 Non-Overlapping Subarrays**
Solve LeetCode Maximum Sum of 3 Non-Overlapping Subarrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of 3 Non-Overlapping Subarrays |
| LeetCode | #689 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums  and an integer  k , find three non-overlapping subarrays of length  k  with maximum sum and return them.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Sum of 3 Non-Overlapping Subarrays**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1096-maximum-sum-of-two-non-overlapping-subarrays/)
- [3956. Maximum Sum of M Non-Overlapping Subarrays I](../../4001-4500/4123-maximum-sum-of-m-non-overlapping-subarrays-i/)
- [3957. Maximum Sum of M Non-Overlapping Subarrays II](../../4001-4500/4125-maximum-sum-of-m-non-overlapping-subarrays-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/)
