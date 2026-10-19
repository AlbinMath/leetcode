# LeetCode 2227: Encrypt and Decrypt Strings

**LeetCode Problem #2227 — Encrypt and Decrypt Strings**
Solve LeetCode Encrypt and Decrypt Strings using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Encrypt and Decrypt Strings |
| LeetCode | #2227 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a character array  keys  containing  unique  characters and a string array  values  containing strings of length 2. You are also given another string array  dictionary  that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a  0-indexed  string.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Encrypt and Decrypt Strings**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [43. Multiply Strings](../0043-multiply-strings/)
- [205. Isomorphic Strings](../0205-isomorphic-strings/)
- [415. Add Strings](../0415-add-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/encrypt-and-decrypt-strings/)
