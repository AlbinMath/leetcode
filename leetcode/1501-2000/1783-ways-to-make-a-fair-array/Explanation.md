# LeetCode 1664: Ways to Make a Fair Array

**LeetCode Problem #1664 — Ways to Make a Fair Array**
Solve LeetCode Ways to Make a Fair Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Ways to Make a Fair Array |
| LeetCode | #1664 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums . You can choose  exactly one  index ( 0-indexed ) and remove the element. Notice that the index of the elements may change after the removal.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Ways to Make a Fair Array**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1735. Count Ways to Make Array With Product](../../1501-2000/1836-count-ways-to-make-array-with-product/)
- [1558. Minimum Numbers of Function Calls to Make Target Array](../../1501-2000/1662-minimum-numbers-of-function-calls-to-make-target-array/)
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../../1501-2000/1679-shortest-subarray-to-be-removed-to-make-array-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/ways-to-make-a-fair-array/)
