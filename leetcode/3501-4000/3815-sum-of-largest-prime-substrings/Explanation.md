# LeetCode 3556: Sum of Largest Prime Substrings

**LeetCode Problem #3556 — Sum of Largest Prime Substrings**
Solve LeetCode Sum of Largest Prime Substrings using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Largest Prime Substrings |
| LeetCode | #3556 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s , find the sum of the  3 largest unique  prime numbers   that can be formed using any of its   substrings  .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sum of Largest Prime Substrings**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3770. Largest Prime from Consecutive Prime Sum](../../4001-4500/4085-largest-prime-from-consecutive-prime-sum/)
- [1781. Sum of Beauty of All Substrings](../../1501-2000/1890-sum-of-beauty-of-all-substrings/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-largest-prime-substrings/)
