# LeetCode 3: Longest Substring Without Repeating Characters

**LeetCode Problem #3 — Longest Substring Without Repeating Characters**
Solve LeetCode Longest Substring Without Repeating Characters using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Substring Without Repeating Characters |
| LeetCode | #3 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s , find the length of the  longest    substring   without duplicate characters.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
The code uses a **Sliding Window** technique with two pointers (`left` and `right`) and a `set` to keep track of unique characters.
1. It initializes an empty set `seen` to store characters currently in the window, a `left` pointer to represent the start of the window, and a `max_length` to track the longest valid substring found.
2. A `for` loop moves the `right` pointer across the string from left to right, expanding the window.
3. If the character at `s[right]` is already in the `seen` set, it means we found a repeating character. A `while` loop then removes characters from the left side of the window (moving the `left` pointer forward) until the duplicate character is removed from the set.
4. After ensuring the character `s[right]` is not a duplicate in the current window, it adds `s[right]` to the `seen` set.
5. It then updates `max_length` by comparing the current maximum with the size of the current window (`right - left + 1`).
6. Finally, once the `right` pointer finishes scanning the string, `max_length` will contain the length of the longest valid substring.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Substring Without Repeating Characters**. Applying **Dynamic Sliding Window Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [2213. Longest Substring of One Repeating Character](../2319-longest-substring-of-one-repeating-character/)
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [14. Longest Common Prefix](../0014-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
