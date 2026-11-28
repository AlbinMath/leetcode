# LeetCode 3854: Minimum Operations to Make Array Parity Alternating

**LeetCode Problem #3854 — Minimum Operations to Make Array Parity Alternating**
Solve LeetCode Minimum Operations to Make Array Parity Alternating using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make Array Parity Alternating |
| LeetCode | #3854 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

An array is called **parity alternating** if for every index `i` where `0 <= i < n - 1`, `nums[i]` and `nums[i + 1]` have different parity (one is even and the other is odd).

In one operation, you may choose any index `i` and either increase `nums[i]` by 1 or decrease `nums[i]` by 1.

Return an integer array `answer` of length 2 where:

`answer[0]` is the **minimum** number of operations required to make the array parity alternating. 
 `answer[1]` is the **minimum** possible value of `max(nums) - min(nums)` taken over all arrays that are parity alternating and can be obtained by performing **exactly** `answer[0]` operations.

An array of length 1 is considered parity alternating.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [-2,-3,1,4]`
- **Output:** `[2,6]`
- **Explanation:** Applying the following operations: 

 
 Increase `nums[2]` by 1, resulting in `nums = [-2, -3, 2, 4]`. 
 Decrease `nums[3]` by 1, resulting in `nums = [-2, -3, 2, 3]`. 
 

 The resulting array is parity alternating, and the value of `max(nums) - min(nums) = 3 - (-3) = 6` is the minimum possible among all parity alternating arrays obtainable using exactly 2 operations.

### Example 2
- **Input:** `nums = [0,2,-2]`
- **Output:** `[1,3]`
- **Explanation:** Applying the following operation: 

 
 Decrease `nums[1]` by 1, resulting in `nums = [0, 1, -2]`. 
 

 The resulting array is parity alternating, and the value of `max(nums) - min(nums) = 1 - (-2) = 3` is the minimum possible among all parity alternating arrays obtainable using exactly 1 operation.

### Example 3
- **Input:** `nums = [7]`
- **Output:** `[0,0]`
- **Explanation:** No operations are required. The array is already parity alternating, and the value of `max(nums) - min(nums) = 7 - 7 = 0`, which is the minimum possible.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Operations to Make Array Parity Alternating**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-2,-3,1,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,6]`.
4. **Verification:** Applying the following operations: 

 
 Increase `nums[2]` by 1, resulting in `nums = [-2, -3, 2, 4]`. 
 Decrease `nums[3]` by 1, resulting in `nums = [-2, -3, 2, 3]`. 
 

 The resulting array is parity alternating, and the value of `max(nums) - min(nums) = 3 - (-3) = 6` is the minimum possible among all parity alternating arrays obtainable using exactly 2 operations.

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
var makeParityAlternating = function(nums) {
    const n = nums.length;

    if (n === 1) return [0, 0];

    function getCost(startParity) {
        let cost = 0;

        for (let i = 0; i < n; i++) {
            const parity = ((nums[i] % 2) + 2) % 2;
            const required = (startParity + i) % 2;

            if (parity !== required) cost++;
        }

        return cost;
    }

    const costEvenStart = getCost(0);
    const costOddStart = getCost(1);
    const minOps = Math.min(costEvenStart, costOddStart);

    function getMinRange(startParity) {
        const candidates = [];

        for (let i = 0; i < n; i++) {
            const parity = ((nums[i] % 2) + 2) % 2;
            const required = (startParity + i) % 2;

            if (parity === required) {
                candidates.push([nums[i], i]);
            } else {
                candidates.push([nums[i] - 1, i]);
                candidates.push([nums[i] + 1, i]);
            }
        }

        candidates.sort((a, b) => a[0] - b[0]);

        const count = new Array(n).fill(0);
        let covered = 0;
        let left = 0;
        let minRange = Infinity;

        for (let right = 0; right < candidates.length; right++) {
            const index = candidates[right][1];

            if (count[index] === 0) covered++;
            count[index]++;

            while (covered === n) {
                minRange = Math.min(
                    minRange,
                    candidates[right][0] - candidates[left][0]
                );

                const leftIndex = candidates[left][1];
                count[leftIndex]--;

                if (count[leftIndex] === 0) covered--;

                left++;
            }
        }

        return minRange;
    }

    let minRange = Infinity;

    if (costEvenStart === minOps) {
        minRange = Math.min(minRange, getMinRange(0));
    }

    if (costOddStart === minOps) {
        minRange = Math.min(minRange, getMinRange(1));
    }

    return [minOps, minRange];
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
- [2170. Minimum Operations to Make the Array Alternating](../../2001-2500/2170-minimum-operations-to-make-the-array-alternating/)
- [3937. Minimum Operations to Make Array Modulo Alternating I](../../3501-4000/3937-minimum-operations-to-make-array-modulo-alternating-i/)
- [1551. Minimum Operations to Make Array Equal](../../1501-2000/1551-minimum-operations-to-make-array-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/)
