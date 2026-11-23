# LeetCode 1074: Number of Submatrices That Sum to Target

**LeetCode Problem #1074 — Number of Submatrices That Sum to Target**
Solve LeetCode Number of Submatrices That Sum to Target using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Submatrices That Sum to Target |
| LeetCode | #1074 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a  matrix  and a  target , return the number of non-empty submatrices that sum to  target .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Submatrices That Sum to Target**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../1621-number-of-subsequences-that-satisfy-the-given-sum-condition/)
- [2177. Find Three Consecutive Integers That Sum to a Given Number](../2278-find-three-consecutive-integers-that-sum-to-a-given-number/)
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../3240-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)
