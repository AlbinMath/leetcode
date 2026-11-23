# LeetCode 1595: Minimum Cost to Connect Two Groups of Points

**LeetCode Problem #1595 — Minimum Cost to Connect Two Groups of Points**
Solve LeetCode Minimum Cost to Connect Two Groups of Points using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Connect Two Groups of Points |
| LeetCode | #1595 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two groups of points where the first group has  size 1   points, the second group has  size 2   points, and  size 1  >= size 2  .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Cost to Connect Two Groups of Points**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1584. Min Cost to Connect All Points](../../1501-2000/1706-min-cost-to-connect-all-points/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1395-minimum-time-visiting-all-points/)
- [1637. Widest Vertical Area Between Two Points Containing No Points](../../1501-2000/1742-widest-vertical-area-between-two-points-containing-no-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/)
