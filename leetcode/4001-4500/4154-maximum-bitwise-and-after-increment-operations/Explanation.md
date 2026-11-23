# LeetCode 3806: Maximum Bitwise AND After Increment Operations

**LeetCode Problem #3806 — Maximum Bitwise AND After Increment Operations**
Solve LeetCode Maximum Bitwise AND After Increment Operations using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Bitwise AND After Increment Operations |
| LeetCode | #3806 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums  and two integers  k  and  m .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Bitwise AND After Increment Operations**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [3849. Maximum Bitwise XOR After Rearrangement](../../4001-4500/4044-maximum-bitwise-xor-after-rearrangement/)
- [2317. Maximum XOR After Operations ](../../2001-2500/2402-maximum-xor-after-operations-/)
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3501-4000/3622-maximum-frequency-of-an-element-after-performing-operations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/)
