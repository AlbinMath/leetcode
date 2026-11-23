# LeetCode 1389: Create Target Array in the Given Order

**LeetCode Problem #1389 — Create Target Array in the Given Order**
Solve LeetCode Create Target Array in the Given Order using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create Target Array in the Given Order |
| LeetCode | #1389 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given two arrays of integers  nums  and  index . Your task is to create  target  array under the following rules:

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Create Target Array in the Given Order**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1649. Create Sorted Array through Instructions](../../1501-2000/1772-create-sorted-array-through-instructions/)
- [1639. Number of Ways to Form a Target String Given a Dictionary](../../1501-2000/1744-number-of-ways-to-form-a-target-string-given-a-dictionary/)
- [2161. Partition Array According to Given Pivot](../../2001-2500/2265-partition-array-according-to-given-pivot/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-target-array-in-the-given-order/)
