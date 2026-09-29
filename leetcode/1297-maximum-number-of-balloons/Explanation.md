# Maximum Number Of Balloons

## Problem Explanation
Given a string `text`, return the maximum number of times the word `"balloon"` can be formed using the characters in `text`. Each character can only be used once.

## How the Code Works
1. **Count Characters:** Count the frequency of every character in the text.
2. **Check Required Characters:** The word "balloon" needs: `b`×1, `a`×1, `l`×2, `o`×2, `n`×1.
3. **Bottleneck:** The answer is the minimum of: count of `b`, count of `a`, count of `l` divided by 2, count of `o` divided by 2, and count of `n`. The character with the smallest available count determines how many complete "balloon"s can be formed.

Time complexity is $O(N)$ and space complexity is $O(1)$.
