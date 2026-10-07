# LeetCode 76: Minimum Window Substring

**LeetCode Problem #76 — Minimum Window Substring**
Solve LeetCode Minimum Window Substring using PHP and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Window Substring |
| LeetCode | #76 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two strings  s  and  t  of lengths  m  and  n  respectively, return  the  minimum window      substring     of   s   such that every character in   t   ( including duplicates ) is included in the window . If there is no such substring, return  the empty string   "" .

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
We iterate through the input using **Dynamic Sliding Window Traversal**. By maintaining state efficiently in a **Array / Hash Set**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Window Substring**. Applying **Dynamic Sliding Window Traversal** yields the target result step by step.

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
PHP

## Source Code
- [solution.php](./solution.php)

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
- [3. Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [30. Substring with Concatenation of All Words](../0030-substring-with-concatenation-of-all-words/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-window-substring/)
