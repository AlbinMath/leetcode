# LeetCode 1170: Compare Strings by Frequency of the Smallest Character

**LeetCode Problem #1170 — Compare Strings by Frequency of the Smallest Character**
Solve LeetCode Compare Strings by Frequency of the Smallest Character using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Compare Strings by Frequency of the Smallest Character |
| LeetCode | #1170 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Let the function  f(s)  be the  frequency of the lexicographically smallest character  in a non-empty string  s . For example, if  s = "dcce"  then  f(s) = 2  because the lexicographically smallest character is  &#39;c&#39; , which has a frequency of 2.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Compare Strings by Frequency of the Smallest Character**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [387. First Unique Character in a String](../0387-first-unique-character-in-a-string/)
- [424. Longest Repeating Character Replacement](../0424-longest-repeating-character-replacement/)
- [821. Shortest Distance to a Character](../0841-shortest-distance-to-a-character/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/)
