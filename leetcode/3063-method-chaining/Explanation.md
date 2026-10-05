# LeetCode 3063: Linked List Frequency

**LeetCode Problem #3063 — Linked List Frequency**
Solve LeetCode Linked List Frequency using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Linked List Frequency |
| LeetCode | #3063 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Write a solution to list the names of animals that weigh  strictly more than   100  kilograms.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Linked List Frequency**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [2863. Maximum Length of Semi-Decreasing Subarrays](../2863-calculator-with-method-chaining/)
- [1. Two Sum](../0001-two-sum/)
- [13. Roman to Integer](../0013-roman-to-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/method-chaining/)
