# LeetCode 2913: Subarrays Distinct Element Sum of Squares I

**LeetCode Problem #2913 — Subarrays Distinct Element Sum of Squares I**
Solve LeetCode Subarrays Distinct Element Sum of Squares I using JavaScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subarrays Distinct Element Sum of Squares I |
| LeetCode | #2913 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  integer array  nums .

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Subarrays Distinct Element Sum of Squares I**. Applying **Monotonic Stack Filtering** yields the target result step by step.

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
- [2916. Subarrays Distinct Element Sum of Squares II](../3139-subarrays-distinct-element-sum-of-squares-ii/)
- [3737. Count Subarrays With Majority Element I](../4074-count-subarrays-with-majority-element-i/)
- [496. Next Greater Element I](../0496-next-greater-element-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/)
