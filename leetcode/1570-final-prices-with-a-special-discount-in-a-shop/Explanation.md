# LeetCode 1475: Final Prices With a Special Discount in a Shop

**LeetCode Problem #1475 — Final Prices With a Special Discount in a Shop**
Solve LeetCode Final Prices With a Special Discount in a Shop using TypeScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Final Prices With a Special Discount in a Shop |
| LeetCode | #1475 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  prices  where  prices[i]  is the price of the  i th   item in a shop.

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
The code uses a **Monotonic Stack** to efficiently find the next smaller or equal element for each index. It processes prices left to right, maintaining a stack of indices with unresolved discounts. When a price that qualifies as a discount is found, all applicable items on the stack get their discount applied.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Final Prices With a Special Discount in a Shop**. Applying **Monotonic Stack Filtering** yields the target result step by step.

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
- [1608. Special Array With X Elements Greater Than or Equal X](../1730-special-array-with-x-elements-greater-than-or-equal-x/)
- [1873. Calculate Special Bonus](../2024-calculate-special-bonus/)
- [1974. Minimum Time to Type Word Using Special Typewriter](../2088-minimum-time-to-type-word-using-special-typewriter/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)
