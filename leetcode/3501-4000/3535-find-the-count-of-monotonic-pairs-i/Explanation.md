# LeetCode 3250: Find the Count of Monotonic Pairs I

**LeetCode Problem #3250 — Find the Count of Monotonic Pairs I**
Solve LeetCode Find the Count of Monotonic Pairs I using JavaScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Count of Monotonic Pairs I |
| LeetCode | #3250 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array of  positive  integers  nums  of length  n .

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
We iterate through the input using **Monotonic Stack Filtering**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Count of Monotonic Pairs I**. Applying **Monotonic Stack Filtering** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [3251. Find the Count of Monotonic Pairs II](../../3501-4000/3536-find-the-count-of-monotonic-pairs-ii/)
- [1729. Find Followers Count](../../1501-2000/1877-find-followers-count/)
- [1782. Count Pairs Of Nodes](../../1501-2000/1891-count-pairs-of-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/)
