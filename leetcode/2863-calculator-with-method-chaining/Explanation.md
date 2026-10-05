# LeetCode 2863: Maximum Length of Semi-Decreasing Subarrays

**LeetCode Problem #2863 — Maximum Length of Semi-Decreasing Subarrays**
Solve LeetCode Maximum Length of Semi-Decreasing Subarrays using TypeScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Length of Semi-Decreasing Subarrays |
| LeetCode | #2863 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Design a  Calculator  class. The class should provide the mathematical operations of addition, subtraction, multiplication, division, and exponentiation. It should also allow consecutive operations to be performed using method chaining. The  Calculator  class constructor should accept a number which serves as the initial value of  result .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Each method (`add`, `subtract`, `multiply`, `divide`) modifies the internal `result` and returns `this` to enable chaining. `divide` throws an error if dividing by zero. `getResult` returns the current value.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Length of Semi-Decreasing Subarrays**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [3063. Linked List Frequency](../3063-method-chaining/)
- [1. Two Sum](../0001-two-sum/)
- [13. Roman to Integer](../0013-roman-to-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/calculator-with-method-chaining/)
