# LeetCode 2707: Extra Characters in a String

**LeetCode Problem #2707 — Extra Characters in a String**
Solve LeetCode Extra Characters in a String using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Extra Characters in a String |
| LeetCode | #2707 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  string  s  and a dictionary of words  dictionary . You have to break  s  into one or more  non-overlapping  substrings such that each substring is present in  dictionary . There may be some  extra characters  in  s  which are not present in any of the substrings.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Extra Characters in a String**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1374. Generate a String With Characters That Have Odd Counts](../1490-generate-a-string-with-characters-that-have-odd-counts/)
- [1957. Delete Characters to Make Fancy String](../1302-delete-characters-to-make-fancy-string/)
- [3. Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/extra-characters-in-a-string/)
