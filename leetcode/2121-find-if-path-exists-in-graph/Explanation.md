# LeetCode 1971: Find if Path Exists in Graph

**LeetCode Problem #1971 — Find if Path Exists in Graph**
Solve LeetCode Find if Path Exists in Graph using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find if Path Exists in Graph |
| LeetCode | #1971 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is a  bi-directional  graph with  n  vertices, where each vertex is labeled from  0  to  n - 1  ( inclusive ). The edges in the graph are represented as a 2D integer array  edges , where each  edges[i] = [u i , v i ]  denotes a bi-directional edge between vertex  u i   and vertex  v i  . Every vertex pair is connected by  at most one  edge, and no vertex has an edge to itself.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find if Path Exists in Graph**. Applying **Memoization & State Transition** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1791. Find Center of Star Graph](../1916-find-center-of-star-graph/)
- [2267.  Check if There Is a Valid Parentheses String Path](../2349--check-if-there-is-a-valid-parentheses-string-path/)
- [2267.  Check if There Is a Valid Parentheses String Path](../2349-check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-if-path-exists-in-graph/)
