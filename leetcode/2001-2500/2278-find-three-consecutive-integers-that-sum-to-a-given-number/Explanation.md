# LeetCode 2177: Find Three Consecutive Integers That Sum to a Given Number

**LeetCode Problem #2177 — Find Three Consecutive Integers That Sum to a Given Number**
Solve LeetCode Find Three Consecutive Integers That Sum to a Given Number using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Three Consecutive Integers That Sum to a Given Number |
| LeetCode | #2177 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer  num , return  three consecutive integers (as a sorted array)   that  sum  to   num . If  num  cannot be expressed as the sum of three consecutive integers, return  an  empty  array.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Three Consecutive Integers That Sum to a Given Number**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1501-2000/1621-number-of-subsequences-that-satisfy-the-given-sum-condition/)
- [2526. Find Consecutive Integers from a Data Stream](../../2501-3000/2620-find-consecutive-integers-from-a-data-stream/)
- [1606. Find Servers That Handled Most Number of Requests](../../1501-2000/1710-find-servers-that-handled-most-number-of-requests/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/)
