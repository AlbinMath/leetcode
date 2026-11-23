# LeetCode 1638: Count Substrings That Differ by One Character

**LeetCode Problem #1638 — Count Substrings That Differ by One Character**
Solve LeetCode Count Substrings That Differ by One Character using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Substrings That Differ by One Character |
| LeetCode | #1638 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two strings  s  and  t , find the number of ways you can choose a non-empty substring of  s  and replace a  single character  by a different character such that the resulting substring is a substring of  t . In other words, find the number of substrings in  s  that differ from some substring in  t  by  exactly  one character.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Substrings That Differ by One Character**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3258. Count Substrings That Satisfy K-Constraint I](../3543-count-substrings-that-satisfy-k-constraint-i/)
- [3261. Count Substrings That Satisfy K-Constraint II](../3546-count-substrings-that-satisfy-k-constraint-ii/)
- [3297. Count Substrings That Can Be Rearranged to Contain a String I](../3573-count-substrings-that-can-be-rearranged-to-contain-a-string-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-substrings-that-differ-by-one-character/)
