# LeetCode 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

**LeetCode Problem #1343 — Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold**
Solve LeetCode Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold |
| LeetCode | #1343 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of integers  arr  and two integers  k  and  threshold , return  the number of sub-arrays of size   k   and average greater than or equal to   threshold .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../../3001-3500/3240-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
- [3091. Apply Operations to Make Sum of Array Greater Than or Equal to k](../../3001-3500/3328-apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/)
- [1524. Number of Sub-arrays With Odd Sum](../../1501-2000/1631-number-of-sub-arrays-with-odd-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
