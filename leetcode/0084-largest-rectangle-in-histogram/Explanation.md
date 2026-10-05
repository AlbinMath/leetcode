# LeetCode 84: Largest Rectangle in Histogram

**LeetCode Problem #84 — Largest Rectangle in Histogram**
Solve LeetCode Largest Rectangle in Histogram using TypeScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Rectangle in Histogram |
| LeetCode | #84 |
| Difficulty | Hard |
| Language | TypeScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an array of integers  heights  representing the histogram&#39;s bar height where the width of each bar is  1 , return  the area of the largest rectangle in the histogram .

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
The code uses a **Monotonic Stack** to efficiently compute the largest rectangle in $O(N)$ time.

1. **Stack of Indices:** The stack stores indices of bars in increasing order of their heights.
2. **Iteration:** It iterates from index `0` to `heights.length` (inclusive). At index `heights.length`, a virtual bar of height `0` is used to flush all remaining bars from the stack.
3. **Popping Taller Bars:** Whenever the current bar's height is less than the bar at the top of the stack, bars are popped. For each popped bar:
   - The `height` is the height of the popped bar.
   - The `width` extends from the current index `i` back to the bar just after the new top of the stack. If the stack is empty, the width is `i` (extends all the way to the left).
   - The area `height * width` is computed and `maxArea` is updated.
4. **Push Current Index:** The current index is pushed onto the stack.

The stack ensures each bar is pushed and popped at most once, giving $O(N)$ time complexity and $O(N)$ space complexity.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Rectangle in Histogram**. Applying **Monotonic Stack Filtering** yields the target result step by step.

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
- [586. Customer Placing the Largest Number of Orders](../0586-customer-placing-the-largest-number-of-orders/)
- [866. Prime Palindrome](../0866-rectangle-overlap/)
- [1501. Countries You Can Safely Invest In](../1501-circle-and-rectangle-overlapping/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/)
