# LeetCode 1960: Maximum Product of the Length of Two Palindromic Substrings

**LeetCode Problem #1960 — Maximum Product of the Length of Two Palindromic Substrings**
Solve LeetCode Maximum Product of the Length of Two Palindromic Substrings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of the Length of Two Palindromic Substrings |
| LeetCode | #1960 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  string  s  and are tasked with finding two  non-intersecting palindromic  substrings of  odd  length such that the product of their lengths is maximized.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Product of the Length of Two Palindromic Substrings**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1464. Maximum Product of Two Elements in an Array](../1574-maximum-product-of-two-elements-in-an-array/)
- [1913. Maximum Product Difference Between Two Pairs](../2042-maximum-product-difference-between-two-pairs/)
- [3090. Maximum Length Substring With Two Occurrences](../3349-maximum-length-substring-with-two-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/)
