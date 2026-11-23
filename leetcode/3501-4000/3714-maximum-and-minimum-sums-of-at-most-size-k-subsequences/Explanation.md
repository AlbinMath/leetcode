# LeetCode 3428: Maximum and Minimum Sums of at Most Size K Subsequences

**LeetCode Problem #3428 — Maximum and Minimum Sums of at Most Size K Subsequences**
Solve LeetCode Maximum and Minimum Sums of at Most Size K Subsequences using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum and Minimum Sums of at Most Size K Subsequences |
| LeetCode | #3428 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums  and a positive integer  k . Return the sum of the  maximum  and  minimum  elements of all   subsequences   of  nums  with  at most   k  elements.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum and Minimum Sums of at Most Size K Subsequences**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [3430. Maximum and Minimum Sums of at Most Size K Subarrays](../../3501-4000/3725-maximum-and-minimum-sums-of-at-most-size-k-subarrays/)
- [3627. Maximum Median Sum of Subsequences of Size 3](../../3501-4000/3766-maximum-median-sum-of-subsequences-of-size-3/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/)
