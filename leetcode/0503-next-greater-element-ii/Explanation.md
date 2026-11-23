# LeetCode 503: Next Greater Element II

**LeetCode Problem #503 — Next Greater Element II**
Solve LeetCode Next Greater Element II using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Next Greater Element II |
| LeetCode | #503 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a circular integer array  nums  (i.e., the next element of  nums[nums.length - 1]  is  nums[0] ), return  the  next greater number  for every element in   nums .

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
We iterate through the input using **Monotonic Stack Filtering**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Next Greater Element II**. Applying **Monotonic Stack Filtering** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [496. Next Greater Element I](../0496-next-greater-element-i/)
- [556. Next Greater Element III](../0556-next-greater-element-iii/)
- [2454. Next Greater Element IV](../2549-next-greater-element-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/next-greater-element-ii/)
