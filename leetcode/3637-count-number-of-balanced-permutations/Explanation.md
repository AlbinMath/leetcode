# LeetCode 3343: Count Number of Balanced Permutations

**LeetCode Problem #3343 — Count Number of Balanced Permutations**
Solve LeetCode Count Number of Balanced Permutations using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Balanced Permutations |
| LeetCode | #3343 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  num . A string of digits is called  balanced  if the sum of the digits at even indices is equal to the sum of the digits at odd indices.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Backtracking Recursive Search**. By maintaining state efficiently in a **Recursion Tree**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree**).
2. Process elements sequentially using **Backtracking Recursive Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Number of Balanced Permutations**. Applying **Backtracking Recursive Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3577. Count the Number of Computer Unlocking Permutations](../3864-count-the-number-of-computer-unlocking-permutations/)
- [1248. Count Number of Nice Subarrays](../1370-count-number-of-nice-subarrays/)
- [1395. Count Number of Teams](../1511-count-number-of-teams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-balanced-permutations/)
