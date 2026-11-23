# LeetCode 2813: Maximum Elegance of a K-Length Subsequence

**LeetCode Problem #2813 — Maximum Elegance of a K-Length Subsequence**
Solve LeetCode Maximum Elegance of a K-Length Subsequence using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Elegance of a K-Length Subsequence |
| LeetCode | #2813 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  2D integer array  items  of length  n  and an integer  k .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Elegance of a K-Length Subsequence**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [2030. Smallest K-Length Subsequence With Occurrences of a Letter](../2157-smallest-k-length-subsequence-with-occurrences-of-a-letter/)
- [2099. Find Subsequence of Length K With the Largest Sum](../2204-find-subsequence-of-length-k-with-the-largest-sum/)
- [2461. Maximum Sum of Distinct Subarrays With Length K](../2552-maximum-sum-of-distinct-subarrays-with-length-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/)
