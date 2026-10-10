# LeetCode 1523: Count Odd Numbers in an Interval Range

**LeetCode Problem #1523 — Count Odd Numbers in an Interval Range**
Solve LeetCode Count Odd Numbers in an Interval Range using Python and Greedy. This solution finds the optimal result using Greedy Choice Strategy in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Odd Numbers in an Interval Range |
| LeetCode | #1523 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Greedy Choice Strategy |
| Data Structure | Array / Priority Queue |
| Pattern | Greedy |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two non-negative integers  low  and   high  . Return the  count of odd numbers between   low   and    high    (inclusive) .

## Key Insight
Leverage **Greedy** with **Array / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Greedy Choice Strategy**. By maintaining state efficiently in a **Array / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Priority Queue**).
2. Process elements sequentially using **Greedy Choice Strategy**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Odd Numbers in an Interval Range**. Applying **Greedy Choice Strategy** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Greedy**

## Topics
- Greedy
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [1351. Count Negative Numbers in a Sorted Matrix](../1476-count-negative-numbers-in-a-sorted-matrix/)
- [3751. Total Waviness of Numbers in Range I](../4057-total-waviness-of-numbers-in-range-i/)
- [3753. Total Waviness of Numbers in Range II](../4128-total-waviness-of-numbers-in-range-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)
