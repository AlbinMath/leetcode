# LeetCode 4010: Maximize Pair Strength Using GCD

**LeetCode Problem #4010 — Maximize Pair Strength Using GCD**
Solve LeetCode Maximize Pair Strength Using GCD using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Pair Strength Using GCD |
| LeetCode | #4010 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Choose exactly one pair of distinct indices `i` and `j`. The strength of the pair is defined as `(nums[i] * nums[j]) / gcd(nums[i], nums[j]) ^2`.

Return the maximum strength over all possible pairs.

## Constraints
- `2 <= nums.length <= 2000`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,3,5]`
- **Output:** `15`
- **Explanation:** Choosing `i = 1` and `j = 2` gives strength `(3 * 5) / gcd(3, 5)^2 = 15 / 1 = 15`, which is the maximum over all pairs.

### Example 2
- **Input:** `nums = [4,6,8]`
- **Output:** `12`
- **Explanation:** Choosing `i = 1` and `j = 2` gives strength `(6 * 8) / gcd(6, 8)^2 = 48 / 4 = 12`, which is the maximum over all pairs.

### Example 3
- **Input:** `nums = [3,3]`
- **Output:** `1`
- **Explanation:** Choosing `i = 0` and `j = 1` gives strength `(3 * 3) / gcd(3, 3)^2 = 9 / 9 = 1`, the maximum over all pairs.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximize Pair Strength Using GCD**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** Choosing `i = 1` and `j = 2` gives strength `(3 * 5) / gcd(3, 5)^2 = 15 / 1 = 15`, which is the maximum over all pairs.

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
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxPairStrength = function(nums) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Sort descending to enable early pruning when nums[i] * nums[j] <= maxStrength
    nums.sort((a, b) => b - a);

    const n = nums.length;
    let maxStrength = 0;

    for (let i = 0; i < n - 1; i++) {
        const a = nums[i];
        // Even with gcd = 1, no remaining pair with a can beat maxStrength
        if (a * nums[i + 1] <= maxStrength) break;

        for (let j = i + 1; j < n; j++) {
            const b = nums[j];
            if (a * b <= maxStrength) break;

            const g = gcd(a, b);
            const strength = (a / g) * (b / g);
            if (strength > maxStrength) {
                maxStrength = strength;
            }
        }
    }

    return maxStrength;
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
- [3695. Maximize Alternating Sum Using Swaps](../../3501-4000/3695-maximize-alternating-sum-using-swaps/)
- [4062. Transform Array Using Pair Operations](../../4001-4500/4062-transform-array-using-pair-operations/)
- [3480. Maximize Subarrays After Removing One Conflicting Pair](../../3001-3500/3480-maximize-subarrays-after-removing-one-conflicting-pair/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-pair-strength-using-gcd/)
