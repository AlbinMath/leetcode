# LeetCode 3165: Maximum Sum of Subsequence With Non-adjacent Elements

**LeetCode Problem #3165 — Maximum Sum of Subsequence With Non-adjacent Elements**
Solve LeetCode Maximum Sum of Subsequence With Non-adjacent Elements using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of Subsequence With Non-adjacent Elements |
| LeetCode | #3165 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array  nums  consisting of integers. You are also given a 2D array  queries , where  queries[i] = [pos i , x i ] .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Sum of Subsequence With Non-adjacent Elements**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../1096-maximum-sum-of-two-non-overlapping-subarrays/)
- [3956. Maximum Sum of M Non-Overlapping Subarrays I](../4123-maximum-sum-of-m-non-overlapping-subarrays-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/)
