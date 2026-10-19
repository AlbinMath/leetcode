# LeetCode 478: Generate Random Point in a Circle

**LeetCode Problem #478 — Generate Random Point in a Circle**
Solve LeetCode Generate Random Point in a Circle using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate Random Point in a Circle |
| LeetCode | #478 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given the radius and the position of the center of a circle, implement the function  randPoint  which generates a uniform random point inside the circle.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Generate Random Point in a Circle**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [22. Generate Parentheses](../0022-generate-parentheses/)
- [138. Copy List with Random Pointer](../0138-copy-list-with-random-pointer/)
- [528. Random Pick with Weight](../0912-random-pick-with-weight/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-random-point-in-a-circle/)
