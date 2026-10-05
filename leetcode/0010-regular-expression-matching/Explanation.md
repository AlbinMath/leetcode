# LeetCode 10: Regular Expression Matching

**LeetCode Problem #10 — Regular Expression Matching**
Solve LeetCode Regular Expression Matching using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Regular Expression Matching |
| LeetCode | #10 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an input string  s  and a pattern  p , implement regular expression matching with support for  &#39;.&#39;  and  &#39;*&#39;  where:

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
This solution uses **Top-Down Dynamic Programming (Memoization)** to check all possible valid matches efficiently.

1. **State:** The recursive function `dp(i, j)` determines if the substring `s[i:]` matches the pattern `p[j:]`.
2. **Memoization:** It uses a `Map` (`memo`) to store the results of `(i, j)` to avoid redundant calculations.
3. **Base Case:** If the pattern is fully consumed (`j === p.length`), the string must also be fully consumed (`i === s.length`) for a valid match.
4. **First Match:** It checks if the current characters match: `s[i] === p[j]` or if `p[j] === '.'` (which matches any character).
5. **Handling '*':**
   - If the *next* character in the pattern is `'*'`, there are two choices:
     1. **Ignore the '*' and the preceding element:** Advance the pattern by 2 characters (`dp(i, j + 2)`). This simulates the `'*'` matching *zero* occurrences.
     2. **Consume a character from `s`:** If `firstMatch` is true, we can consume one character from `s` and keep the pattern at `j` (`dp(i + 1, j)`). This simulates the `'*'` matching *one or more* occurrences.
6. **Handling Normal Characters:** If there's no `'*'`, it simply requires `firstMatch` to be true and recursively calls `dp(i + 1, j + 1)`.

By memoizing the states, the time complexity is reduced to $O(S \times P)$ where $S$ and $P$ are the lengths of the string and pattern respectively.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Regular Expression Matching**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [115. Distinct Subsequences](../0115-distinct-subsequences/)
- [486. Predict the Winner](../0486-predict-the-winner/)
- [940. Distinct Subsequences II](../0977-distinct-subsequences-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/regular-expression-matching/)
