# LeetCode 1976: Number of Ways to Arrive at Destination

**LeetCode Problem #1976 — Number of Ways to Arrive at Destination**
Solve LeetCode Number of Ways to Arrive at Destination using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Arrive at Destination |
| LeetCode | #1976 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are in a city that consists of  n  intersections numbered from  0  to  n - 1  with  bi-directional  roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Ways to Arrive at Destination**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1569. Number of Ways to Reorder Array to Get Same BST](../1692-number-of-ways-to-reorder-array-to-get-same-bst/)
- [1866. Number of Ways to Rearrange Sticks With K Sticks Visible](../1996-number-of-ways-to-rearrange-sticks-with-k-sticks-visible/)
- [3558. Number of Ways to Assign Edge Weights I](../3844-number-of-ways-to-assign-edge-weights-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)
