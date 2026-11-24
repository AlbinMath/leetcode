# LeetCode 97: Interleaving String

**LeetCode Problem #97 — Interleaving String**
Solve LeetCode Interleaving String using JavaScript, Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Interleaving String |
| LeetCode | #97 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An **interleaving** of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

`s = s_1 + s_2 + ... + s_n` 
 `t = t_1 + t_2 + ... + t_m` 
 `|n - m| <= 1` 
 The **interleaving** is `s_1 + t_1 + s_2 + t_2 + s_3 + t_3 + ...` or `t_1 + s_1 + t_2 + s_2 + t_3 + s_3 + ...`

**Note:** `a + b` is the concatenation of strings `a` and `b`.

## Constraints
- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2`, and `s3` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"`
- **Output:** `true`
- **Explanation:** One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

### Example 2
- **Input:** `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"`
- **Output:** `false`
- **Explanation:** Notice how it is impossible to interleave s2 with any other string to obtain s3.

### Example 3
- **Input:** `s1 = "", s2 = "", s3 = ""`
- **Output:** `true`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Interleaving String**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var isInterleave = function(s1, s2, s3) {
    const m = s1.length;
    const n = s2.length;

    if (m + n !== s3.length) {
        return false;
    }

    const dp = new Array(n + 1).fill(false);
    dp[0] = true;

    // Initialize using s2 only
    for (let j = 1; j <= n; j++) {
        dp[j] = dp[j - 1] && s2[j - 1] === s3[j - 1];
    }

    // Process characters from s1
    for (let i = 1; i <= m; i++) {
        dp[0] = dp[0] && s1[i - 1] === s3[i - 1];

        for (let j = 1; j <= n; j++) {
            const ch = s3[i + j - 1];

            // Take the character from s1 or s2
            dp[j] =
                (dp[j] && s1[i - 1] === ch) ||
                (dp[j - 1] && s2[j - 1] === ch);
        }
    }

    return dp[n];
};
```

### Python
```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2) + 1)
        dp[0] = True
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, len(s2) + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or \
                         (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1]
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
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [87. Scramble String](../../0001-0500/0087-scramble-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/interleaving-string/)
