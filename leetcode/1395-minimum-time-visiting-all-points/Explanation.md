# LeetCode 1266: Minimum Time Visiting All Points

**LeetCode Problem #1266 — Minimum Time Visiting All Points**
Solve LeetCode Minimum Time Visiting All Points using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time Visiting All Points |
| LeetCode | #1266 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
On a 2D plane, there are  n  points with integer coordinates  points[i] = [x i , y i ] . Return  the  minimum time  in seconds to visit all the points in the order given by   points .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Time Visiting All Points**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1928. Minimum Cost to Reach Destination in Time](../2040-minimum-cost-to-reach-destination-in-time/)
- [1974. Minimum Time to Type Word Using Special Typewriter](../2088-minimum-time-to-type-word-using-special-typewriter/)
- [2045. Second Minimum Time to Reach Destination](../2171-second-minimum-time-to-reach-destination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-visiting-all-points/)
