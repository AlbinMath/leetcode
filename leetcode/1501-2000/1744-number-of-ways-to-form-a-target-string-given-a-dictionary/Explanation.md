# LeetCode 1639: Number of Ways to Form a Target String Given a Dictionary

**LeetCode Problem #1639 — Number of Ways to Form a Target String Given a Dictionary**
Solve LeetCode Number of Ways to Form a Target String Given a Dictionary using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Form a Target String Given a Dictionary |
| LeetCode | #1639 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a list of strings of the  same length   words  and a string  target .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Ways to Form a Target String Given a Dictionary**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1633-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)
- [3291. Minimum Number of Valid Strings to Form Target I](../../3501-4000/3559-minimum-number-of-valid-strings-to-form-target-i/)
- [3292. Minimum Number of Valid Strings to Form Target II](../../3501-4000/3557-minimum-number-of-valid-strings-to-form-target-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/)
