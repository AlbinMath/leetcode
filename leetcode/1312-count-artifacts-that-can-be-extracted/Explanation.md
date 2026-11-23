# LeetCode 2201: Count Artifacts That Can Be Extracted

**LeetCode Problem #2201 — Count Artifacts That Can Be Extracted**
Solve LeetCode Count Artifacts That Can Be Extracted using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Artifacts That Can Be Extracted |
| LeetCode | #2201 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is an  n x n   0-indexed  grid with some artifacts buried in it. You are given the integer  n  and a  0-indexed  2D integer array  artifacts  describing the positions of the rectangular artifacts where  artifacts[i] = [r1 i , c1 i , r2 i , c2 i ]  denotes that the  i th   artifact is buried in the subgrid where:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Artifacts That Can Be Extracted**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3297. Count Substrings That Can Be Rearranged to Contain a String I](../3573-count-substrings-that-can-be-rearranged-to-contain-a-string-i/)
- [3298. Count Substrings That Can Be Rearranged to Contain a String II](../3572-count-substrings-that-can-be-rearranged-to-contain-a-string-ii/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../1553-count-triplets-that-can-form-two-arrays-of-equal-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/)
