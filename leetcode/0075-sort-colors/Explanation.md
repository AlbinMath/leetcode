# LeetCode 75: Sort Colors

**LeetCode Problem #75 — Sort Colors**
Solve LeetCode Sort Colors using PHP and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Colors |
| LeetCode | #75 |
| Difficulty | Medium |
| Language | PHP |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array  nums  with  n  objects colored red, white, or blue, sort them   in-place   so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sort Colors**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
PHP

## Source Code
- [solution.php](./solution.php)

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
- [905. Sort Array By Parity](../0941-sort-array-by-parity/)
- [922. Sort Array By Parity II](../0958-sort-array-by-parity-ii/)
- [1122. Relative Sort Array](../1217-relative-sort-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-colors/)
