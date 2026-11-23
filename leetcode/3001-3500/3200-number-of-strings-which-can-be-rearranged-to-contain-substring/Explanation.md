# LeetCode 2930: Number of Strings Which Can Be Rearranged to Contain Substring

**LeetCode Problem #2930 — Number of Strings Which Can Be Rearranged to Contain Substring**
Solve LeetCode Number of Strings Which Can Be Rearranged to Contain Substring using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Strings Which Can Be Rearranged to Contain Substring |
| LeetCode | #2930 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`.

A string `s` is called **good **if it contains only lowercase English characters **and** it is possible to rearrange the characters of `s` such that the new string contains `"leet"` as a **substring**.

For example:

The string `"lteer"` is good because we can rearrange it to form `"leetr"` . 
 `"letl"` is not good because we cannot rearrange it to contain `"leet"` as a substring.

Return *the **total** number of good strings of length *`n`.

Since the answer may be large, return it **modulo **`10^9 + 7`.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= n <= 10^5`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `12`
- **Explanation:** The 12 strings which can be rearranged to have "leet" as a substring are: "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".

### Example 2
- **Input:** `n = 10`
- **Output:** `83943898`
- **Explanation:** The number of strings with length 10 which can be rearranged to have "leet" as a substring is 526083947580. Hence the answer is 526083947580 % (10^9 + 7) = 83943898.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Strings Which Can Be Rearranged to Contain Substring**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** The 12 strings which can be rearranged to have "leet" as a substring are: "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".

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
var stringCount = function(n) {
    const MOD = 1000000007;

    let dp = Array.from({ length: 2 }, () =>
        Array.from({ length: 3 }, () => Array(2).fill(0))
    );
    dp[0][0][0] = 1;

    for (let i = 0; i < n; i++) {
        const next = Array.from({ length: 2 }, () =>
            Array.from({ length: 3 }, () => Array(2).fill(0))
        );

        for (let l = 0; l < 2; l++) {
            for (let e = 0; e < 3; e++) {
                for (let t = 0; t < 2; t++) {
                    const ways = dp[l][e][t];
                    if (ways === 0) continue;

                    // Choose one of the 23 other letters
                    next[l][e][t] =
                        (next[l][e][t] + ways * 23) % MOD;

                    // Choose 'l'
                    next[1][e][t] =
                        (next[1][e][t] + ways) % MOD;

                    // Choose 'e'
                    next[l][Math.min(2, e + 1)][t] =
                        (next[l][Math.min(2, e + 1)][t] + ways) % MOD;

                    // Choose 't'
                    next[l][e][1] =
                        (next[l][e][1] + ways) % MOD;
                }
            }
        }

        dp = next;
    }

    return dp[1][2][1];
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
- [3297. Count Substrings That Can Be Rearranged to Contain a String I](../../3501-4000/3573-count-substrings-that-can-be-rearranged-to-contain-a-string-i/)
- [3298. Count Substrings That Can Be Rearranged to Contain a String II](../../3501-4000/3572-count-substrings-that-can-be-rearranged-to-contain-a-string-ii/)
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1469-minimum-number-of-steps-to-make-two-strings-anagram/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/)
