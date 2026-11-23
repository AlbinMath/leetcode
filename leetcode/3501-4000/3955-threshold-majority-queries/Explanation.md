# LeetCode 3636: Threshold Majority Queries

**LeetCode Problem #3636 — Threshold Majority Queries**
Solve LeetCode Threshold Majority Queries using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Threshold Majority Queries |
| LeetCode | #3636 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums  of length  n  and an array  queries , where  queries[i] = [l i , r i , threshold i ] .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Threshold Majority Queries**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](../../1001-1500/1413-maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../../1001-1500/1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/threshold-majority-queries/)
