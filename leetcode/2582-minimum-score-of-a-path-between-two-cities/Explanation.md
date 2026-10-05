# LeetCode 2582: Pass the Pillow

**LeetCode Problem #2582 — Pass the Pillow**
Solve LeetCode Pass the Pillow using Java and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Pass the Pillow |
| LeetCode | #2582 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a positive integer  n  representing  n  cities numbered from  1  to  n . You are also given a  2D  array  roads  where  roads[i] = [a i , b i , distance i ]  indicates that there is a  bidirectional  road between cities  a i   and  b i   with a distance equal to  distance i  . The cities graph is not necessarily connected.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Since you can traverse any edge multiple times, the answer is the minimum edge weight in the connected component containing cities 1 and n. Use **BFS/DFS** or **Union-Find** to find all reachable nodes from city 1 and track the minimum edge weight.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Pass the Pillow**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Database / SQL**

## Topics
- Database
- SQL
- Data Aggregation

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Database / SQL**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2182. Construct String With Repeat Limit](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [3986. Number of Elapsed Seconds Between Two Times](../3986-maximum-path-score-in-a-grid/)
- [1. Two Sum](../0001-two-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)
