# LeetCode 4024: Nearest Available Drone

**LeetCode Problem #4024 — Nearest Available Drone**
Solve LeetCode Nearest Available Drone using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Nearest Available Drone |
| LeetCode | #4024 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a 2D integer array  drones , where  drones[i] = [x i , y i , range i ]  represents the x-coordinate, y-coordinate, and travel range of the  i th   drone.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Nearest Available Drone**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1779. Find Nearest Point That Has the Same X or Y Coordinate](../../1501-2000/1888-find-nearest-point-that-has-the-same-x-or-y-coordinate/)
- [1926. Nearest Exit from Entrance in Maze](../../2001-2500/2038-nearest-exit-from-entrance-in-maze/)
- [999. Available Captures for Rook](../../1001-1500/1041-available-captures-for-rook/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/nearest-available-drone/)
