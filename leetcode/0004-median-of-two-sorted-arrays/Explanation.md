# Median of Two Sorted Arrays

## Problem Explanation
You are given two sorted integer arrays, `nums1` and `nums2`, of sizes `m` and `n` respectively. The task is to find the **median** of the two arrays when combined. The median is the middle element of a sorted array (or the average of the two middle elements if the total number of elements is even).

A crucial constraint is that the overall run time complexity must be **O(log (m+n))**. This means you cannot simply merge the two arrays and find the median (which would be O(m+n)).

## How the Code Works
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
