# LeetCode 33: Search in Rotated Sorted Array

**LeetCode Problem #33 — Search in Rotated Sorted Array**
Solve LeetCode Search in Rotated Sorted Array using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Search in Rotated Sorted Array |
| LeetCode | #33 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem
There is an integer array  nums  sorted in ascending order (with  distinct  values).

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses a modified **Binary Search** that determines which half of the array is sorted and whether the target lies within that sorted half.

1. **Standard Binary Search Setup:** Two pointers `left` and `right` define the current search range. The middle element is calculated as `mid = left + (right - left) / 2`.
2. **Found:** If `nums[mid] == target`, return `mid`.
3. **Left Half Is Sorted** (`nums[left] <= nums[mid]`):
   - If the target falls within this sorted range (`nums[left] <= target < nums[mid]`), the search narrows to the left half (`right = mid - 1`).
   - Otherwise, it searches the right half (`left = mid + 1`).
4. **Right Half Is Sorted** (when `nums[left] > nums[mid]`):
   - If the target falls within the sorted right range (`nums[mid] < target <= nums[right]`), the search narrows to the right half (`left = mid + 1`).
   - Otherwise, it searches the left half (`right = mid - 1`).
5. If the loop ends without finding the target, it returns `-1`.

The key insight is that in a rotated sorted array, at least one half of the array (split at `mid`) is always sorted. By checking which half is sorted, we can determine if the target lies in that half. Time complexity is $O(\log N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Search in Rotated Sorted Array**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [1878. Get Biggest Three Rhombus Sums in a Grid](../1878-check-if-array-is-sorted-and-rotated/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
