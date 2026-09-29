# Smallest Subsequence Of Distinct Characters

## Problem Explanation
Given a string `s`, return the lexicographically smallest subsequence of `s` that contains all the distinct characters of `s` exactly once. (This is equivalent to "Remove Duplicate Letters.")

## How the Code Works
The code uses a **Monotonic Stack** (greedy) approach.

1. **Last Occurrence:** It records the last index of each character in the string.
2. **Used Array:** Tracks which characters are currently in the result to avoid duplicates.
3. **Build the Result String:** For each character `c` at index `i`:
   - If `c` is already in the result (`used[c]` is true), skip it.
   - While the last character in the result (`st.back()`) is greater than `c` AND that character appears again later (`last[st.back()] > i`): remove it from the result and mark it as unused. This ensures we keep the smallest characters first when possible.
   - Add `c` to the result and mark it as used.
4. The result is the lexicographically smallest subsequence containing all distinct characters.

Time complexity is $O(N)$ and space complexity is $O(1)$ (at most 26 characters in the stack).
