# LeetCode 2550: Count Collisions of Monkeys on a Polygon

**LeetCode Problem #2550 — Count Collisions of Monkeys on a Polygon**
Solve LeetCode Count Collisions of Monkeys on a Polygon using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Collisions of Monkeys on a Polygon |
| LeetCode | #2550 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a regular convex polygon with  n  vertices. The vertices are labeled from  0  to  n - 1  in a clockwise direction, and each vertex has  exactly one monkey . The following figure shows a convex polygon of  6  vertices.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Collisions of Monkeys on a Polygon**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2211. Count Collisions on a Road](../2317-count-collisions-on-a-road/)
- [38. Count and Say](../0038-count-and-say/)
- [204. Count Primes](../0204-count-primes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/)
