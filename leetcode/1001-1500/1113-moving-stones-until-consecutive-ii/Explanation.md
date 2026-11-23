# LeetCode 1040: Moving Stones Until Consecutive II

**LeetCode Problem #1040 — Moving Stones Until Consecutive II**
Solve LeetCode Moving Stones Until Consecutive II using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Moving Stones Until Consecutive II |
| LeetCode | #1040 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are some stones in different positions on the X-axis. You are given an integer array  stones , the positions of the stones.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Moving Stones Until Consecutive II**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [1033. Moving Stones Until Consecutive](../../1001-1500/1103-moving-stones-until-consecutive/)
- [771. Jewels and Stones](../../0501-1000/0782-jewels-and-stones/)
- [947. Most Stones Removed with Same Row or Column](../../0501-1000/0984-most-stones-removed-with-same-row-or-column/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/moving-stones-until-consecutive-ii/)
