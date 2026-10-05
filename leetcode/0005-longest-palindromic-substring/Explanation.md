# LeetCode 5: Longest Palindromic Substring

**LeetCode Problem #5 — Longest Palindromic Substring**
Solve LeetCode Longest Palindromic Substring using Python and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Palindromic Substring |
| LeetCode | #5 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s , return  the longest    palindromic     substring   in  s .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses the **Expand Around Center** approach. Since a palindrome mirrors around its center, we can iterate through the string and treat each character (or pair of characters) as a potential center, expanding outwards as long as the characters match.

1. It initializes `start` and `end` variables to keep track of the indices of the longest palindrome found so far.
2. It defines a helper function `expand(left, right)` which takes the starting center indices. It uses a `while` loop to expand outwards (`left -= 1` and `right += 1`) as long as the indices are within bounds and the characters at those indices are equal. It returns the boundaries of the identified palindrome.
3. It iterates through each character index `i` in the string:
   - **Odd-length Palindromes**: It calls `expand(i, i)` treating the single character at `i` as the center (e.g., "aba").
   - **Even-length Palindromes**: It calls `expand(i, i + 1)` treating the gap between `i` and `i+1` as the center (e.g., "abba").
4. After each expansion, it checks if the length of the newly found palindrome (`right - left`) is greater than the currently recorded maximum length (`end - start`). If it is, it updates `start` and `end`.
5. Finally, it returns the substring `s[start : end + 1]`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Palindromic Substring**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3. Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/)
- [2319. Check if Matrix Is X-Matrix](../2319-longest-substring-of-one-repeating-character/)
- [14. Longest Common Prefix](../0014-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)
