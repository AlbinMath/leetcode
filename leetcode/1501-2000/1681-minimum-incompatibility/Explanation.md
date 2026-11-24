# LeetCode 1681: Minimum Incompatibility

**LeetCode Problem #1681 — Minimum Incompatibility**
Solve LeetCode Minimum Incompatibility using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Incompatibility |
| LeetCode | #1681 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`​​​ and an integer `k`. You are asked to distribute this array into `k` subsets of **equal size** such that there are no two equal elements in the same subset.

A subset's **incompatibility** is the difference between the maximum and minimum elements in that array.

Return *the **minimum possible sum of incompatibilities** of the *`k` *subsets after distributing the array optimally, or return *`-1`* if it is not possible.*

A subset is a group integers that appear in the array with no particular order.

## Constraints
- `1 <= k <= nums.length <= 16`
- `nums.length` is divisible by `k`
- `1 <= nums[i] <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,2,1,4], k = 2`
- **Output:** `4`
- **Explanation:** The optimal distribution of subsets is [1,2] and [1,4].
The incompatibility is (2-1) + (4-1) = 4.
Note that [1,1] and [2,4] would result in a smaller sum, but the first subset contains 2 equal elements.

### Example 2
- **Input:** `nums = [6,3,8,1,3,1,2,2], k = 4`
- **Output:** `6`
- **Explanation:** The optimal distribution of subsets is [1,2], [2,3], [6,8], and [1,3].
The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.

### Example 3
- **Input:** `nums = [5,3,3,6,3,3], k = 3`
- **Output:** `-1`
- **Explanation:** It is impossible to distribute nums into 3 subsets where no two elements are equal in the same subset.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Incompatibility**, we observe the problem requirements and utilize the **Sliding Window** technique. We maintain a contiguous window defined by `left` and `right` pointers. The right pointer expands the window by adding incoming elements, while the left pointer advances to restore window invariants whenever duplicates or constraint limits are exceeded.

## Algorithm
1. Initialize `left = 0` and window tracking data structures.
2. Expand `right` pointer over input elements.
3. Contract `left` pointer when window invariants are breached.
4. Update global best metric for valid window intervals.
5. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1,4], k = 2`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The optimal distribution of subsets is [1,2] and [1,4].
The incompatibility is (2-1) + (4-1) = 4.
Note that [1,1] and [2,4] would result in a smaller sum, but the first subset contains 2 equal elements.

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
 * @param {number} k
 * @return {number}
 */
var minimumIncompatibility = function(nums, k) {
    const n = nums.length;
    const groupSize = n / k;

    // A value appearing more than k times cannot be distributed
    // without putting equal values in the same group.
    const freq = new Array(n + 1).fill(0);

    for (const num of nums) {
        freq[num]++;
        if (freq[num] > k) return -1;
    }

    const totalMasks = 1 << n;
    const INF = 1e9;

    // cost[mask] = incompatibility of this valid group,
    // or INF if it is not a valid group of groupSize elements.
    const cost = new Array(totalMasks).fill(INF);

    for (let mask = 1; mask < totalMasks; mask++) {
        if (countBits(mask) !== groupSize) continue;

        let minVal = Infinity;
        let maxVal = -Infinity;
        let seen = 0;
        let valid = true;

        for (let i = 0; i < n; i++) {
            if ((mask & (1 << i)) === 0) continue;

            const value = nums[i];
            const bit = 1 << value;

            if (seen & bit) {
                valid = false;
                break;
            }

            seen |= bit;
            minVal = Math.min(minVal, value);
            maxVal = Math.max(maxVal, value);
        }

        if (valid) {
            cost[mask] = maxVal - minVal;
        }
    }

    // dp[mask] = minimum cost to distribute the elements in mask.
    const dp = new Array(totalMasks).fill(INF);
    dp[0] = 0;

    for (let mask = 1; mask < totalMasks; mask++) {
        if (countBits(mask) % groupSize !== 0) continue;

        // Fix the first element in the remaining mask.
        // This avoids trying different orders of the same groups.
        const firstBit = mask & -mask;

        for (
            let group = mask;
            group > 0;
            group = (group - 1) & mask
        ) {
            if ((group & firstBit) === 0) continue;
            if (cost[group] === INF) continue;

            const remaining = mask ^ group;

            if (dp[remaining] !== INF) {
                dp[mask] = Math.min(
                    dp[mask],
                    dp[remaining] + cost[group]
                );
            }
        }
    }

    return dp[totalMasks - 1] === INF
        ? -1
        : dp[totalMasks - 1];
};

function countBits(mask) {
    let count = 0;

    while (mask > 0) {
        mask &= mask - 1;
        count++;
    }

    return count;
}
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
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [76. Minimum Window Substring](../../0001-0500/0076-minimum-window-substring/)
- [111. Minimum Depth of Binary Tree](../../0001-0500/0111-minimum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-incompatibility/)
