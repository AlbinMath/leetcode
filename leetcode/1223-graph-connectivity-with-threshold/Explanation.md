# LeetCode 1627: Graph Connectivity With Threshold

**LeetCode Problem #1627 — Graph Connectivity With Threshold**
Solve LeetCode Graph Connectivity With Threshold using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Graph Connectivity With Threshold |
| LeetCode | #1627 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
We have  n  cities labeled from  1  to  n . Two different cities with labels  x  and  y  are directly connected by a bidirectional road if and only if  x  and  y  share a common divisor  strictly greater  than some  threshold . More formally, cities with labels  x  and  y  have a road between them if there exists an integer  z  such that all of the following are true:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Graph Connectivity With Threshold**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](../1413-maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/graph-connectivity-with-threshold/)
