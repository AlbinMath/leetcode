# LeetCode 2842: Count K-Subsequences of a String With Maximum Beauty

**LeetCode Problem #2842 — Count K-Subsequences of a String With Maximum Beauty**
Solve LeetCode Count K-Subsequences of a String With Maximum Beauty using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count K-Subsequences of a String With Maximum Beauty |
| LeetCode | #2842 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` and an integer `k`.

A **k-subsequence** is a **subsequence** of `s`, having length `k`, and all its characters are **unique**, **i.e**., every character occurs once.

Let `f(c)` denote the number of times the character `c` occurs in `s`.

The **beauty** of a **k-subsequence** is the **sum** of `f(c)` for every character `c` in the k-subsequence.

For example, consider `s = "abbbdd"` and `k = 2`:

`f('a') = 1`, `f('b') = 3`, `f('d') = 2` 
 Some k-subsequences of `s` are:
 
 `" **ab** bbdd"` -> `"ab"` having a beauty of `f('a') + f('b') = 4` 
 `" **a** bbb** d **d"` -> `"ad"` having a beauty of `f('a') + f('d') = 3` 
 `"a** b **bb **d** d"` -> `"bd"` having a beauty of `f('b') + f('d') = 5`

Return *an integer denoting the number of k-subsequences **whose **beauty** is the **maximum** among all **k-subsequences***. Since the answer may be too large, return it modulo `10^9 + 7`.

A subsequence of a string is a new string formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

**Notes**

`f(c)` is the number of times a character `c` occurs in `s`, not a k-subsequence. 
 Two k-subsequences are considered different if one is formed by an index that is not present in the other. So, two k-subsequences may form the same string.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `1 <= k <= s.length`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "bcca", k = 2`
- **Output:** `4`
- **Explanation:** From s we have f('a') = 1, f('b') = 1, and f('c') = 2. 
The k-subsequences of s are:

### Example 2
- **Input:** `s = "abbcd", k = 4`
- **Output:** `2`
- **Explanation:** From s we have f('a') = 1, f('b') = 2, f('c') = 1, and f('d') = 1. 
The k-subsequences of s are:

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Count K-Subsequences of a String With Maximum Beauty**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "bcca", k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** From s we have f('a') = 1, f('b') = 1, and f('c') = 2. 
The k-subsequences of s are:

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
var countKSubsequencesWithMaxBeauty = function(s, k) {
    const MOD = 1000000007n;
    const freq = new Array(26).fill(0);

    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    const counts = freq.filter(x => x > 0).sort((a, b) => b - a);

    if (counts.length < k) return 0;

    const threshold = counts[k - 1];
    let greater = 0;
    let equal = 0;

    for (const f of counts) {
        if (f > threshold) greater++;
        if (f === threshold) equal++;
    }

    let answer = 1n;

    for (let i = 0; i < greater; i++) {
        answer = answer * BigInt(counts[i]) % MOD;
    }

    const choose = k - greater;

    let combination = 1n;
    for (let i = 1; i <= choose; i++) {
        combination = combination * BigInt(equal - i + 1) % MOD;
        combination = combination * modPow(BigInt(i), MOD - 2n, MOD) % MOD;
    }

    answer = answer * combination % MOD;

    for (let i = 0; i < choose; i++) {
        answer = answer * BigInt(threshold) % MOD;
    }

    return Number(answer);
};

function modPow(base, exp, mod) {
    let result = 1n;
    while (exp > 0n) {
        if (exp % 2n === 1n) result = result * base % mod;
        base = base * base % mod;
        exp /= 2n;
    }
    return result;
}
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
- [3428. Maximum and Minimum Sums of at Most Size K Subsequences](../../3001-3500/3428-maximum-and-minimum-sums-of-at-most-size-k-subsequences/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1239. Maximum Length of a Concatenated String with Unique Characters](../../1001-1500/1239-maximum-length-of-a-concatenated-string-with-unique-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/)
