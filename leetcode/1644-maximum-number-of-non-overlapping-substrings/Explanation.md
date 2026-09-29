# Maximum Number Of Non Overlapping Substrings

## Problem Explanation
Given a string, find the maximum number of non-overlapping substrings such that each substring contains all occurrences of every character within it. If multiple solutions have the same count, return the one with minimum total length.

## How the Code Works
The code uses a **Greedy** approach. It first finds the leftmost and rightmost occurrence of each character. Then for each potential starting character, it expands the substring to include all occurrences of all characters within it. Finally, it greedily selects non-overlapping substrings by preferring shorter ones that end earliest.

Time complexity is $O(N \times |\Sigma|)$ and space complexity is $O(|\Sigma|)$ where $|\Sigma|$ is the alphabet size.
