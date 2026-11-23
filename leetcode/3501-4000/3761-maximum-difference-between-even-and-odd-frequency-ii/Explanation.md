# LeetCode 3445: Maximum Difference Between Even and Odd Frequency II

**LeetCode Problem #3445 — Maximum Difference Between Even and Odd Frequency II**
Solve LeetCode Maximum Difference Between Even and Odd Frequency II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Difference Between Even and Odd Frequency II |
| LeetCode | #3445 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a string  s  and an integer  k . Your task is to find the  maximum  difference between the frequency of  two  characters,  freq[a] - freq[b] , in a  substring   subs  of  s , such that:

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Difference Between Even and Odd Frequency II**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1092-maximum-difference-between-node-and-ancestor/)
- [1913. Maximum Product Difference Between Two Pairs](../../2001-2500/2042-maximum-product-difference-between-two-pairs/)
- [328. Odd Even Linked List](../../0001-0500/0328-odd-even-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/)
