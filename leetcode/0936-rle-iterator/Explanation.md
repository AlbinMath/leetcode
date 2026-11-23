# LeetCode 900: RLE Iterator

**LeetCode Problem #900 — RLE Iterator**
Solve LeetCode RLE Iterator using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | RLE Iterator |
| LeetCode | #900 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
We can use run-length encoding (i.e.,  RLE ) to encode a sequence of integers. In a run-length encoded array of even length  encoding  ( 0-indexed ), for all even  i ,  encoding[i]  tells us the number of times that the non-negative integer value  encoding[i + 1]  is repeated in the sequence.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **RLE Iterator**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [173. Binary Search Tree Iterator](../0173-binary-search-tree-iterator/)
- [284. Peeking Iterator](../0284-peeking-iterator/)
- [341. Flatten Nested List Iterator](../0341-flatten-nested-list-iterator/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rle-iterator/)
