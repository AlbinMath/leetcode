# LeetCode 2874: Maximum Value of an Ordered Triplet II

**LeetCode Problem #2874 — Maximum Value of an Ordered Triplet II**
Solve LeetCode Maximum Value of an Ordered Triplet II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Value of an Ordered Triplet II |
| LeetCode | #2874 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`.

Return ***the maximum value over all triplets of indices*** `(i, j, k)` *such that* `i < j < k`*. *If all such triplets have a negative value, return `0`.

The **value of a triplet of indices** `(i, j, k)` is equal to `(nums[i] - nums[j]) * nums[k]`.

## Constraints
- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [12,6,1,2,7]`
- **Output:** `77`
- **Explanation:** The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
It can be shown that there are no ordered triplets of indices with a value greater than 77.

### Example 2
- **Input:** `nums = [1,10,3,4,19]`
- **Output:** `133`
- **Explanation:** The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
It can be shown that there are no ordered triplets of indices with a value greater than 133.

### Example 3
- **Input:** `nums = [1,2,3]`
- **Output:** `0`
- **Explanation:** The only ordered triplet of indices (0, 1, 2) has a negative value of (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Value of an Ordered Triplet II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [12,6,1,2,7]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `77`.
4. **Verification:** The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
It can be shown that there are no ordered triplets of indices with a value greater than 77.

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
var maximumTripletValue = function(nums) {
    let leftMax = nums[0];
    let maxDiff = 0;
    let ans = 0;

    for (let k = 1; k < nums.length; k++) {
        ans = Math.max(ans, maxDiff * nums[k]);
        maxDiff = Math.max(maxDiff, leftMax - nums[k]);
        leftMax = Math.max(leftMax, nums[k]);
    }

    return ans;
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
- [2873. Maximum Value of an Ordered Triplet I](../../2501-3000/2873-maximum-value-of-an-ordered-triplet-i/)
- [1131. Maximum of Absolute Value Expression](../../1001-1500/1131-maximum-of-absolute-value-expression/)
- [1695. Maximum Erasure Value](../../1501-2000/1695-maximum-erasure-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/)
