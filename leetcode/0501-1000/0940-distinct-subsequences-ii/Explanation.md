# LeetCode 940: Distinct Subsequences II

**LeetCode Problem #940 — Distinct Subsequences II**
Solve LeetCode Distinct Subsequences II using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Subsequences II |
| LeetCode | #940 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string s, return *the number of **distinct non-empty subsequences** of* `s`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `" a b c d e "` while `"aec"` is not.

## Constraints
- `1 <= s.length <= 2000`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abc"`
- **Output:** `7`
- **Explanation:** The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

### Example 2
- **Input:** `s = "aba"`
- **Output:** `6`
- **Explanation:** The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

### Example 3
- **Input:** `s = "aaa"`
- **Output:** `3`
- **Explanation:** The 3 distinct subsequences are "a", "aa" and "aaa".

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
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

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
 * @return {number}
 */
var distinctSubseqII = function(s) {
    const MOD = 1000000007;
    let dp = 1;
    const last = new Array(26).fill(0);

    for (let i = 0; i < s.length; i++) {
        const c = s.charCodeAt(i) - 97;
        let newDp = (2 * dp) % MOD;
        newDp = (newDp - last[c] + MOD) % MOD;
        last[c] = dp;
        dp = newDp;
    }
    return (dp - 1 + MOD) % MOD;
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
- [115. Distinct Subsequences](../../0001-0500/0115-distinct-subsequences/)
- [491. Non-decreasing Subsequences](../../0001-0500/0491-non-decreasing-subsequences/)
- [659. Split Array into Consecutive Subsequences](../../0501-1000/0659-split-array-into-consecutive-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distinct-subsequences-ii/)
