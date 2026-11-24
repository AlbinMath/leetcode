# LeetCode 3583: Count Special Triplets

**LeetCode Problem #3583 — Count Special Triplets**
Solve LeetCode Count Special Triplets using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Special Triplets |
| LeetCode | #3583 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A **special triplet** is defined as a triplet of indices `(i, j, k)` such that:

`0 <= i < j < k < n`, where `n = nums.length` 
 `nums[i] == nums[j] * 2` 
 `nums[k] == nums[j] * 2`

Return the total number of **special triplets** in the array.

Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `3 <= n == nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [6,3,6]`
- **Output:** `1`
- **Explanation:** The only special triplet is `(i, j, k) = (0, 1, 2)`, where: 

 
 `nums[0] = 6`, `nums[1] = 3`, `nums[2] = 6` 
 `nums[0] = nums[1] * 2 = 3 * 2 = 6` 
 `nums[2] = nums[1] * 2 = 3 * 2 = 6`

### Example 2
- **Input:** `nums = [0,1,0,0]`
- **Output:** `1`
- **Explanation:** The only special triplet is `(i, j, k) = (0, 2, 3)`, where: 

 
 `nums[0] = 0`, `nums[2] = 0`, `nums[3] = 0` 
 `nums[0] = nums[2] * 2 = 0 * 2 = 0` 
 `nums[3] = nums[2] * 2 = 0 * 2 = 0`

### Example 3
- **Input:** `nums = [8,4,2,8,4]`
- **Output:** `2`
- **Explanation:** There are exactly two special triplets: 

 
 `(i, j, k) = (0, 1, 3)`

 
 `nums[0] = 8`, `nums[1] = 4`, `nums[3] = 8` 
 `nums[0] = nums[1] * 2 = 4 * 2 = 8` 
 `nums[3] = nums[1] * 2 = 4 * 2 = 8` 
 
 
 `(i, j, k) = (1, 2, 4)`
 
 `nums[1] = 4`, `nums[2] = 2`, `nums[4] = 4` 
 `nums[1] = nums[2] * 2 = 2 * 2 = 4` 
 `nums[4] = nums[2] * 2 = 2 * 2 = 4`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Special Triplets**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [6,3,6]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The only special triplet is `(i, j, k) = (0, 1, 2)`, where: 

 
 `nums[0] = 6`, `nums[1] = 3`, `nums[2] = 6` 
 `nums[0] = nums[1] * 2 = 3 * 2 = 6` 
 `nums[2] = nums[1] * 2 = 3 * 2 = 6`

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
var specialTriplets = function(nums) {
    const MOD = 1000000007;
    const MAX = 200001;

    let left = Array(MAX).fill(0);
    let right = Array(MAX).fill(0);

    // Count all elements initially in right
    for (const num of nums) {
        right[num]++;
    }

    let ans = 0;

    for (let j = 0; j < nums.length; j++) {
        let x = nums[j];
        let target = x * 2;

        // Remove current element from right
        right[x]--;

        // Count valid pairs on both sides
        ans = (ans + left[target] * right[target]) % MOD;

        // Add current element to left
        left[x]++;
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
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1501-2000/1553-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [1534. Count Good Triplets](../../1501-2000/1656-count-good-triplets/)
- [2179. Count Good Triplets in an Array](../../2001-2500/2280-count-good-triplets-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-special-triplets/)
