# LeetCode 3842: Toggle Light Bulbs

**LeetCode Problem #3842 — Toggle Light Bulbs**
Solve LeetCode Toggle Light Bulbs using Python and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Toggle Light Bulbs |
| LeetCode | #3842 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is an undirected tree with  n  nodes labeled from 1 to  n , rooted at node 1. The tree is represented by a 2D integer array  edges  of length  n - 1 , where  edges[i] = [u i , v i ]  indicates that there is an edge between nodes  u i   and  v i  .

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Relational Join & Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Toggle Light Bulbs**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [3844. Longest Almost-Palindromic Substring](../3844-number-of-ways-to-assign-edge-weights-i/)
- [3276. Select Cells in Grid With Maximum Score](../3276-minimum-number-of-pushes-to-type-word-ii/)
- [3820. Pythagorean Distance Nodes in a Tree](../3820-number-of-unique-xor-triplets-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/)
