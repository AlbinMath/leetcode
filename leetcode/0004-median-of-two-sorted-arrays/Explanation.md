# LeetCode 4: Median of Two Sorted Arrays

**LeetCode Problem #4 — Median of Two Sorted Arrays**
Solve LeetCode Median of Two Sorted Arrays using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Median of Two Sorted Arrays |
| LeetCode | #4 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two sorted arrays  nums1  and  nums2  of size  m  and  n  respectively, return  the median  of the two sorted arrays.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To achieve the O(log (m+n)) time complexity, the code uses **Binary Search**. Instead of searching for the median element itself, it searches for the correct "partition" (cut) across the two arrays.

1. First, it ensures that `nums1` is always the smaller array to minimize the search space.
2. It uses binary search on `nums1` using `left` and `right` pointers. It partitions both arrays such that the total number of elements on the left side of both partitions is roughly equal to the right side (specifically `(m + n + 1) // 2`).
3. For a given partition in `nums1` (`partition1`) and `nums2` (`partition2`), it identifies the maximum elements on the left side (`maxLeft1`, `maxLeft2`) and the minimum elements on the right side (`minRight1`, `minRight2`).
4. **Valid Partition Check**: A partition is valid if all elements on the left are less than or equal to all elements on the right. This translates to `maxLeft1 <= minRight2` and `maxLeft2 <= minRight1`.
5. If the partition is valid:
   - For an odd total length, the median is the maximum of the left side.
   - For an even total length, the median is the average of the maximum left element and the minimum right element.
6. If `maxLeft1 > minRight2`, the partition in `nums1` is too far right, so we move it to the left (`right = partition1 - 1`).
7. Otherwise, the partition in `nums1` is too far left, so we move it to the right (`left = partition1 + 1`).

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Median of Two Sorted Arrays**. Applying **Modified Binary Search** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [2657. Find the Prefix Common Array of Two Arrays](../2766-find-the-prefix-common-array-of-two-arrays/)
- [2722. Join Two Arrays by ID](../2858-join-two-arrays-by-id/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)
