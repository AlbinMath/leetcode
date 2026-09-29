# Number Of Strings That Appear As Substrings In Word

## Problem Explanation
Given an array of strings `patterns` and a string `word`, return how many strings in `patterns` are substrings of `word`.

## How the Code Works
The code iterates through each pattern and checks if it exists as a substring of `word` using the built-in `contains`/`indexOf` method. Count and return the matches.

Time complexity is $O(P \times W)$ where $P$ is total pattern length and $W$ is word length, and space complexity is $O(1)$.
