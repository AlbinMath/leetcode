# LeetCode 2882: Drop Duplicate Rows

**LeetCode Problem #2882 — Drop Duplicate Rows**
Solve LeetCode Drop Duplicate Rows using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Drop Duplicate Rows |
| LeetCode | #2882 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There are some duplicate rows in the DataFrame based on the  email  column.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Drop Duplicate Rows**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2883. Drop Missing Data](../../3001-3500/3075-drop-missing-data/)
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1147-flip-columns-for-maximum-number-of-equal-rows/)
- [1337. The K Weakest Rows in a Matrix](../../1001-1500/1463-the-k-weakest-rows-in-a-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/drop-duplicate-rows/)
