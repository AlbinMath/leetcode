# LeetCode 3605: Minimum Stability Factor of Array

**LeetCode Problem #3605 — Minimum Stability Factor of Array**
Solve LeetCode Minimum Stability Factor of Array using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Stability Factor of Array |
| LeetCode | #3605 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `maxC`.

A ** subarray ** is called **stable** if the *highest common factor (HCF)* of all its elements is **greater than or equal to** 2.

The **stability factor** of an array is defined as the length of its **longest** stable subarray.

You may modify **at most** `maxC` elements of the array to any integer.

Return the **minimum** possible stability factor of the array after at most `maxC` modifications. If no stable subarray remains, return 0.

**Note:**

The **highest common factor (HCF)** of an array is the largest integer that evenly divides all the array elements. 
 A **subarray** of length 1 is stable if its only element is greater than or equal to 2, since `HCF([x]) = x`.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= maxC <= n`

## Examples
### Example 1
- **Input:** `nums = [3,5,10], maxC = 1`
- **Output:** `1`
- **Explanation:** The stable subarray `[5, 10]` has `HCF = 5`, which has a stability factor of 2. 
 Since `maxC = 1`, one optimal strategy is to change `nums[1]` to `7`, resulting in `nums = [3, 7, 10]`. 
 Now, no subarray of length greater than 1 has `HCF >= 2`. Thus, the minimum possible stability factor is 1.

### Example 2
- **Input:** `nums = [2,6,8], maxC = 2`
- **Output:** `1`
- **Explanation:** The subarray `[2, 6, 8]` has `HCF = 2`, which has a stability factor of 3. 
 Since `maxC = 2`, one optimal strategy is to change `nums[1]` to 3 and `nums[2]` to 5, resulting in `nums = [2, 3, 5]`. 
 Now, no subarray of length greater than 1 has `HCF >= 2`. Thus, the minimum possible stability factor is 1.

### Example 3
- **Input:** `nums = [2,4,9,6], maxC = 1`
- **Output:** `2`
- **Explanation:** The stable subarrays are:
 
 `[2, 4]` with `HCF = 2` and stability factor of 2. 
 `[9, 6]` with `HCF = 3` and stability factor of 2. 
 
 
 Since `maxC = 1`, the stability factor of 2 cannot be reduced due to two separate stable subarrays. Thus, the minimum possible stability factor is 2.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Minimum Stability Factor of Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,5,10], maxC = 1`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The stable subarray `[5, 10]` has `HCF = 5`, which has a stability factor of 2. 
 Since `maxC = 1`, one optimal strategy is to change `nums[1]` to `7`, resulting in `nums = [3, 7, 10]`. 
 Now, no subarray of length greater than 1 has `HCF >= 2`. Thus, the minimum possible stability factor is 1.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @param {number} maxC
 * @return {number}
 */
var minStable = function(nums, maxC) {
    const n = nums.length;

    // Edge case: can we eliminate ALL elements >= 2 (stability factor = 0)?
    let countGe2 = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] >= 2) countGe2++;
    }
    if (countGe2 <= maxC) return 0;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Build Sparse Table for O(1) range GCD queries
    const LOG = 32 - Math.clz32(n);
    const st = Array.from({ length: LOG }, () => new Int32Array(n));
    st[0].set(nums);

    for (let k = 1; k < LOG; k++) {
        const half = 1 << (k - 1);
        const limit = n - (1 << k);
        for (let i = 0; i <= limit; i++) {
            st[k][i] = gcd(st[k - 1][i], st[k - 1][i + half]);
        }
    }

    const lg = new Int32Array(n + 1);
    for (let i = 2; i <= n; i++) {
        lg[i] = lg[i >> 1] + 1;
    }

    const queryGcd = (l, r) => {
        const k = lg[r - l + 1];
        return gcd(st[k][l], st[k][r - (1 << k) + 1]);
    };

    // Check if we can break all stable subarrays of length L + 1 using <= maxC changes
    const canAchieve = (L) => {
        const windowLen = L + 1;
        let ops = 0;
        let lastModified = -1;

        for (let i = windowLen - 1; i < n; i++) {
            // Skip if this window already includes a modified element (set to 1)
            if (lastModified >= i - windowLen + 1) continue;

            if (queryGcd(i - windowLen + 1, i) >= 2) {
                ops++;
                if (ops > maxC) return false;
                lastModified = i;
            }
        }
        return true;
    };

    // Binary search for the minimum achievable stability factor L in [1, n]
    let low = 1;
    let high = n;
    let ans = n;

    while (low <= high) {
        const mid = (low + high) >> 1;
        if (canAchieve(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return ans;
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
- [3334. Find the Maximum Factor Score of Array](../../3501-4000/3593-find-the-maximum-factor-score-of-array/)
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../../0001-0500/0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-stability-factor-of-array/)
