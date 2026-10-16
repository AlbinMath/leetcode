# LeetCode 1318: Minimum Flips to Make a OR b Equal to c

**LeetCode Problem #1318 — Minimum Flips to Make a OR b Equal to c**
Solve LeetCode Minimum Flips to Make a OR b Equal to c using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Flips to Make a OR b Equal to c |
| LeetCode | #1318 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given 3 positives numbers  a ,  b  and  c . Return the minimum flips required in some bits of  a  and  b  to make (  a  OR  b  ==  c  ). (bitwise OR operation).

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Flips to Make a OR b Equal to c**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../2753-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [921. Minimum Add to Make Parentheses Valid](../0957-minimum-add-to-make-parentheses-valid/)
- [1460. Make Two Arrays Equal by Reversing Subarrays](../1556-make-two-arrays-equal-by-reversing-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)
