# LeetCode 1928: Minimum Cost to Reach Destination in Time

**LeetCode Problem #1928 — Minimum Cost to Reach Destination in Time**
Solve LeetCode Minimum Cost to Reach Destination in Time using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Reach Destination in Time |
| LeetCode | #1928 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a country of  n  cities numbered from  0  to  n - 1  where  all the cities are connected  by bi-directional roads. The roads are represented as a 2D integer array  edges  where  edges[i] = [x i , y i , time i ]  denotes a road between cities  x i   and  y i   that takes  time i   minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Cost to Reach Destination in Time**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2045. Second Minimum Time to Reach Destination](../../2001-2500/2171-second-minimum-time-to-reach-destination/)
- [3604. Minimum Time to Reach Destination in Directed Graph](../../3501-4000/3916-minimum-time-to-reach-destination-in-directed-graph/)
- [2162. Minimum Cost to Set Cooking Time](../../2001-2500/2266-minimum-cost-to-set-cooking-time/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/)
