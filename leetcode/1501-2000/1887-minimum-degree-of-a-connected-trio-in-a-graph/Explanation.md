# LeetCode 1761: Minimum Degree of a Connected Trio in a Graph

**LeetCode Problem #1761 — Minimum Degree of a Connected Trio in a Graph**
Solve LeetCode Minimum Degree of a Connected Trio in a Graph using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Degree of a Connected Trio in a Graph |
| LeetCode | #1761 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an undirected graph. You are given an integer  n  which is the number of nodes in the graph and an array  edges , where each  edges[i] = [u i , v i ]  indicates that there is an undirected edge between  u i   and  v i  .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Degree of a Connected Trio in a Graph**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [3378. Count Connected Components in LCM Graph](../../3501-4000/3680-count-connected-components-in-lcm-graph/)
- [3608. Minimum Time for K Connected Components](../../3501-4000/3908-minimum-time-for-k-connected-components/)
- [3108. Minimum Cost Walk in Weighted Graph](../../3001-3500/3348-minimum-cost-walk-in-weighted-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/)
