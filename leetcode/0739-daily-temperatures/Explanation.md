# LeetCode 739: Daily Temperatures

**LeetCode Problem #739 — Daily Temperatures**
Solve LeetCode Daily Temperatures using TypeScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Daily Temperatures |
| LeetCode | #739 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an array of integers  temperatures  represents the daily temperatures, return  an array   answer   such that   answer[i]   is the number of days you have to wait after the   i th    day to get a warmer temperature . If there is no future day for which this is possible, keep  answer[i] == 0  instead.

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
The code uses a **Monotonic Stack** (decreasing) to efficiently find the next warmer day for each index.

1. **Stack of Indices:** The stack stores indices of days whose "next warmer day" hasn't been found yet, in decreasing order of temperature.
2. **Iteration:** For each day `i`:
   - While the stack is not empty and `temperatures[i]` is greater than the temperature at the index on top of the stack: pop the index `prev` and set `result[prev] = i - prev`.
   - Push `i` onto the stack.
3. Any indices remaining in the stack after the loop already have `result[i] = 0` (initialized at the start).

Time complexity is $O(N)$ (each index is pushed and popped at most once) and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Daily Temperatures**. Applying **Monotonic Stack Filtering** yields the target result step by step.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [1837. Sum of Digits in Base K](../1837-daily-leads-and-partners/)
- [84. Largest Rectangle in Histogram](../0084-largest-rectangle-in-histogram/)
- [1159. Market Analysis II](../1159-smallest-subsequence-of-distinct-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/daily-temperatures/)
