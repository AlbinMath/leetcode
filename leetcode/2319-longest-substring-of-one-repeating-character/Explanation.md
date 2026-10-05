# LeetCode 2213: Longest Substring of One Repeating Character

**LeetCode Problem #2213 — Longest Substring of One Repeating Character**
Solve LeetCode Longest Substring of One Repeating Character using Java and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Substring of One Repeating Character |
| LeetCode | #2213 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  string  s . You are also given a  0-indexed  string  queryCharacters  of length  k  and a  0-indexed  array of integer  indices   queryIndices  of length  k , both of which are used to describe  k  queries.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses a **Segment Tree** where each node stores: the longest repeating prefix, suffix, and overall substring, plus the characters at the boundaries. Merging two segments checks if the suffix of the left and prefix of the right share the same character.

Time complexity is $O((N + Q) \log N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Substring of One Repeating Character**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3. Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [14. Longest Common Prefix](../0014-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)
