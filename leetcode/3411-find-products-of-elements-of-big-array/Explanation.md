# LeetCode 3145: Find Products of Elements of Big Array

**LeetCode Problem #3145 — Find Products of Elements of Big Array**
Solve LeetCode Find Products of Elements of Big Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Products of Elements of Big Array |
| LeetCode | #3145 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
The  powerful array  of a non-negative integer  x  is defined as the shortest sorted array of powers of two that sum up to  x . The table below illustrates examples of how the  powerful array  is determined. It can be proven that the powerful array of  x  is unique.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Products of Elements of Big Array**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2593. Find Score of an Array After Marking All Elements](../2695-find-score-of-an-array-after-marking-all-elements/)
- [34. Find First and Last Position of Element in Sorted Array](../0034-find-first-and-last-position-of-element-in-sorted-array/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-products-of-elements-of-big-array/)
