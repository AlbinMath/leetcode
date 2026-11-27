# LeetCode 730: Count Different Palindromic Subsequences

**LeetCode Problem #730 — Count Different Palindromic Subsequences**
Solve LeetCode Count Different Palindromic Subsequences using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Different Palindromic Subsequences |
| LeetCode | #730 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string s, return *the number of different non-empty palindromic subsequences in* `s`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences `a_1, a_2, ...` and `b_1, b_2, ...` are different if there is some `i` for which `a_i != b_i`.

## Constraints
- `1 <= s.length <= 1000`
- `s[i]` is either `'a'`, `'b'`, `'c'`, or `'d'`.

## Examples
### Example 1
- **Input:** `s = "bccb"`
- **Output:** `6`
- **Explanation:** The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

### Example 2
- **Input:** `s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"`
- **Output:** `104860361`
- **Explanation:** There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Count Different Palindromic Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "bccb"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

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
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # nxt[i][c]: first index >= i with letter c (n if none)
        # prv[i][c]: last index <= i with letter c (-1 if none)
        nxt = [[n] * 4 for _ in range(n + 2)]
        prv = [[-1] * 4 for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            nxt[i] = nxt[i + 1][:]
            nxt[i][ord(s[i]) - 97] = i
        for i in range(n):
            prv[i] = prv[i - 1][:] if i > 0 else [-1] * 4
            prv[i][ord(s[i]) - 97] = i

        # dp[i][j] with empty ranges (i > j) equal to 0
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        def get(i, j):
            return dp[i][j] if i <= j else 0

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    dp[i][j] = (get(i + 1, j) + get(i, j - 1) - get(i + 1, j - 1)) % MOD
                else:
                    c = ord(s[i]) - 97
                    lo = nxt[i + 1][c]
                    hi = prv[j - 1][c]
                    inner = get(i + 1, j - 1)
                    if lo > j - 1 or lo > hi:        # no c strictly inside
                        dp[i][j] = (2 * inner + 2) % MOD
                    elif lo == hi:                   # exactly one c inside
                        dp[i][j] = (2 * inner + 1) % MOD
                    else:                            # two or more c inside
                        dp[i][j] = (2 * inner - get(lo + 1, hi - 1)) % MOD

        return dp[0][n - 1] % MOD
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
- [1819. Number of Different Subsequences GCDs](../../1501-2000/1819-number-of-different-subsequences-gcds/)
- [1332. Remove Palindromic Subsequences](../../1001-1500/1332-remove-palindromic-subsequences/)
- [1930. Unique Length-3 Palindromic Subsequences](../../1501-2000/1930-unique-length-3-palindromic-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-different-palindromic-subsequences/)
