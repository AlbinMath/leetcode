# LeetCode 1042: Flower Planting With No Adjacent

**LeetCode Problem #1042 — Flower Planting With No Adjacent**
Solve LeetCode Flower Planting With No Adjacent using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flower Planting With No Adjacent |
| LeetCode | #1042 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have  n  gardens, labeled from  1  to  n , and an array  paths  where  paths[i] = [x i , y i ]  describes a bidirectional path between garden  x i   to garden  y i  . In each garden, you want to plant one of 4 types of flowers.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Flower Planting With No Adjacent**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [363. Max Sum of Rectangle No Larger Than K](../../0001-0500/0363-max-sum-of-rectangle-no-larger-than-k/)
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1440-convert-integer-to-the-sum-of-two-no-zero-integers/)
- [1637. Widest Vertical Area Between Two Points Containing No Points](../../1501-2000/1742-widest-vertical-area-between-two-points-containing-no-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flower-planting-with-no-adjacent/)
