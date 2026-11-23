# LeetCode 1450: Number of Students Doing Homework at a Given Time

**LeetCode Problem #1450 — Number of Students Doing Homework at a Given Time**
Solve LeetCode Number of Students Doing Homework at a Given Time using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Students Doing Homework at a Given Time |
| LeetCode | #1450 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given two integer arrays  startTime  and  endTime  and given an integer  queryTime .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Students Doing Homework at a Given Time**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [949. Largest Time for Given Digits](../../0501-1000/0986-largest-time-for-given-digits/)
- [1456. Maximum Number of Vowels in a Substring of Given Length](../../1501-2000/1567-maximum-number-of-vowels-in-a-substring-of-given-length/)
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1501-2000/1621-number-of-subsequences-that-satisfy-the-given-sum-condition/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/)
