# LeetCode 524: Longest Word in Dictionary through Deleting

**LeetCode Problem #524 — Longest Word in Dictionary through Deleting**
Solve LeetCode Longest Word in Dictionary through Deleting using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Word in Dictionary through Deleting |
| LeetCode | #524 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  s  and a string array  dictionary , return  the longest string in the dictionary that can be formed by deleting some of the given string characters . If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Word in Dictionary through Deleting**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [720. Longest Word in Dictionary](../../0501-1000/0720-longest-word-in-dictionary/)
- [1493. Longest Subarray of 1's After Deleting One Element](../../1501-2000/1586-longest-subarray-of-1s-after-deleting-one-element/)
- [676. Implement Magic Dictionary](../../0501-1000/0676-implement-magic-dictionary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)
