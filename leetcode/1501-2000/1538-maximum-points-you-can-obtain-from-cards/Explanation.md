# LeetCode 1423: Maximum Points You Can Obtain from Cards

**LeetCode Problem #1423 — Maximum Points You Can Obtain from Cards**
Solve LeetCode Maximum Points You Can Obtain from Cards using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Points You Can Obtain from Cards |
| LeetCode | #1423 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are several cards  arranged in a row , and each card has an associated number of points. The points are given in the integer array  cardPoints .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Points You Can Obtain from Cards**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1424-maximum-candies-you-can-get-from-boxes/)
- [3114. Latest Time You Can Obtain After Replacing Characters](../../3001-3500/3361-latest-time-you-can-obtain-after-replacing-characters/)
- [2503. Maximum Number of Points From Grid Queries](../../2501-3000/2588-maximum-number-of-points-from-grid-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)
