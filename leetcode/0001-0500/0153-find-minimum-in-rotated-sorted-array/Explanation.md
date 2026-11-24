# LeetCode 153: Find Minimum in Rotated Sorted Array

**LeetCode Problem #153 — Find Minimum in Rotated Sorted Array**
Solve LeetCode Find Minimum in Rotated Sorted Array using C++, JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Minimum in Rotated Sorted Array |
| LeetCode | #153 |
| Difficulty | Medium |
| Language | C++, JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

`[4,5,6,7,0,1,2]` if it was rotated `4` times. 
 `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n) time`.

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

## Examples
### Example 1
- **Input:** `nums = [3,4,5,1,2]`
- **Output:** `1`
- **Explanation:** The original array was [1,2,3,4,5] rotated 3 times.

### Example 2
- **Input:** `nums = [4,5,6,7,0,1,2]`
- **Output:** `0`
- **Explanation:** The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

### Example 3
- **Input:** `nums = [11,13,15,17]`
- **Output:** `11`
- **Explanation:** The original array was [11,13,15,17] and it was rotated 4 times.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **Binary Search** to find the minimum.

1. It maintains two pointers `left` and `right`.
2. In each iteration, it calculates `mid = left + (right - left) / 2`.
3. **Key Decision:**
   - If `nums[mid] > nums[right]`: The minimum must be in the right half (the rotation point is to the right of `mid`), so `left = mid + 1`.
   - Otherwise (`nums[mid] <= nums[right]`): The minimum is at `mid` or to the left, so `right = mid`.
4. When `left === right`, the minimum element has been found.

Time complexity is $O(\log N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,4,5,1,2]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The original array was [1,2,3,4,5] rotated 3 times.

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
C++, JavaScript

## Source Code
- [solution.cpp](./solution.cpp)
- [solution.js](./solution.js)


### C++
```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }
};
```

### JavaScript
```javascript
var findMin = function(nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (nums[mid] > nums[right]) {
            // Minimum is in the right half
            left = mid + 1;
        } else {
            // Minimum is at mid or in the left half
            right = mid;
        }
    }

    return nums[left];
};
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
- [154. Find Minimum in Rotated Sorted Array II](../../0001-0500/0154-find-minimum-in-rotated-sorted-array-ii/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
