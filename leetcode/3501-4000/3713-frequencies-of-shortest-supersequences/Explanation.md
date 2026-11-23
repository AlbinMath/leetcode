# LeetCode 3435: Frequencies of Shortest Supersequences

**LeetCode Problem #3435 — Frequencies of Shortest Supersequences**
Solve LeetCode Frequencies of Shortest Supersequences using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Frequencies of Shortest Supersequences |
| LeetCode | #3435 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array of strings  words . Find all  shortest common supersequences (SCS)  of   words   that are not  permutations  of each other.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Frequencies of Shortest Supersequences**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1647. Minimum Deletions to Make Character Frequencies Unique](../../1501-2000/1770-minimum-deletions-to-make-character-frequencies-unique/)
- [3389. Minimum Operations to Make Character Frequencies Equal](../../3501-4000/3638-minimum-operations-to-make-character-frequencies-equal/)
- [214. Shortest Palindrome](../../0001-0500/0214-shortest-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/frequencies-of-shortest-supersequences/)
