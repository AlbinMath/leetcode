# LeetCode 34: Find First and Last Position of Element in Sorted Array

**LeetCode Problem #34 — Find First and Last Position of Element in Sorted Array**
Solve LeetCode Find First and Last Position of Element in Sorted Array using JavaScript, Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find First and Last Position of Element in Sorted Array |
| LeetCode | #34 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [5,7,7,8,8,10], target = 8`
- **Output:** `[3,4]`

### Example 2
- **Input:** `nums = [5,7,7,8,8,10], target = 6`
- **Output:** `[-1,-1]`

### Example 3
- **Input:** `nums = [], target = 0`
- **Output:** `[-1,-1]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find First and Last Position of Element in Sorted Array**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,7,7,8,8,10], target = 8`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4]`.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var searchRange = function(nums, target) {
    function findBound(isFirst) {
        let left = 0;
        let right = nums.length - 1;
        let result = -1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (nums[mid] === target) {
                result = mid;

                if (isFirst) {
                    // Continue searching to the left
                    right = mid - 1;
                } else {
                    // Continue searching to the right
                    left = mid + 1;
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }

    const first = findBound(true);
    const last = findBound(false);

    return [first, last];
};
```

### Python
```python
class Solution:
    def searchRange(self, nums, target):

        def findFirst():
            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    result = mid
                    right = mid - 1   # Keep searching left

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return result

        def findLast():
            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    result = mid
                    left = mid + 1    # Keep searching right

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return result

        return [findFirst(), findLast()]
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
- [154. Find Minimum in Rotated Sorted Array II](../../0001-0500/0154-find-minimum-in-rotated-sorted-array-ii/)
- [540. Single Element in a Sorted Array](../../0501-1000/0540-single-element-in-a-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
