# LeetCode 215: Kth Largest Element in an Array

**LeetCode Problem #215 — Kth Largest Element in an Array**
Solve LeetCode Kth Largest Element in an Array using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Largest Element in an Array |
| LeetCode | #215 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and an integer `k`, return *the* `k^th` *largest element in the array*.

Note that it is the `k^th` largest element in the sorted order, not the `k^th` distinct element.

Can you solve it without sorting?

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [3,2,1,5,6,4], k = 2`
- **Output:** `5`

### Example 2
- **Input:** `nums = [3,2,3,1,2,4,5,5,6], k = 4`
- **Output:** `4`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Kth Largest Element in an Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,1,5,6,4], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var findKthLargest = function(nums, k) {
    const target = nums.length - k;
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        // Select a random pivot
        const randomIndex =
            left + Math.floor(Math.random() * (right - left + 1));

        const pivot = nums[randomIndex];

        // Move the pivot to the end
        [nums[randomIndex], nums[right]] =
            [nums[right], nums[randomIndex]];

        // Three-way partition:
        // [left, lt - 1] < pivot
        // [lt, i - 1] === pivot
        // [gt + 1, right] > pivot
        let lt = left;
        let i = left;
        let gt = right;

        while (i <= gt) {
            if (nums[i] < pivot) {
                [nums[lt], nums[i]] = [nums[i], nums[lt]];
                lt++;
                i++;
            } else if (nums[i] > pivot) {
                [nums[i], nums[gt]] = [nums[gt], nums[i]];
                gt--;
            } else {
                i++;
            }
        }

        if (target < lt) {
            right = lt - 1;
        } else if (target > gt) {
            left = gt + 1;
        } else {
            return pivot;
        }
    }

    return -1;
};
```

### Python
```python
class Solution:
    def findKthLargest(self, nums, k):
        import heapq
        return heapq.nlargest(k, nums)[-1]
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [703. Kth Largest Element in a Stream](../../0501-1000/0703-kth-largest-element-in-a-stream/)
- [1985. Find the Kth Largest Integer in the Array](../../1501-2000/1985-find-the-kth-largest-integer-in-the-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)
