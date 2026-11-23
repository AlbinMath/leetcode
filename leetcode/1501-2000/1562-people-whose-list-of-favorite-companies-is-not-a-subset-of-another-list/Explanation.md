# LeetCode 1452: People Whose List of Favorite Companies Is Not a Subset of Another List

**LeetCode Problem #1452 — People Whose List of Favorite Companies Is Not a Subset of Another List**
Solve LeetCode People Whose List of Favorite Companies Is Not a Subset of Another List using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | People Whose List of Favorite Companies Is Not a Subset of Another List |
| LeetCode | #1452 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given the array  favoriteCompanies  where  favoriteCompanies[i]  is the list of favorites companies for the  ith  person ( indexed from 0 ).

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **People Whose List of Favorite Companies Is Not a Subset of Another List**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1978. Employees Whose Manager Left the Company](../../2001-2500/2127-employees-whose-manager-left-the-company/)
- [620. Not Boring Movies](../../0501-1000/0620-not-boring-movies/)
- [1581. Customer Who Visited but Did Not Make Any Transactions](../../1501-2000/1724-customer-who-visited-but-did-not-make-any-transactions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)
