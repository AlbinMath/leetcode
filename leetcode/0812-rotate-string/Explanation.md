# Rotate String

## Problem Explanation
Given two strings `s` and `goal`, return `true` if `s` can become `goal` after some number of rotations (shifts) of `s`. A rotation moves the first character of `s` to the end.

For example, `s = "abcde"` and `goal = "cdeab"` → `true` (rotate left by 2).

## How the Code Works
The code uses a clever **string concatenation** trick:

1. **Length Check:** If the lengths differ, return `false` immediately.
2. **Concatenation:** It concatenates `s` with itself: `s + s`. This doubled string contains every possible rotation of `s` as a substring. For example, `"abcde" + "abcde" = "abcdeabcde"` contains `"cdeab"` as a substring.
3. **Find:** It checks if `goal` exists anywhere in `s + s` using `.find()`. If found, `goal` is a valid rotation.

Time complexity is $O(N)$ with an efficient string search and space complexity is $O(N)$ for the concatenated string.
