# LeetCode 2276: Count Integers in Intervals

**LeetCode Problem #2276 — Count Integers in Intervals**
Solve LeetCode Count Integers in Intervals using JavaScript and Greedy. This solution finds the optimal result using Greedy Choice Strategy in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Integers in Intervals |
| LeetCode | #2276 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Greedy Choice Strategy |
| Data Structure | Array / Priority Queue |
| Pattern | Greedy |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an  empty  set of intervals, implement a data structure that can:

## Key Insight
Leverage **Greedy** with **Array / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Priority Queue**).
2. Process elements sequentially using **Greedy Choice Strategy**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Integers in Intervals**. Applying **Greedy Choice Strategy** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Greedy**

## Topics
- Greedy
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Greedy**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2180. Count Integers With Even Digit Sum](../2298-count-integers-with-even-digit-sum/)
- [2843.   Count Symmetric Integers](../2998---count-symmetric-integers/)
- [3272. Find the Count of Good Integers](../3548-find-the-count-of-good-integers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-integers-in-intervals/)
