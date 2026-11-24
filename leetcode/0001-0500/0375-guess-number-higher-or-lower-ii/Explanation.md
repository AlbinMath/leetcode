# LeetCode 375: Guess Number Higher or Lower II

**LeetCode Problem #375 — Guess Number Higher or Lower II**
Solve LeetCode Guess Number Higher or Lower II using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Guess Number Higher or Lower II |
| LeetCode | #375 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
We are playing the Guessing Game. The game will work as follows:

I pick a number between `1` and `n`. 
 You guess a number. 
 If you guess the right number, **you win the game**. 
 If you guess the wrong number, then I will tell you whether the number I picked is **higher or lower**, and you will continue guessing. 
 Every time you guess a wrong number `x`, you will pay `x` dollars. If you run out of money, **you lose the game**.

Given a particular `n`, return *the minimum amount of money you need to **guarantee a win regardless of what number I pick***.

## Constraints
- `1 <= n <= 200`

## Examples
### Example 1
- **Input:** `n = 10`
- **Output:** `16`
- **Explanation:** The winning strategy is as follows:
- The range is [1,10]. Guess 7.
 - If this is my number, your total is $0. Otherwise, you pay $7.
 - If my number is higher, the range is [8,10]. Guess 9.
 - If this is my number, your total is $7. Otherwise, you pay $9.
 - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
 - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
 - If my number is lower, the range is [1,6]. Guess 3.
 - If this is my number, your total is $7. Otherwise, you pay $3.
 - If my number is higher, the range is [4,6]. Guess 5.
 - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
 - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
 - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
 - If my number is lower, the range is [1,2]. Guess 1.
 - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
 - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.

### Example 2
- **Input:** `n = 1`
- **Output:** `0`
- **Explanation:** There is only one possible number, so you can guess 1 and not have to pay anything.

### Example 3
- **Input:** `n = 2`
- **Output:** `1`
- **Explanation:** There are two possible numbers, 1 and 2.
- Guess 1.
 - If this is my number, your total is $0. Otherwise, you pay $1.
 - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Guess Number Higher or Lower II**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** The winning strategy is as follows:
- The range is [1,10]. Guess 7.
 - If this is my number, your total is $0. Otherwise, you pay $7.
 - If my number is higher, the range is [8,10]. Guess 9.
 - If this is my number, your total is $7. Otherwise, you pay $9.
 - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
 - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
 - If my number is lower, the range is [1,6]. Guess 3.
 - If this is my number, your total is $7. Otherwise, you pay $3.
 - If my number is higher, the range is [4,6]. Guess 5.
 - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
 - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
 - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
 - If my number is lower, the range is [1,2]. Guess 1.
 - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
 - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

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


```python
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for l in range(1, n - length + 2):
                r = l + length - 1
                dp[l][r] = min(x + max(dp[l][x - 1], dp[x + 1][r])
                               for x in range(l, r))
        return dp[1][n]
```

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
- [374. Guess Number Higher or Lower](../../0001-0500/0374-guess-number-higher-or-lower/)
- [843. Guess the Word](../../0501-1000/0843-guess-the-word/)
- [709. To Lower Case](../../0501-1000/0709-to-lower-case/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower-ii/)
