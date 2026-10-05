# LeetCode 3525: Find X Value of Array II

**LeetCode Problem #3525 — Find X Value of Array II**
Solve LeetCode Find X Value of Array II using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find X Value of Array II |
| LeetCode | #3525 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of  positive  integers  nums  and a  positive  integer  k . You are also given a 2D array  queries , where  queries[i] = [index i , value i , start i , x i ] .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
Because updates are persistent and there can be many queries, calculating the answers iteratively would be too slow. The code uses a **Segment Tree** to answer queries and handle updates efficiently.

1. **Segment Tree Structure**:
   - `prod` stores the product modulo `k` of all elements within a segment.
   - `cnt` is flattened 2D array. For each segment node, it stores an array of size `k` where `cnt[node * k + r]` is the number of valid prefixes (relative to the segment's start) whose product modulo `k` is `r`.
2. **Building the Tree**:
   - It initializes the leaves with individual array elements.
   - For internal nodes, it computes the `prod` as the product of its left and right children modulo `k`.
   - The `cnt` for an internal node is formed by:
     - Taking all prefixes from the left child (as they are also prefixes of the parent segment).
     - Taking prefixes from the right child, but multiplying their products by the total product of the left child, because a prefix extending into the right child must include all of the left child.
3. **Updating (`update` function)**:
   - When an element is updated, it updates the corresponding leaf node's `prod` and `cnt`.
   - It then traverses up the tree to the root, recalculating `prod` and `cnt` for every ancestor just like during the build phase.
4. **Querying (`query` function)**:
   - To find the counts for a subarray starting at `start` and ending at `n-1`, it queries the segment tree for the range `[start, n)`.
   - It accumulates the results from left to right. Just like building nodes, it keeps a running `leftProd` and a `leftCnt` array, merging them with the relevant nodes from the segment tree to compute the final counts of prefix products for the requested range.
5. For each query, it performs the update, calls the query function, and pushes the count for the requested remainder `x` into the `result` array.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find X Value of Array II**. Applying **Modified Binary Search** yields the target result step by step.

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
- [3524. Find X Value of Array I](../3831-find-x-value-of-array-i/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-x-value-of-array-ii/)
