# Longest Palindromic Substring

## Problem Explanation
Given a string `s`, you need to find the longest substring within it that is a **palindrome**. A palindrome is a string that reads the same forwards and backwards.

For example, in the string `"babad"`, the longest palindromic substring is `"bab"` (or `"aba"`). In `"cbbd"`, it is `"bb"`.

## How the Code Works
The code uses the **Expand Around Center** approach. Since a palindrome mirrors around its center, we can iterate through the string and treat each character (or pair of characters) as a potential center, expanding outwards as long as the characters match.

1. It initializes `start` and `end` variables to keep track of the indices of the longest palindrome found so far.
2. It defines a helper function `expand(left, right)` which takes the starting center indices. It uses a `while` loop to expand outwards (`left -= 1` and `right += 1`) as long as the indices are within bounds and the characters at those indices are equal. It returns the boundaries of the identified palindrome.
3. It iterates through each character index `i` in the string:
   - **Odd-length Palindromes**: It calls `expand(i, i)` treating the single character at `i` as the center (e.g., "aba").
   - **Even-length Palindromes**: It calls `expand(i, i + 1)` treating the gap between `i` and `i+1` as the center (e.g., "abba").
4. After each expansion, it checks if the length of the newly found palindrome (`right - left`) is greater than the currently recorded maximum length (`end - start`). If it is, it updates `start` and `end`.
5. Finally, it returns the substring `s[start : end + 1]`.
