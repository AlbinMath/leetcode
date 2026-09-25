# Longest Substring Without Repeating Characters

## Problem Explanation
Given a string `s`, you need to find the length of the longest contiguous substring that does not contain any duplicate characters. 

For example, in the string `"abcabcbb"`, the longest substring without repeating characters is `"abc"`, which has a length of 3. In the string `"bbbbb"`, the longest such substring is `"b"` (length 1).

## How the Code Works
The code uses a **Sliding Window** technique with two pointers (`left` and `right`) and a `set` to keep track of unique characters.
1. It initializes an empty set `seen` to store characters currently in the window, a `left` pointer to represent the start of the window, and a `max_length` to track the longest valid substring found.
2. A `for` loop moves the `right` pointer across the string from left to right, expanding the window.
3. If the character at `s[right]` is already in the `seen` set, it means we found a repeating character. A `while` loop then removes characters from the left side of the window (moving the `left` pointer forward) until the duplicate character is removed from the set.
4. After ensuring the character `s[right]` is not a duplicate in the current window, it adds `s[right]` to the `seen` set.
5. It then updates `max_length` by comparing the current maximum with the size of the current window (`right - left + 1`).
6. Finally, once the `right` pointer finishes scanning the string, `max_length` will contain the length of the longest valid substring.
