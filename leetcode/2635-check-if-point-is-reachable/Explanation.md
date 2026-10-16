# LeetCode 2543: Check if Point Is Reachable

**LeetCode Problem #2543 — Check if Point Is Reachable**
Solve LeetCode Check if Point Is Reachable using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Point Is Reachable |
| LeetCode | #2543 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There exists an infinitely large grid. You are currently at point  (1, 1) , and you need to reach the point  (targetX, targetY)  using a finite number of steps.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check if Point Is Reachable**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1232. Check If It Is a Straight Line](../1349-check-if-it-is-a-straight-line/)
- [1250. Check If It Is a Good Array](../1372-check-if-it-is-a-good-array/)
- [1346. Check If N and Its Double Exist](../1468-check-if-n-and-its-double-exist/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-point-is-reachable/)
