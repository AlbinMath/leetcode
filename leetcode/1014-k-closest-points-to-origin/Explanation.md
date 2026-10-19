# LeetCode 973: K Closest Points to Origin

**LeetCode Problem #973 — K Closest Points to Origin**
Solve LeetCode K Closest Points to Origin using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K Closest Points to Origin |
| LeetCode | #973 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of  points  where  points[i] = [x i , y i ]  represents a point on the  X-Y  plane and an integer  k , return the  k  closest points to the origin  (0, 0) .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **K Closest Points to Origin**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [658. Find K Closest Elements](../0658-find-k-closest-elements/)
- [16. 3Sum Closest](../0016-3sum-closest/)
- [23. Merge k Sorted Lists](../0023-merge-k-sorted-lists/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/)
