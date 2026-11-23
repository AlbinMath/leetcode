# LeetCode 828: Count Unique Characters of All Substrings of a Given String

**LeetCode Problem #828 — Count Unique Characters of All Substrings of a Given String**
Solve LeetCode Count Unique Characters of All Substrings of a Given String using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Unique Characters of All Substrings of a Given String |
| LeetCode | #828 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Let&#39;s define a function  countUniqueChars(s)  that returns the number of unique characters in  s .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Unique Characters of All Substrings of a Given String**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [1358. Number of Substrings Containing All Three Characters](../../1001-1500/1460-number-of-substrings-containing-all-three-characters/)
- [2062. Count Vowel Substrings of a String](../../2001-2500/2186-count-vowel-substrings-of-a-string/)
- [3297. Count Substrings That Can Be Rearranged to Contain a String I](../../3501-4000/3573-count-substrings-that-can-be-rearranged-to-contain-a-string-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/)
