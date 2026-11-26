# LeetCode 2420: Find All Good Indices

**LeetCode Problem #2420 — Find All Good Indices**
Solve LeetCode Find All Good Indices using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Good Indices |
| LeetCode | #2420 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of size `n` and a positive integer `k`.

We call an index `i` in the range `k <= i < n - k` **good** if the following conditions are satisfied:

The `k` elements that are just **before** the index `i` are in **non-increasing** order. 
 The `k` elements that are just **after** the index `i` are in **non-decreasing** order.

Return *an array of all good indices sorted in **increasing** order*.

## Constraints
- `n == nums.length`
- `3 <= n <= 10^5`
- `1 <= nums[i] <= 10^6`
- `1 <= k <= n / 2`

## Examples
### Example 1
- **Input:** `nums = [2,1,1,1,3,4,1], k = 2`
- **Output:** `[2,3]`
- **Explanation:** There are two good indices in the array:
- Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in non-decreasing order.
- Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in non-decreasing order.
Note that the index 4 is not good because [4,1] is not non-decreasing.

### Example 2
- **Input:** `nums = [2,1,1,2], k = 2`
- **Output:** `[]`
- **Explanation:** There are no good indices in this array.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find All Good Indices**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,1,1,3,4,1], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3]`.
4. **Verification:** There are two good indices in the array:
- Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in non-decreasing order.
- Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in non-decreasing order.
Note that the index 4 is not good because [4,1] is not non-decreasing.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var goodIndices = function(nums, k) {
    const n = nums.length;

    let left = new Array(n).fill(1);
    let right = new Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        if (nums[i] <= nums[i - 1]) {
            left[i] = left[i - 1] + 1;
        }
    }
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] <= nums[i + 1]) {
            right[i] = right[i + 1] + 1;
        }
    }

    let result = [];
    for (let i = k; i < n - k; i++) {
        if (left[i - 1] >= k && right[i + 1] >= k) {
            result.push(i);
        }
    }

    return result;
};
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
- [1397. Find All Good Strings](../../1001-1500/1397-find-all-good-strings/)
- [2100. Find Good Days to Rob the Bank](../../2001-2500/2100-find-good-days-to-rob-the-bank/)
- [2732. Find a Good Subset of the Matrix](../../2501-3000/2732-find-a-good-subset-of-the-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-good-indices/)
