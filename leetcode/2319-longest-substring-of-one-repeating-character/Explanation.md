# Longest Substring Of One Repeating Character

## Problem Explanation
Given a string and queries that each change one character, after each query return the length of the longest substring of one repeating character.

## How the Code Works
The code uses a **Segment Tree** where each node stores: the longest repeating prefix, suffix, and overall substring, plus the characters at the boundaries. Merging two segments checks if the suffix of the left and prefix of the right share the same character.

Time complexity is $O((N + Q) \log N)$ and space complexity is $O(N)$.
