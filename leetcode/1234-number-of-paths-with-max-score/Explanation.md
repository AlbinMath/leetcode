# LeetCode 1301: Number of Paths with Max Score

**LeetCode Problem #1301 — Number of Paths with Max Score**
Solve LeetCode Number of Paths with Max Score using PHP and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Paths with Max Score |
| LeetCode | #1301 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a square  board  of characters. You can move on the board starting at the bottom right square marked with the character  &#39;S&#39; .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **2D Dynamic Programming** processing from `S` toward `E`.

1. **Two DP Tables:** `score[i][j]` stores the maximum score reachable from `(i,j)` to `S`. `ways[i][j]` stores the number of paths achieving that score. `-1` means unreachable.
2. **Base Case:** `score[n-1][n-1] = 0`, `ways[n-1][n-1] = 1` (at `S`).
3. **Transition:** For each cell `(i,j)` processed right-to-left, bottom-to-top:
   - Skip obstacles (`X`).
   - Check three neighbors: down `(i+1,j)`, right `(i,j+1)`, diagonal `(i+1,j+1)`.
   - Take the neighbor with the highest score. If multiple neighbors tie, sum their path counts.
   - Add the current cell's digit value to the best score.
4. **Result:** `[score[0][0], ways[0][0]]`, or `[0, 0]` if unreachable.

Time complexity is $O(N^2)$ and space complexity is $O(N^2)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Paths with Max Score**. Applying **Memoization & State Transition** yields the target result step by step.

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
PHP

## Source Code
- [solution.php](./solution.php)

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
- [9. Palindrome Number](../0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../0017-letter-combinations-of-a-phone-number/)
- [485. Max Consecutive Ones](../0485-max-consecutive-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-paths-with-max-score/)
