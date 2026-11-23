# LeetCode 992: Subarrays with K Different Integers

**LeetCode Problem #992 — Subarrays with K Different Integers**
Solve LeetCode Subarrays with K Different Integers using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subarrays with K Different Integers |
| LeetCode | #992 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums  and an integer  k , return  the number of  good subarrays  of   nums .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Subarrays with K Different Integers**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3859. Count Subarrays With K Distinct Integers](../4002-count-subarrays-with-k-distinct-integers/)
- [1805. Number of Different Integers in a String](../1933-number-of-different-integers-in-a-string/)
- [3621. Number of Integers With Popcount-Depth Equal to K I](../3937-number-of-integers-with-popcount-depth-equal-to-k-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subarrays-with-k-different-integers/)
