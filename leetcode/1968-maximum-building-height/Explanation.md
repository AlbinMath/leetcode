# LeetCode 1968: Array With Elements Not Equal to Average of Neighbors

**LeetCode Problem #1968 — Array With Elements Not Equal to Average of Neighbors**
Solve LeetCode Array With Elements Not Equal to Average of Neighbors using Python and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Array With Elements Not Equal to Average of Neighbors |
| LeetCode | #1968 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You want to build  n  new buildings in a city. The new buildings will be built in a line and are labeled from  1  to  n .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **two-pass constraint propagation**.

1. Add restriction `[1, 0]` (building 1 must be height 0) and sort by building ID.
2. **Left-to-right pass:** Each restriction is tightened so it doesn't exceed the previous restriction's height + distance between them.
3. **Right-to-left pass:** Same tightening from the other direction.
4. **Calculate peaks:** Between each pair of consecutive restricted buildings, the maximum achievable peak is `(h1 + h2 + distance) / 2`.
5. Also check the height achievable after the last restriction (increases by 1 per building up to building `n`).

Time complexity is $O(M \log M)$ where $M$ is the number of restrictions, and space complexity is $O(M)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Array With Elements Not Equal to Average of Neighbors**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [628. Maximum Product of Three Numbers](../0628-maximum-product-of-three-numbers/)
- [1186. Maximum Subarray Sum with One Deletion](../1186-building-h2o/)
- [1208. Get Equal Substrings Within Budget](../1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-building-height/)
