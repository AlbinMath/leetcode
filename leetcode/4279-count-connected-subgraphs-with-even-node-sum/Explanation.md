# LeetCode 3910: Count Connected Subgraphs with Even Node Sum

**LeetCode Problem #3910 — Count Connected Subgraphs with Even Node Sum**
Solve LeetCode Count Connected Subgraphs with Even Node Sum using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Connected Subgraphs with Even Node Sum |
| LeetCode | #3910 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an undirected graph with  n  nodes labeled from 0 to  n - 1 . Node  i  has a  value  of  nums[i] , which is either 0 or 1. The edges of the graph are given by a 2D array  edges  where  edges[i] = [u i , v i ]  represents an edge between node  u i   and node  v i  .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Connected Subgraphs with Even Node Sum**. Applying **Memoization & State Transition** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [2180. Count Integers With Even Digit Sum](../2298-count-integers-with-even-digit-sum/)
- [327. Count of Range Sum](../0327-count-of-range-sum/)
- [1925. Count Square Sum Triples](../2037-count-square-sum-triples/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/)
