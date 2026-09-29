# Regular Expression Matching

## Problem Explanation
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'`.
- `'.'` Matches any single character.
- `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

For example:
- `s = "aa"`, `p = "a"` returns `false` (does not match the whole string).
- `s = "aa"`, `p = "a*"` returns `true` (`*` repeats `'a'` once to match `"aa"`).
- `s = "ab"`, `p = ".*"` returns `true` (`.*` means "zero or more of any character").

## How the Code Works
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
