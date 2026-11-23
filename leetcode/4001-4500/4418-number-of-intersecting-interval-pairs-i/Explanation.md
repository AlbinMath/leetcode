# LeetCode 4056: Number of Intersecting Interval Pairs I

**LeetCode Problem #4056 — Number of Intersecting Interval Pairs I**
Solve LeetCode Number of Intersecting Interval Pairs I using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Intersecting Interval Pairs I |
| LeetCode | #4056 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a 2D integer array  intervals  of  n  elements, where  intervals[i] = [start i , end i ]  represents the  closed  interval from  start i   to  end i  .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Intersecting Interval Pairs I**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [1128. Number of Equivalent Domino Pairs](../../1001-1500/1227-number-of-equivalent-domino-pairs/)
- [1512. Number of Good Pairs](../../1501-2000/1635-number-of-good-pairs/)
- [1530. Number of Good Leaf Nodes Pairs](../../1501-2000/1653-number-of-good-leaf-nodes-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/)
