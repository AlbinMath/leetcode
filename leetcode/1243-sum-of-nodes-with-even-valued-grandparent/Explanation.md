# LeetCode 1315: Sum of Nodes with Even-Valued Grandparent

**LeetCode Problem #1315 — Sum of Nodes with Even-Valued Grandparent**
Solve LeetCode Sum of Nodes with Even-Valued Grandparent using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Nodes with Even-Valued Grandparent |
| LeetCode | #1315 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given the  root  of a binary tree, return  the sum of values of nodes with an  even-valued grandparent  . If there are no nodes with an  even-valued grandparent , return  0 .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sum of Nodes with Even-Valued Grandparent**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [985. Sum of Even Numbers After Queries](../1027-sum-of-even-numbers-after-queries/)
- [2074. Reverse Nodes in Even Length Groups](../2196-reverse-nodes-in-even-length-groups/)
- [2180. Count Integers With Even Digit Sum](../2298-count-integers-with-even-digit-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/)
