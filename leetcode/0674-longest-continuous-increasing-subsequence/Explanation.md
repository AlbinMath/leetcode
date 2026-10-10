# LeetCode 674: Longest Continuous Increasing Subsequence

**LeetCode Problem #674 — Longest Continuous Increasing Subsequence**
Solve LeetCode Longest Continuous Increasing Subsequence using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Continuous Increasing Subsequence |
| LeetCode | #674 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an unsorted array of integers  nums , return  the length of the longest  continuous increasing subsequence  (i.e. subarray) . The subsequence must be  strictly  increasing.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Continuous Increasing Subsequence**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [521. Longest Uncommon Subsequence I](../0521-longest-uncommon-subsequence-i/)
- [594. Longest Harmonious Subsequence](../0594-longest-harmonious-subsequence/)
- [1403. Minimum Subsequence in Non-Increasing Order](../1519-minimum-subsequence-in-non-increasing-order/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)
