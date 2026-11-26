# LeetCode 1143: Longest Common Subsequence

**LeetCode Problem #1143 — Longest Common Subsequence**
Solve LeetCode Longest Common Subsequence using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Common Subsequence |
| LeetCode | #1143 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two strings `text1` and `text2`, return *the length of their longest **common subsequence**. *If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

## Constraints
- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

## Examples
### Example 1
- **Input:** `text1 = "abcde", text2 = "ace"`
- **Output:** `3`
- **Explanation:** The longest common subsequence is "ace" and its length is 3.

### Example 2
- **Input:** `text1 = "abc", text2 = "abc"`
- **Output:** `3`
- **Explanation:** The longest common subsequence is "abc" and its length is 3.

### Example 3
- **Input:** `text1 = "abc", text2 = "def"`
- **Output:** `0`
- **Explanation:** There is no such common subsequence, so the result is 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Longest Common Subsequence**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text1 = "abcde", text2 = "ace"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The longest common subsequence is "ace" and its length is 3.

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
var longestCommonSubsequence = function(text1, text2) {
    const m = text1.length;
    const n = text2.length;

    const dp = Array.from(
        { length: m + 1 },
        () => Array(n + 1).fill(0)
    );

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i - 1] === text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                );
            }
        }
    }

    return dp[m][n];
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
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)
- [1923. Longest Common Subpath](../../1501-2000/1923-longest-common-subpath/)
- [3043. Find the Length of the Longest Common Prefix](../../3001-3500/3043-find-the-length-of-the-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-common-subsequence/)
