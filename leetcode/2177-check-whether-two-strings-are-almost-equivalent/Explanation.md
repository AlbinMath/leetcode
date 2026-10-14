# LeetCode 2068: Check Whether Two Strings are Almost Equivalent

**LeetCode Problem #2068 — Check Whether Two Strings are Almost Equivalent**
Solve LeetCode Check Whether Two Strings are Almost Equivalent using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check Whether Two Strings are Almost Equivalent |
| LeetCode | #2068 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Two strings  word1  and  word2  are considered  almost equivalent  if the differences between the frequencies of each letter from  &#39;a&#39;  to  &#39;z&#39;  between  word1  and  word2  is  at most   3 .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check Whether Two Strings are Almost Equivalent**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1662. Check If Two String Arrays are Equivalent](../1781-check-if-two-string-arrays-are-equivalent/)
- [1657. Determine if Two Strings Are Close](../1777-determine-if-two-strings-are-close/)
- [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](../1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/)
