# LeetCode 3413: Maximum Coins From K Consecutive Bags

**LeetCode Problem #3413 — Maximum Coins From K Consecutive Bags**
Solve LeetCode Maximum Coins From K Consecutive Bags using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Coins From K Consecutive Bags |
| LeetCode | #3413 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There are an infinite amount of bags on a number line, one bag for each coordinate. Some of these bags contain coins.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Coins From K Consecutive Bags**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [2920. Maximum Points After Collecting Coins From All Nodes](../../3001-3500/3179-maximum-points-after-collecting-coins-from-all-nodes/)
- [1191. K-Concatenation Maximum Sum](../../1001-1500/1299-k-concatenation-maximum-sum/)
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1424-maximum-candies-you-can-get-from-boxes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/)
