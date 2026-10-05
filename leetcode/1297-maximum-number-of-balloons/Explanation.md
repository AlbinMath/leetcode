# LeetCode 1297: Maximum Number of Occurrences of a Substring

**LeetCode Problem #1297 — Maximum Number of Occurrences of a Substring**
Solve LeetCode Maximum Number of Occurrences of a Substring using Kotlin and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Occurrences of a Substring |
| LeetCode | #1297 |
| Difficulty | Medium |
| Language | Kotlin |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  text , you want to use the characters of  text  to form as many instances of the word  "balloon"  as possible.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
1. **Count Characters:** Count the frequency of every character in the text.
2. **Check Required Characters:** The word "balloon" needs: `b`×1, `a`×1, `l`×2, `o`×2, `n`×1.
3. **Bottleneck:** The answer is the minimum of: count of `b`, count of `a`, count of `l` divided by 2, count of `o` divided by 2, and count of `n`. The character with the smallest available count determines how many complete "balloon"s can be formed.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Number of Occurrences of a Substring**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1644. Lowest Common Ancestor of a Binary Tree II](../1644-maximum-number-of-non-overlapping-substrings/)
- [2182. Construct String With Repeat Limit](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [2559. Count Vowel Strings in Ranges](../2559-maximum-number-of-non-overlapping-palindrome-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/)
