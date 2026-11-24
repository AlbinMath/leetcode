# LeetCode 4: Median of Two Sorted Arrays

**LeetCode Problem #4 — Median of Two Sorted Arrays**
Solve LeetCode Median of Two Sorted Arrays using JavaScript, Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Median of Two Sorted Arrays |
| LeetCode | #4 |
| Difficulty | Hard |
| Language | JavaScript, Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

## Constraints
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums1 = [1,3], nums2 = [2]`
- **Output:** `2.00000`
- **Explanation:** merged array = [1,2,3] and median is 2.

### Example 2
- **Input:** `nums1 = [1,2], nums2 = [3,4]`
- **Output:** `2.50000`
- **Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

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

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,3], nums2 = [2]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2.00000`.
4. **Verification:** merged array = [1,2,3] and median is 2.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var findMedianSortedArrays = function(nums1, nums2) {
    // Always binary-search the smaller array
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }

    const m = nums1.length;
    const n = nums2.length;

    let left = 0;
    let right = m;

    while (left <= right) {
        const i = Math.floor((left + right) / 2);
        const j = Math.floor((m + n + 1) / 2) - i;

        const left1 = i === 0 ? -Infinity : nums1[i - 1];
        const right1 = i === m ? Infinity : nums1[i];

        const left2 = j === 0 ? -Infinity : nums2[j - 1];
        const right2 = j === n ? Infinity : nums2[j];

        // Correct partition
        if (left1 <= right2 && left2 <= right1) {
            if ((m + n) % 2 === 1) {
                return Math.max(left1, left2);
            }

            return (
                Math.max(left1, left2) +
                Math.min(right1, right2)
            ) / 2;
        }

        // Too many elements taken from nums1
        if (left1 > right2) {
            right = i - 1;
        } else {
            // Too few elements taken from nums1
            left = i + 1;
        }
    }

    return 0; // Unreachable for valid input
};
```

### Python
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == m else nums1[i]

            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                return (max(left1, left2) + min(right1, right2)) / 2.0

            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1

        return 0.0
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
- [2040. Kth Smallest Product of Two Sorted Arrays](../../2001-2500/2040-kth-smallest-product-of-two-sorted-arrays/)
- [21. Merge Two Sorted Lists](../../0001-0500/0021-merge-two-sorted-lists/)
- [167. Two Sum II - Input Array Is Sorted](../../0001-0500/0167-two-sum-ii-input-array-is-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)
