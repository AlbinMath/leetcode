# LeetCode 2333: Minimum Sum of Squared Difference

**LeetCode Problem #2333 — Minimum Sum of Squared Difference**
Solve LeetCode Minimum Sum of Squared Difference using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Sum of Squared Difference |
| LeetCode | #2333 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive **0-indexed** integer arrays `nums1` and `nums2`, both of length `n`.

The **sum of squared difference** of arrays `nums1` and `nums2` is defined as the **sum** of `(nums1[i] - nums2[i])^2` for each `0 <= i < n`.

You are also given two positive integers `k1` and `k2`. You can modify any of the elements of `nums1` by `+1` or `-1` at most `k1` times. Similarly, you can modify any of the elements of `nums2` by `+1` or `-1` at most `k2` times.

Return *the minimum **sum of squared difference** after modifying array *`nums1`* at most *`k1`* times and modifying array *`nums2`* at most *`k2`* times*.

**Note**: You are allowed to modify the array elements to become **negative** integers.

## Constraints
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^5`
- `0 <= k1, k2 <= 10^9`

## Examples
### Example 1
- **Input:** `nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0`
- **Output:** `579`
- **Explanation:** The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
The sum of square difference will be: (1 - 2)^2 + (2 - 10)^2 + (3 - 20)^2 + (4 - 19)^2 = 579.

### Example 2
- **Input:** `nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1`
- **Output:** `43`
- **Explanation:** One way to obtain the minimum sum of square difference is: 
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be: 
(2 - 5)^2 + (4 - 8)^2 + (10 - 7)^2 + (12 - 9)^2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Sum of Squared Difference**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `579`.
4. **Verification:** The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
The sum of square difference will be: (1 - 2)^2 + (2 - 10)^2 + (3 - 20)^2 + (4 - 19)^2 = 579.

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
var minSumSquareDiff = function(nums1, nums2, k1, k2) {
    const n = nums1.length;
    let k = k1 + k2;
    const diff = new Array(n);

    let maxDiff = 0;

    for (let i = 0; i < n; i++) {
        diff[i] = Math.abs(nums1[i] - nums2[i]);
        maxDiff = Math.max(maxDiff, diff[i]);
    }

    // No difference can be reduced below zero
    if (k >= diff.reduce((sum, d) => sum + d, 0)) {
        return 0;
    }

    // Count the number of differences at each level
    const count = new Array(maxDiff + 1).fill(0);

    for (const d of diff) {
        count[d]++;
    }

    // Reduce the largest differences first
    for (let d = maxDiff; d > 0 && k > 0; d--) {
        const canReduce = Math.min(k, count[d]);

        count[d] -= canReduce;
        count[d - 1] += canReduce;
        k -= canReduce;
    }

    // Calculate the final sum of squared differences
    let result = 0;

    for (let d = 0; d <= maxDiff; d++) {
        result += d * d * count[d];
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
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [209. Minimum Size Subarray Sum](../../0001-0500/0209-minimum-size-subarray-sum/)
- [599. Minimum Index Sum of Two Lists](../../0501-1000/0599-minimum-index-sum-of-two-lists/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-sum-of-squared-difference/)
