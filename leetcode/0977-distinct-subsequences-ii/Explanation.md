# Distinct Subsequences II

## Problem Explanation
Given a string `s`, return the number of distinct non-empty subsequences of `s`, modulo `10^9 + 7`.

## How the Code Works
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
