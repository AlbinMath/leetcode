# LeetCode 744: Find Smallest Letter Greater Than Target

**LeetCode Problem #744 — Find Smallest Letter Greater Than Target**
Solve LeetCode Find Smallest Letter Greater Than Target using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Smallest Letter Greater Than Target |
| LeetCode | #744 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of characters  letters  that is sorted in  non-decreasing order , and a character  target . There are  at least two different  characters in  letters .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Smallest Letter Greater Than Target**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3720. Lexicographically Smallest Permutation Greater Than Target](../4020-lexicographically-smallest-permutation-greater-than-target/)
- [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](../4037-lexicographically-smallest-palindromic-permutation-greater-than-target/)
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
