# LeetCode 315: Count of Smaller Numbers After Self

**LeetCode Problem #315 — Count of Smaller Numbers After Self**
Solve LeetCode Count of Smaller Numbers After Self using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count of Smaller Numbers After Self |
| LeetCode | #315 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums , return  an integer array   counts   where   counts[i]   is the number of smaller elements to the right of   nums[i] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count of Smaller Numbers After Self**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [728. Self Dividing Numbers](../0728-self-dividing-numbers/)
- [1351. Count Negative Numbers in a Sorted Matrix](../1476-count-negative-numbers-in-a-sorted-matrix/)
- [1365. How Many Numbers Are Smaller Than the Current Number](../1482-how-many-numbers-are-smaller-than-the-current-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
