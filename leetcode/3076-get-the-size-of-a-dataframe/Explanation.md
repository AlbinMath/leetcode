# LeetCode 2878: Get the Size of a DataFrame

**LeetCode Problem #2878 — Get the Size of a DataFrame**
Solve LeetCode Get the Size of a DataFrame using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Get the Size of a DataFrame |
| LeetCode | #2878 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Write a solution to calculate and display the  number of rows and columns  of  players .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Get the Size of a DataFrame**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [961. N-Repeated Element in Size 2N Array](../1001-n-repeated-element-in-size-2n-array/)
- [1413. Minimum Value to Get Positive Step by Step Sum](../1514-minimum-value-to-get-positive-step-by-step-sum/)
- [1646. Get Maximum in Generated Array](../1769-get-maximum-in-generated-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/get-the-size-of-a-dataframe/)
