# LeetCode 10: Regular Expression Matching

**LeetCode Problem #10 — Regular Expression Matching**
Solve LeetCode Regular Expression Matching using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Regular Expression Matching |
| LeetCode | #10 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

`'.'` Matches any single character.​​​​ 
 `'*'` Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

## Constraints
- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'.'`, and `'*'`.
- It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

## Examples
### Example 1
- **Input:** `s = "aa", p = "a"`
- **Output:** `false`
- **Explanation:** "a" does not match the entire string "aa".

### Example 2
- **Input:** `s = "aa", p = "a*"`
- **Output:** `true`
- **Explanation:** '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

### Example 3
- **Input:** `s = "ab", p = ".*"`
- **Output:** `true`
- **Explanation:** ".*" means "zero or more (*) of any character (.)".

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
This solution uses **Top-Down Dynamic Programming (Memoization)** to check all possible valid matches efficiently.

1. **State:** The recursive function `dp(i, j)` determines if the substring `s[i:]` matches the pattern `p[j:]`.
2. **Memoization:** It uses a `Map` (`memo`) to store the results of `(i, j)` to avoid redundant calculations.
3. **Base Case:** If the pattern is fully consumed (`j === p.length`), the string must also be fully consumed (`i === s.length`) for a valid match.
4. **First Match:** It checks if the current characters match: `s[i] === p[j]` or if `p[j] === '.'` (which matches any character).
5. **Handling '*':**
   - If the *next* character in the pattern is `'*'`, there are two choices:
     1. **Ignore the '*' and the preceding element:** Advance the pattern by 2 characters (`dp(i, j + 2)`). This simulates the `'*'` matching *zero* occurrences.
     2. **Consume a character from `s`:** If `firstMatch` is true, we can consume one character from `s` and keep the pattern at `j` (`dp(i + 1, j)`). This simulates the `'*'` matching *one or more* occurrences.
6. **Handling Normal Characters:** If there's no `'*'`, it simply requires `firstMatch` to be true and recursively calls `dp(i + 1, j + 1)`.

By memoizing the states, the time complexity is reduced to $O(S \times P)$ where $S$ and $P$ are the lengths of the string and pattern respectively.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aa", p = "a"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** "a" does not match the entire string "aa".

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
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    const memo = new Map();

    function dp(i, j) {
        // Pattern completely processed
        if (j === p.length) {
            return i === s.length;
        }

        const key = i + "," + j;
        if (memo.has(key)) {
            return memo.get(key);
        }

        // Check if current characters match
        const firstMatch =
            i < s.length &&
            (s[i] === p[j] || p[j] === ".");

        let result;

        // If next character is '*'
        if (j + 1 < p.length && p[j + 1] === "*") {
            // Option 1: use '*' as zero occurrences
            // Option 2: consume one matching character
            result =
                dp(i, j + 2) ||
                (firstMatch && dp(i + 1, j));
        } else {
            // Normal character or '.'
            result = firstMatch && dp(i + 1, j + 1);
        }

        memo.set(key, result);
        return result;
    }

    return dp(0, 0);
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
- [282. Expression Add Operators](../../0001-0500/0282-expression-add-operators/)
- [736. Parse Lisp Expression](../../0501-1000/0736-parse-lisp-expression/)
- [1106. Parsing A Boolean Expression](../../1001-1500/1197-parsing-a-boolean-expression/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/regular-expression-matching/)
