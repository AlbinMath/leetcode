# LeetCode 1879: Minimum XOR Sum of Two Arrays

**LeetCode Problem #1879 — Minimum XOR Sum of Two Arrays**
Solve LeetCode Minimum XOR Sum of Two Arrays using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum XOR Sum of Two Arrays |
| LeetCode | #1879 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2` of length `n`.

The **XOR sum** of the two integer arrays is `(nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1])` (**0-indexed**).

For example, the **XOR sum** of `[1,2,3]` and `[3,2,1]` is equal to `(1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4`.

Rearrange the elements of `nums2` such that the resulting **XOR sum** is minimized .

Return *the **XOR sum** after the rearrangement*.

## Constraints
- `n == nums1.length`
- `n == nums2.length`
- `1 <= n <= 14`
- `0 <= nums1[i], nums2[i] <= 10^7`

## Examples
### Example 1
- **Input:** `nums1 = [1,2], nums2 = [2,3]`
- **Output:** `2`

### Example 2
- **Input:** `nums1 = [1,0,3], nums2 = [5,3,4]`
- **Output:** `8`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum XOR Sum of Two Arrays**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2], nums2 = [2,3]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minimumXORSum = function(nums1, nums2) {
    const n = nums1.length;
    const totalMasks = 1 << n;
    const dp = new Array(totalMasks).fill(Infinity);

    dp[0] = 0;

    for (let mask = 0; mask < totalMasks; mask++) {
        if (dp[mask] === Infinity) continue;

        // Number of selected elements tells us the next index in nums1.
        const i = countBits(mask);

        if (i === n) continue;

        for (let j = 0; j < n; j++) {
            // Skip elements of nums2 that have already been used.
            if (mask & (1 << j)) continue;

            const nextMask = mask | (1 << j);
            const cost = nums1[i] ^ nums2[j];

            dp[nextMask] = Math.min(
                dp[nextMask],
                dp[mask] + cost
            );
        }
    }

    return dp[totalMasks - 1];

    function countBits(mask) {
        let count = 0;

        while (mask > 0) {
            mask &= mask - 1;
            count++;
        }

        return count;
    }
};
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [2918. Minimum Equal Sum of Two Arrays After Replacing Zeros](../../2501-3000/2918-minimum-equal-sum-of-two-arrays-after-replacing-zeros/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [599. Minimum Index Sum of Two Lists](../../0501-1000/0599-minimum-index-sum-of-two-lists/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/)
