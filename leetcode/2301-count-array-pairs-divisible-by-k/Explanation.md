# LeetCode 2183: Count Array Pairs Divisible by K

**LeetCode Problem #2183 — Count Array Pairs Divisible by K**
Solve LeetCode Count Array Pairs Divisible by K using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Array Pairs Divisible by K |
| LeetCode | #2183 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a  0-indexed  integer array  nums  of length  n  and an integer  k , return  the  number of pairs    (i, j)   such that:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Array Pairs Divisible by K**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1005. Maximize Sum Of Array After K Negations](../1047-maximize-sum-of-array-after-k-negations/)
- [1679. Max Number of K-Sum Pairs](../1798-max-number-of-k-sum-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-array-pairs-divisible-by-k/)
