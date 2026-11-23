# LeetCode 1695: Maximum Erasure Value

**LeetCode Problem #1695 — Maximum Erasure Value**
Solve LeetCode Maximum Erasure Value using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Erasure Value |
| LeetCode | #1695 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of positive integers  nums  and want to erase a subarray containing  unique elements . The  score  you get by erasing the subarray is equal to the  sum  of its elements.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Erasure Value**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1881. Maximum Value after Insertion](../2011-maximum-value-after-insertion/)
- [3256. Maximum Value Sum by Placing Three Rooks I](../3550-maximum-value-sum-by-placing-three-rooks-i/)
- [3257. Maximum Value Sum by Placing Three Rooks II](../3542-maximum-value-sum-by-placing-three-rooks-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-erasure-value/)
