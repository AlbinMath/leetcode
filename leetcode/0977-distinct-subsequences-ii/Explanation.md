# LeetCode 977: Squares of a Sorted Array

**LeetCode Problem #977 — Squares of a Sorted Array**
Solve LeetCode Squares of a Sorted Array using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization / Bottom-Up State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Squares of a Sorted Array |
| LeetCode | #977 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Memoization / Bottom-Up State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string s, return  the number of  distinct non-empty subsequences  of   s . Since the answer may be very large, return it  modulo   10 9  + 7 .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **Dynamic Programming** with a clever formula to count distinct subsequences while avoiding duplicates.

1. **DP Variable:** `dp` represents the total number of distinct subsequences (including the empty subsequence) that can be formed from the characters processed so far. It starts at `1` (the empty subsequence).
2. **Last Array:** `last[c]` stores the value of `dp` at the time character `c` was last seen.
3. **For Each Character `s[i]`:**
   - `newDp = 2 * dp`: Every existing subsequence can either include or exclude the new character, doubling the count.
   - `newDp -= last[c]`: Subtract the subsequences that were counted when this same character was last seen, to remove duplicates.
   - Update `last[c] = dp` (the value of `dp` *before* processing this character).
   - Set `dp = newDp`.
4. **Result:** `dp - 1` subtracts the empty subsequence.

Time complexity is $O(N)$ and space complexity is $O(1)$ (the `last` array has fixed size 26).

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization / Bottom-Up State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Squares of a Sorted Array**. Applying **Memoization / Bottom-Up State Transition** yields the target result step by step.

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
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [602. Friend Requests II: Who Has the Most Friends](../0602-friend-requests-ii-who-has-the-most-friends/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distinct-subsequences-ii/)
