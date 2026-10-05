# LeetCode 1520: Maximum Number of Non-Overlapping Substrings

**LeetCode Problem #1520 — Maximum Number of Non-Overlapping Substrings**
Solve LeetCode Maximum Number of Non-Overlapping Substrings using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Non-Overlapping Substrings |
| LeetCode | #1520 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  s  of lowercase letters, you need to find the maximum number of  non-empty  substrings of  s  that meet the following conditions:

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **Greedy** approach. It first finds the leftmost and rightmost occurrence of each character. Then for each potential starting character, it expands the substring to include all occurrences of all characters within it. Finally, it greedily selects non-overlapping substrings by preferring shorter ones that end earliest.

Time complexity is $O(N \times |\Sigma|)$ and space complexity is $O(|\Sigma|)$ where $|\Sigma|$ is the alphabet size.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Number of Non-Overlapping Substrings**. Applying **Min/Max Heap Priority Selection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2472. Maximum Number of Non-overlapping Palindrome Substrings](../2559-maximum-number-of-non-overlapping-palindrome-substrings/)
- [1621. Number of Sets of K Non-Overlapping Line Segments](../1725-number-of-sets-of-k-non-overlapping-line-segments/)
- [3414. Maximum Score of Non-overlapping Intervals](../3562-maximum-score-of-non-overlapping-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)
