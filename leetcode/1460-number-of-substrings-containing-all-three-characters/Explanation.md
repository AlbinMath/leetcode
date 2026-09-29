# Number Of Substrings Containing All Three Characters

## Problem Explanation
Given a string `s` consisting only of characters `a`, `b`, and `c`, return the number of substrings that contain at least one occurrence of all three characters.

## How the Code Works
The code uses a clever **counting approach** based on tracking the last occurrence of each character.

1. **Last Array:** `last[0]`, `last[1]`, `last[2]` store the most recent index where `a`, `b`, `c` appeared, initialized to `-1`.
2. For each index `right`, update `last[s[right] - 'a'] = right`.
3. If all three characters have appeared (`last[0] != -1 && last[1] != -1 && last[2] != -1`):
   - Find `minLast` = the earliest of the three last positions. Any substring starting from index `0` through `minLast` (inclusive) and ending at `right` will contain all three characters.
   - Add `minLast + 1` to the answer.

Time complexity is $O(N)$ and space complexity is $O(1)$.
