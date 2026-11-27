# LeetCode 33: Search in Rotated Sorted Array

**LeetCode Problem #33 — Search in Rotated Sorted Array**
Solve LeetCode Search in Rotated Sorted Array using C++, JavaScript, Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Search in Rotated Sorted Array |
| LeetCode | #33 |
| Difficulty | Medium |
| Language | C++, JavaScript, Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of *`target`* if it is in *`nums`*, or *`-1`* if it is not in *`nums`.

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [4,5,6,7,0,1,2], target = 0`
- **Output:** `4`

### Example 2
- **Input:** `nums = [4,5,6,7,0,1,2], target = 3`
- **Output:** `-1`

### Example 3
- **Input:** `nums = [1], target = 0`
- **Output:** `-1`

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

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,5,6,7,0,1,2], target = 0`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.

## Complexity Analysis
- **Time Complexity:** O(log n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
C++, JavaScript, Python

## Source Code
- [solution.cpp](./solution.cpp)
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### C++
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target)
                return mid;

            // Left half is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            }
            // Right half is sorted
            else {
                if (nums[mid] < target && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }

        return -1;
    }
};
```

### JavaScript
```javascript
var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (nums[mid] === target) {
            return mid;
        }

        // Left half is sorted
        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        // Right half is sorted
        else {
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
};
```

### Python
```python
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1
```

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
- [81. Search in Rotated Sorted Array II](../../0001-0500/0081-search-in-rotated-sorted-array-ii/)
- [108. Convert Sorted Array to Binary Search Tree](../../0001-0500/0108-convert-sorted-array-to-binary-search-tree/)
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
