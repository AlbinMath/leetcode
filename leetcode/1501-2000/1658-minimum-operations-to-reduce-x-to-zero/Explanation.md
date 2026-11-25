# LeetCode 1658: Minimum Operations to Reduce X to Zero

**LeetCode Problem #1658 — Minimum Operations to Reduce X to Zero**
Solve LeetCode Minimum Operations to Reduce X to Zero using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Reduce X to Zero |
| LeetCode | #1658 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `x`. In one operation, you can either remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Note that this **modifies** the array for future operations.

Return *the **minimum number** of operations to reduce *`x` *to **exactly*** `0` *if it is possible**, otherwise, return *`-1`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`
- `1 <= x <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,1,4,2,3], x = 5`
- **Output:** `2`
- **Explanation:** The optimal solution is to remove the last two elements to reduce x to zero.

### Example 2
- **Input:** `nums = [5,6,7,8,9], x = 4`
- **Output:** `-1`

### Example 3
- **Input:** `nums = [3,2,20,1,1,3], x = 10`
- **Output:** `5`
- **Explanation:** The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
Instead of simulating removing elements from the edges, the problem can be reframed into an inverse problem: 
If we remove a prefix and a suffix that sum to `x`, then the remaining elements in the middle form a contiguous subarray whose sum is `total_sum - x`. To minimize the number of operations (number of elements removed), we need to **maximize the length of this middle subarray**.

1. The code calculates the `total` sum of the array. The `target` sum for the middle subarray is then `total - x`.
2. Edge Cases: 
   - If `target < 0`, it's impossible to reach `x` since all numbers are positive, so it returns `-1`.
   - If `target === 0`, it means the entire array sums to `x`, so all elements must be removed. It returns `nums.length`.
3. It uses a **Sliding Window** technique with two pointers (`left` and `right`) to find the longest contiguous subarray that sums exactly to `target`.
4. It iterates the `right` pointer across the array, adding `nums[right]` to a running `sum`.
5. If the `sum` exceeds the `target`, it shrinks the window from the left by subtracting `nums[left]` and incrementing `left` until the `sum` is less than or equal to `target`.
6. Whenever the `sum` exactly equals the `target`, it updates `maxLength` with the size of the current window (`right - left + 1`).
7. Finally, if a valid subarray was found (`maxLength !== -1`), the minimum operations will be the total number of elements minus the longest subarray length (`nums.length - maxLength`). Otherwise, it returns `-1`.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,4,2,3], x = 5`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The optimal solution is to remove the last two elements to reduce x to zero.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minOperations = function(nums, x) {
    // Total sum - x = sum of the subarray we want to KEEP
    const total = nums.reduce((sum, num) => sum + num, 0);
    const target = total - x;

    if (target < 0) return -1;
    if (target === 0) return nums.length;

    let left = 0;
    let sum = 0;
    let maxLength = -1;

    // Sliding window to find the longest subarray
    // whose sum is equal to target
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];

        while (sum > target && left <= right) {
            sum -= nums[left];
            left++;
        }

        if (sum === target) {
            maxLength = Math.max(maxLength, right - left + 1);
        }
    }

    return maxLength === -1 ? -1 : nums.length - maxLength;
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [1611. Minimum One Bit Operations to Make Integers Zero](../../1501-2000/1611-minimum-one-bit-operations-to-make-integers-zero/)
- [2749. Minimum Operations to Make the Integer Zero](../../2501-3000/2749-minimum-operations-to-make-the-integer-zero/)
- [3495. Minimum Operations to Make Array Elements Zero](../../3001-3500/3495-minimum-operations-to-make-array-elements-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)
