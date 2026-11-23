# LeetCode 3286: Find a Safe Walk Through a Grid

**LeetCode Problem #3286 — Find a Safe Walk Through a Grid**
Solve LeetCode Find a Safe Walk Through a Grid using Java and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find a Safe Walk Through a Grid |
| LeetCode | #3286 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an  m x n  binary matrix  grid  and an integer  health .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find a Safe Walk Through a Grid**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2812. Find the Safest Path in a Grid](../../2501-3000/2914-find-the-safest-path-in-a-grid/)
- [802. Find Eventual Safe States](../../0501-1000/0820-find-eventual-safe-states/)
- [840. Magic Squares In Grid](../../0501-1000/0870-magic-squares-in-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/)
