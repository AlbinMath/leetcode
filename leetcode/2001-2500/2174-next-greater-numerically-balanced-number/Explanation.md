# LeetCode 2048: Next Greater Numerically Balanced Number

**LeetCode Problem #2048 — Next Greater Numerically Balanced Number**
Solve LeetCode Next Greater Numerically Balanced Number using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Next Greater Numerically Balanced Number |
| LeetCode | #2048 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
An integer  x  is  numerically balanced  if for every digit  d  in the number  x , there are  exactly   d  occurrences of that digit in  x .

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Next Greater Numerically Balanced Number**. Applying **Monotonic Stack Filtering** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
- [1963. Minimum Number of Swaps to Make the String Balanced](../../2001-2500/2095-minimum-number-of-swaps-to-make-the-string-balanced/)
- [3343. Count Number of Balanced Permutations](../../3501-4000/3637-count-number-of-balanced-permutations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/next-greater-numerically-balanced-number/)
