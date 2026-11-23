# LeetCode 4100: Minimum Cost Path With Even XOR Parity

**LeetCode Problem #4100 — Minimum Cost Path With Even XOR Parity**
Solve LeetCode Minimum Cost Path With Even XOR Parity using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Path With Even XOR Parity |
| LeetCode | #4100 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a tree with  n  nodes numbered from 0 to  n - 1 , represented by a 2D integer array  edges . Each  edges[i] = [u i , v i , c i ]  represents an edge between nodes  u i   and  v i   with cost  c i  .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Cost Path With Even XOR Parity**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2662. Minimum Cost of a Path With Special Roads](../2686-minimum-cost-of-a-path-with-special-roads/)
- [3650. Minimum Cost Path with Edge Reversals](../3887-minimum-cost-path-with-edge-reversals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-path-with-even-xor-parity/)
