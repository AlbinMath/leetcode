# LeetCode 1222: Queens That Can Attack the King

**LeetCode Problem #1222 — Queens That Can Attack the King**
Solve LeetCode Queens That Can Attack the King using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Queens That Can Attack the King |
| LeetCode | #1222 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
On a  0-indexed   8 x 8  chessboard, there can be multiple black queens and one white king.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Queens That Can Attack the King**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1160. Find Words That Can Be Formed by Characters](../1112-find-words-that-can-be-formed-by-characters/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../1553-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [1725. Number Of Rectangles That Can Form The Largest Square](../1843-number-of-rectangles-that-can-form-the-largest-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/queens-that-can-attack-the-king/)
