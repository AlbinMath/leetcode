# LeetCode 2022: Convert 1D Array Into 2D Array

**LeetCode Problem #2022 — Convert 1D Array Into 2D Array**
Solve LeetCode Convert 1D Array Into 2D Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Convert 1D Array Into 2D Array |
| LeetCode | #2022 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  1-dimensional (1D) integer array  original , and two integers,  m  and  n . You are tasked with creating a 2-dimensional (2D) array with   m  rows and  n  columns using  all  the elements from  original .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Convert 1D Array Into 2D Array**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [842. Split Array into Fibonacci Sequence](../0872-split-array-into-fibonacci-sequence/)
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../2162-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [2206. Divide Array Into Equal Pairs](../2308-divide-array-into-equal-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/convert-1d-array-into-2d-array/)
