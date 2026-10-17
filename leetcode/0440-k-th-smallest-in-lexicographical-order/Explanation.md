# LeetCode 440: K-th Smallest in Lexicographical Order

**LeetCode Problem #440 — K-th Smallest in Lexicographical Order**
Solve LeetCode K-th Smallest in Lexicographical Order using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K-th Smallest in Lexicographical Order |
| LeetCode | #440 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two integers  n  and  k , return  the   k th    lexicographically smallest integer in the range   [1, n] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **K-th Smallest in Lexicographical Order**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [373. Find K Pairs with Smallest Sums](../0373-find-k-pairs-with-smallest-sums/)
- [632. Smallest Range Covering Elements from K Lists](../0632-smallest-range-covering-elements-from-k-lists/)
- [1015. Smallest Integer Divisible by K](../1064-smallest-integer-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/)
