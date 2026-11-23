# LeetCode 2271: Maximum White Tiles Covered by a Carpet

**LeetCode Problem #2271 — Maximum White Tiles Covered by a Carpet**
Solve LeetCode Maximum White Tiles Covered by a Carpet using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum White Tiles Covered by a Carpet |
| LeetCode | #2271 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a 2D integer array  tiles  where  tiles[i] = [l i , r i ]  represents that every tile  j  in the range  l i  <= j <= r i   is colored white.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum White Tiles Covered by a Carpet**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2397. Maximum Rows Covered by Columns](../2482-maximum-rows-covered-by-columns/)
- [53. Maximum Subarray](../0053-maximum-subarray/)
- [104. Maximum Depth of Binary Tree](../0104-maximum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/)
