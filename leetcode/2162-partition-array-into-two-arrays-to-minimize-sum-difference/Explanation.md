# LeetCode 2035: Partition Array Into Two Arrays to Minimize Sum Difference

**LeetCode Problem #2035 — Partition Array Into Two Arrays to Minimize Sum Difference**
Solve LeetCode Partition Array Into Two Arrays to Minimize Sum Difference using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array Into Two Arrays to Minimize Sum Difference |
| LeetCode | #2035 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums  of  2 * n  integers. You need to partition  nums  into  two  arrays of length  n  to  minimize the absolute difference  of the  sums  of the arrays. To partition  nums , put each element of  nums  into  one  of the two arrays.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Partition Array Into Two Arrays to Minimize Sum Difference**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3566. Partition Array into Two Equal Product Subsets](../3843-partition-array-into-two-equal-product-subsets/)
- [3069. Distribute Elements Into Two Arrays I](../3347-distribute-elements-into-two-arrays-i/)
- [3072. Distribute Elements Into Two Arrays II](../3350-distribute-elements-into-two-arrays-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/)
