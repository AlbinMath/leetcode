# LeetCode 1663: Smallest String With A Given Numeric Value

**LeetCode Problem #1663 — Smallest String With A Given Numeric Value**
Solve LeetCode Smallest String With A Given Numeric Value using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest String With A Given Numeric Value |
| LeetCode | #1663 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
The  numeric value  of a  lowercase character  is defined as its position  (1-indexed)  in the alphabet, so the numeric value of  a  is  1 , the numeric value of  b  is  2 , the numeric value of  c  is  3 , and so on.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest String With A Given Numeric Value**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1325. Delete Leaves With a Given Value](../../1001-1500/1450-delete-leaves-with-a-given-value/)
- [2003. Smallest Missing Genetic Value in Each Subtree](../../2001-2500/2131-smallest-missing-genetic-value-in-each-subtree/)
- [2156. Find Substring With Given Hash Value](../../2001-2500/2275-find-substring-with-given-hash-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/)
