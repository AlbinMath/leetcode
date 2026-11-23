# LeetCode 1232: Check If It Is a Straight Line

**LeetCode Problem #1232 — Check If It Is a Straight Line**
Solve LeetCode Check If It Is a Straight Line using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If It Is a Straight Line |
| LeetCode | #1232 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  coordinates ,  coordinates[i] = [x, y] , where  [x, y]  represents the coordinate of a point. Check if these points make a straight line in the XY plane.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check If It Is a Straight Line**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2267.  Check if There Is a Valid Parentheses String Path](../2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1250. Check If It Is a Good Array](../1372-check-if-it-is-a-good-array/)
- [1003. Check If Word Is Valid After Substitutions](../1045-check-if-word-is-valid-after-substitutions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-it-is-a-straight-line/)
