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
- [1346. Check If N and Its Double Exist](../1468-check-if-n-and-its-double-exist/)
- [1437. Check If All 1's Are at Least Length K Places Away](../1548-check-if-all-1s-are-at-least-length-k-places-away/)
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../1566-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-it-is-a-straight-line/)
