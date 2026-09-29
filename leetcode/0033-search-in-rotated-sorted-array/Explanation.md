# Search In Rotated Sorted Array

## Problem Explanation
There is an integer array `nums` sorted in ascending order (with distinct values) that has been rotated at some unknown pivot index. For example, `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]` after rotating at pivot index 3. Given the rotated array and a `target` value, return the index of `target` if it is in the array, or `-1` if it is not. The algorithm must run in $O(\log N)$ time.

## How the Code Works
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
