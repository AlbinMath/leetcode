# LeetCode 1637: Widest Vertical Area Between Two Points Containing No Points

**LeetCode Problem #1637 — Widest Vertical Area Between Two Points Containing No Points**
Solve LeetCode Widest Vertical Area Between Two Points Containing No Points using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Widest Vertical Area Between Two Points Containing No Points |
| LeetCode | #1637 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given  n   points  on a 2D plane where  points[i] = [x i , y i ] , Return  the  widest vertical area  between two points such that no points are inside the area.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Widest Vertical Area Between Two Points Containing No Points**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3047. Find the Largest Area of Square Inside Two Rectangles](../../3001-3500/3325-find-the-largest-area-of-square-inside-two-rectangles/)
- [1595. Minimum Cost to Connect Two Groups of Points](../../1501-2000/1717-minimum-cost-to-connect-two-groups-of-points/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/)
