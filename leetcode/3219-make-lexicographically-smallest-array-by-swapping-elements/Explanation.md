# LeetCode 2948: Make Lexicographically Smallest Array by Swapping Elements

**LeetCode Problem #2948 — Make Lexicographically Smallest Array by Swapping Elements**
Solve LeetCode Make Lexicographically Smallest Array by Swapping Elements using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Lexicographically Smallest Array by Swapping Elements |
| LeetCode | #2948 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  array of  positive  integers  nums  and a  positive  integer  limit .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Make Lexicographically Smallest Array by Swapping Elements**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1887. Reduction Operations to Make the Array Elements Equal](../2016-reduction-operations-to-make-the-array-elements-equal/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../2753-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [1464. Maximum Product of Two Elements in an Array](../1574-maximum-product-of-two-elements-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/)
