# LeetCode 787: Cheapest Flights Within K Stops

**LeetCode Problem #787 — Cheapest Flights Within K Stops**
Solve LeetCode Cheapest Flights Within K Stops using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cheapest Flights Within K Stops |
| LeetCode | #787 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are  n  cities connected by some number of flights. You are given an array  flights  where  flights[i] = [from i , to i , price i ]  indicates that there is a flight from city  from i   to city  to i   with cost  price i  .

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Min/Max Heap Priority Selection**. By maintaining state efficiently in a **Heap / Priority Queue**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Cheapest Flights Within K Stops**. Applying **Min/Max Heap Priority Selection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2146. K Highest Ranked Items Within a Price Range](../../2001-2500/2250-k-highest-ranked-items-within-a-price-range/)
- [3505. Minimum Operations to Make Elements Within K Subarrays Equal](../../3501-4000/3717-minimum-operations-to-make-elements-within-k-subarrays-equal/)
- [1208. Get Equal Substrings Within Budget](../../1001-1500/1321-get-equal-substrings-within-budget/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
