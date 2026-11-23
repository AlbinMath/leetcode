# LeetCode 1641: Count Sorted Vowel Strings

**LeetCode Problem #1641 — Count Sorted Vowel Strings**
Solve LeetCode Count Sorted Vowel Strings using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Sorted Vowel Strings |
| LeetCode | #1641 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer  n , return  the number of strings of length   n   that consist only of vowels (  a  ,   e  ,   i  ,   o  ,   u  ) and are  lexicographically sorted .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Sorted Vowel Strings**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1351. Count Negative Numbers in a Sorted Matrix](../1476-count-negative-numbers-in-a-sorted-matrix/)
- [1684. Count the Number of Consistent Strings](../1786-count-the-number-of-consistent-strings/)
- [2062. Count Vowel Substrings of a String](../2186-count-vowel-substrings-of-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-sorted-vowel-strings/)
