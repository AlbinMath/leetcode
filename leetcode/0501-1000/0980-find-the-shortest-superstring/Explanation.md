# LeetCode 943: Find the Shortest Superstring

**LeetCode Problem #943 — Find the Shortest Superstring**
Solve LeetCode Find the Shortest Superstring using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Shortest Superstring |
| LeetCode | #943 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of strings  words , return  the smallest string that contains each string in   words   as a substring . If there are multiple valid strings of the smallest length, return  any of them .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Shortest Superstring**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3123. Find Edges in Shortest Paths](../../3001-3500/3386-find-edges-in-shortest-paths/)
- [214. Shortest Palindrome](../../0001-0500/0214-shortest-palindrome/)
- [581. Shortest Unsorted Continuous Subarray](../../0501-1000/0581-shortest-unsorted-continuous-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-shortest-superstring/)
