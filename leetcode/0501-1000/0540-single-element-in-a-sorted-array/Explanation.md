# LeetCode 540: Single Element in a Sorted Array

**LeetCode Problem #540 — Single Element in a Sorted Array**
Solve LeetCode Single Element in a Sorted Array using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Single Element in a Sorted Array |
| LeetCode | #540 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return *the single element that appears only once*.

Your solution must run in `O(log n)` time and `O(1)` space.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,1,2,3,3,4,4,8,8]`
- **Output:** `2`

### Example 2
- **Input:** `nums = [3,3,7,7,10,11,11]`
- **Output:** `10`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Single Element in a Sorted Array**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,2,3,3,4,4,8,8]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var singleNonDuplicate = function(nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        let mid = Math.floor((left + right) / 2);

        // Ensure mid is even
        if (mid % 2 === 1) {
            mid--;
        }

        if (nums[mid] === nums[mid + 1]) {
            // Single element is in the right half
            left = mid + 2;
        } else {
            // Single element is in the left half, including mid
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
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)
- [1287. Element Appearing More Than 25% In Sorted Array](../../1001-1500/1287-element-appearing-more-than-25-in-sorted-array/)
- [215. Kth Largest Element in an Array](../../0001-0500/0215-kth-largest-element-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/)
