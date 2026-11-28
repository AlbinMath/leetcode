# LeetCode 91: Decode Ways

**LeetCode Problem #91 — Decode Ways**
Solve LeetCode Decode Ways using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Decode Ways |
| LeetCode | #91 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have intercepted a secret message encoded as a string of numbers. The message is **decoded** via the following mapping:

"1" -> 'A' 
"2" -> 'B' 
... 
"25" -> 'Y' 
"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

`"AAJF"` with the grouping `(1, 1, 10, 6)` 
 `"KJF"` with the grouping `(11, 10, 6)` 
 The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode. 
 
Given a string s containing only digits, return the **number of ways** to **decode** it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a **32-bit** integer.

## Constraints
- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zero(s).

## Examples
### Example 1
- **Input:** `s = "12"`
- **Output:** `2`
- **Explanation:** "12" could be decoded as "AB" (1 2) or "L" (12).

### Example 2
- **Input:** `s = "226"`
- **Output:** `3`
- **Explanation:** "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

### Example 3
- **Input:** `s = "06"`
- **Output:** `0`
- **Explanation:** "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Decode Ways**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "12"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** "12" could be decoded as "AB" (1 2) or "L" (12).

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
var numDecodings = function(s) {
    const n = s.length;
    const dp = new Array(n + 1).fill(0);

    dp[0] = 1;

    for (let i = 1; i <= n; i++) {
        // Decode one digit
        if (s[i - 1] !== '0') {
            dp[i] += dp[i - 1];
        }

        // Decode two digits
        if (i >= 2) {
            const twoDigits = Number(s.substring(i - 2, i));

            if (twoDigits >= 10 && twoDigits <= 26) {
                dp[i] += dp[i - 2];
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
- [639. Decode Ways II](../../0501-1000/0639-decode-ways-ii/)
- [241. Different Ways to Add Parentheses](../../0001-0500/0241-different-ways-to-add-parentheses/)
- [1269. Number of Ways to Stay in the Same Place After Some Steps](../../1001-1500/1269-number-of-ways-to-stay-in-the-same-place-after-some-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/decode-ways/)
