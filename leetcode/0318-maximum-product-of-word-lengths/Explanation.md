# LeetCode 318: Maximum Product of Word Lengths

**LeetCode Problem #318 — Maximum Product of Word Lengths**
Solve LeetCode Maximum Product of Word Lengths using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Word Lengths |
| LeetCode | #318 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string array  words , return  the maximum value of   length(word[i]) * length(word[j])   where the two words do not share common letters . If no such two words exist, return  0 .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Product of Word Lengths**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [152. Maximum Product Subarray](../0152-maximum-product-subarray/)
- [628. Maximum Product of Three Numbers](../0628-maximum-product-of-three-numbers/)
- [1339. Maximum Product of Splitted Binary Tree](../1465-maximum-product-of-splitted-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-word-lengths/)
