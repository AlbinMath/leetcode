# LeetCode 154: Find Minimum in Rotated Sorted Array II

**LeetCode Problem #154 — Find Minimum in Rotated Sorted Array II**
Solve LeetCode Find Minimum in Rotated Sorted Array II using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Minimum in Rotated Sorted Array II |
| LeetCode | #154 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,4,4,5,6,7]` might become:

`[4,5,6,7,0,1,4]` if it was rotated `4` times. 
 `[0,1,4,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` that may contain **duplicates**, return *the minimum element of this array*.

You must decrease the overall operation steps as much as possible.

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- `nums` is sorted and rotated between `1` and `n` times.

## Examples
### Example 1
- **Input:** `nums = [1,3,5]`
- **Output:** `1`

### Example 2
- **Input:** `nums = [2,2,2,0,1]`
- **Output:** `0`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **Binary Search** with an extra case to handle duplicates.

1. It maintains two pointers `left` and `right`.
2. In each iteration, it calculates `mid`.
3. **Three Cases:**
   - `nums[mid] < nums[right]`: The minimum is at `mid` or to the left → `right = mid`.
   - `nums[mid] > nums[right]`: The minimum is in the right half → `left = mid + 1`.
   - `nums[mid] == nums[right]`: **Duplicates make it impossible to determine which side the minimum is on.** The solution safely decrements `right--`. This only eliminates one duplicate and doesn't risk skipping the minimum.
4. When `left === right`, `nums[left]` is the minimum.

The worst-case time complexity is $O(N)$ (when all elements are duplicates), but the average case is $O(\log N)$. Space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,5]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

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


```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] < nums[right]) {
                right = mid;
            }
            else if (nums[mid] > nums[right]) {
                left = mid + 1;
            }
            else {
                // Duplicates: cannot determine the side
                right--;
            }
        }

        return nums[left];
    }
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
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)
- [3011. Find if Array Can Be Sorted](../../3001-3500/3011-find-if-array-can-be-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
