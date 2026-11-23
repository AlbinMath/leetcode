# LeetCode 3326: Minimum Division Operations to Make Array Non Decreasing

**LeetCode Problem #3326 — Minimum Division Operations to Make Array Non Decreasing**
Solve LeetCode Minimum Division Operations to Make Array Non Decreasing using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Division Operations to Make Array Non Decreasing |
| LeetCode | #3326 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Any **positive** divisor of a natural number `x` that is **strictly less** than `x` is called a **proper divisor** of `x`. For example, 2 is a *proper divisor* of 4, while 6 is not a *proper divisor* of 6.

You are allowed to perform an **operation** any number of times on `nums`, where in each **operation** you select any *one* element from `nums` and divide it by its **greatest** **proper divisor**.

Return the **minimum** number of **operations** required to make the array **non-decreasing**.

If it is **not** possible to make the array *non-decreasing* using any number of operations, return `-1`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [25,7]`
- **Output:** `1`
- **Explanation:** Using a single operation, 25 gets divided by 5 and `nums` becomes `[5, 7]`.

### Example 2
- **Input:** `nums = [7,7,6]`
- **Output:** `-1`

### Example 3
- **Input:** `nums = [1,1,1,1]`
- **Output:** `0`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Division Operations to Make Array Non Decreasing**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [25,7]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Using a single operation, 25 gets divided by 5 and `nums` becomes `[5, 7]`.

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
var minOperations = function(nums) {
    // Helper to find the smallest prime factor of x (for x > 1)
    const getSmallestPrimeFactor = (x) => {
        if (x % 2 === 0) return 2;
        for (let d = 3; d * d <= x; d += 2) {
            if (x % d === 0) return d;
        }
        return x; // x is prime
    };

    let operations = 0;

    // Traverse from right to left so each element is bounded by its right neighbor
    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] > nums[i + 1]) {
            nums[i] = getSmallestPrimeFactor(nums[i]);
            operations++;

            // If even its smallest prime factor is greater than nums[i + 1], it's impossible
            if (nums[i] > nums[i + 1]) {
                return -1;
            }
        }
    }

    return operations;
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
- [1827. Minimum Operations to Make the Array Increasing](../../1501-2000/1938-minimum-operations-to-make-the-array-increasing/)
- [2009. Minimum Number of Operations to Make Array Continuous](../../2001-2500/2119-minimum-number-of-operations-to-make-array-continuous/)
- [2170. Minimum Operations to Make the Array Alternating](../../2001-2500/2289-minimum-operations-to-make-the-array-alternating/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/)
