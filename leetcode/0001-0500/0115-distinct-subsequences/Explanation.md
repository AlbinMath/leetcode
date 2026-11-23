# LeetCode 115: Distinct Subsequences

**LeetCode Problem #115 — Distinct Subsequences**
Solve LeetCode Distinct Subsequences using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Subsequences |
| LeetCode | #115 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

## Constraints
- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

## Examples
### Example 1
- **Input:** `s = "rabbbit", t = "rabbit"`
- **Output:** `3`
- **Explanation:** As shown below, there are 3 ways you can generate "rabbit" from s.

### Example 2
- **Input:** `s = "babgbag", t = "bag"`
- **Output:** `5`
- **Explanation:** As shown below, there are 5 ways you can generate "bag" from s.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **1D Dynamic Programming** with space optimization.

1. **DP Definition:** `dp[j]` represents the number of distinct subsequences of `s[0..i-1]` that equal `t[0..j-1]`.
2. **Base Case:** `dp[0] = 1` because the empty string `""` is always a subsequence of any string (by deleting all characters).
3. **Iteration:** For each character `s[i-1]` (outer loop over `s`):
   - It iterates **backwards** over `j` (from `n` down to `1`) to avoid overwriting values that are still needed.
   - If `s[i-1] === t[j-1]`, then `dp[j] += dp[j-1]`. This means: the number of ways to form `t[0..j-1]` includes both (a) the ways without using `s[i-1]` (existing `dp[j]`) and (b) the ways that use `s[i-1]` to match `t[j-1]` (which is `dp[j-1]`).
4. The answer is `dp[n]` — the number of ways to form the entire string `t`.

Time complexity is $O(M \times N)$ where $M$ and $N$ are the lengths of `s` and `t`. Space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "rabbbit", t = "rabbit"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** As shown below, there are 3 ways you can generate "rabbit" from s.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {
    const m = s.length;
    const n = t.length;

    // dp[j] = number of ways to form t[0...j-1]
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;

    for (let i = 1; i <= m; i++) {
        // Go backwards so we don't overwrite values
        for (let j = n; j >= 1; j--) {
            if (s[i - 1] === t[j - 1]) {
                dp[j] += dp[j - 1];
            }
        }
    }

    return dp[n];
};
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
- [940. Distinct Subsequences II](../../0501-1000/0977-distinct-subsequences-ii/)
- [1081. Smallest Subsequence of Distinct Characters](../../1001-1500/1159-smallest-subsequence-of-distinct-characters/)
- [1316. Distinct Echo Substrings](../../1001-1500/1244-distinct-echo-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distinct-subsequences/)
