# LeetCode 2555: Maximize Win From Two Segments

**LeetCode Problem #2555 — Maximize Win From Two Segments**
Solve LeetCode Maximize Win From Two Segments using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Win From Two Segments |
| LeetCode | #2555 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are some prizes on the  X-axis . You are given an integer array  prizePositions  that is  sorted in non-decreasing order , where  prizePositions[i]  is the position of the  i th   prize. There could be different prizes at the same position on the line. You are also given an integer  k .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximize Win From Two Segments**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [884. Uncommon Words from Two Sentences](../../0501-1000/0920-uncommon-words-from-two-sentences/)
- [1771. Maximize Palindrome Length From Subsequences](../../1501-2000/1897-maximize-palindrome-length-from-subsequences/)
- [2259. Remove Digit From Number to Maximize Result](../../2001-2500/2337-remove-digit-from-number-to-maximize-result/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-win-from-two-segments/)
