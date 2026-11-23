# LeetCode 2400: Number of Ways to Reach a Position After Exactly k Steps

**LeetCode Problem #2400 — Number of Ways to Reach a Position After Exactly k Steps**
Solve LeetCode Number of Ways to Reach a Position After Exactly k Steps using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Reach a Position After Exactly k Steps |
| LeetCode | #2400 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given two  positive  integers  startPos  and  endPos . Initially, you are standing at position  startPos  on an  infinite  number line. With one step, you can move either one position to the left, or one position to the right.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Ways to Reach a Position After Exactly k Steps**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [3154. Find Number of Ways to Reach the K-th Stair](../../3001-3500/3414-find-number-of-ways-to-reach-the-k-th-stair/)
- [1866. Number of Ways to Rearrange Sticks With K Sticks Visible](../../1501-2000/1996-number-of-ways-to-rearrange-sticks-with-k-sticks-visible/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2229-maximum-fruits-harvested-after-at-most-k-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/)
