# LeetCode 3117: Minimum Sum of Values by Dividing Array

**LeetCode Problem #3117 — Minimum Sum of Values by Dividing Array**
Solve LeetCode Minimum Sum of Values by Dividing Array using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Sum of Values by Dividing Array |
| LeetCode | #3117 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two arrays `nums` and `andValues` of length `n` and `m` respectively.

The **value** of an array is equal to the **last** element of that array.

You have to divide `nums` into `m` **disjoint contiguous** subarrays such that for the `i^th` subarray `[l_i, r_i]`, the bitwise `AND` of the subarray elements is equal to `andValues[i]`, in other words, `nums[l_i] & nums[l_i + 1] & ... & nums[r_i] == andValues[i]` for all `1 <= i <= m`, where `&` represents the bitwise `AND` operator.

Return *the **minimum** possible sum of the **values** of the *`m`* subarrays *`nums`* is divided into*. *If it is not possible to divide *`nums`* into *`m`* subarrays satisfying these conditions, return* `-1`.

## Constraints
- `1 <= n == nums.length <= 10^4`
- `1 <= m == andValues.length <= min(n, 10)`
- `1 <= nums[i] < 10^5`
- `0 <= andValues[j] < 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,4,3,3,2], andValues = [0,3,3,2]`
- **Output:** `12`
- **Explanation:** The only possible way to divide `nums` is: 

 
 `[1,4]` as `1 & 4 == 0`. 
 `[3]` as the bitwise `AND` of a single element subarray is that element itself. 
 `[3]` as the bitwise `AND` of a single element subarray is that element itself. 
 `[2]` as the bitwise `AND` of a single element subarray is that element itself. 
 

 The sum of the values for these subarrays is `4 + 3 + 3 + 2 = 12`.

### Example 2
- **Input:** `nums = [2,3,5,7,7,7,5], andValues = [0,7,5]`
- **Output:** `17`
- **Explanation:** There are three ways to divide `nums`: 

 
 `[[2,3,5],[7,7,7],[5]]` with the sum of the values `5 + 7 + 5 == 17`. 
 `[[2,3,5,7],[7,7],[5]]` with the sum of the values `7 + 7 + 5 == 19`. 
 `[[2,3,5,7,7],[7],[5]]` with the sum of the values `7 + 7 + 5 == 19`. 
 

 The minimum possible sum of the values is `17`.

### Example 3
- **Input:** `nums = [1,2,3,4], andValues = [2]`
- **Output:** `-1`
- **Explanation:** The bitwise `AND` of the entire array `nums` is `0`. As there is no possible way to divide `nums` into a single subarray to have the bitwise `AND` of elements `2`, return `-1`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Sum of Values by Dividing Array**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,3,3,2], andValues = [0,3,3,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** The only possible way to divide `nums` is: 

 
 `[1,4]` as `1 & 4 == 0`. 
 `[3]` as the bitwise `AND` of a single element subarray is that element itself. 
 `[3]` as the bitwise `AND` of a single element subarray is that element itself. 
 `[2]` as the bitwise `AND` of a single element subarray is that element itself. 
 

 The sum of the values for these subarrays is `4 + 3 + 3 + 2 = 12`.

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
 * @param {number[]} andValues
 * @return {number}
 */
var minimumValueSum = function (nums, andValues) {
    const n = nums.length, m = andValues.length;
    let prev = new Array(n + 1).fill(Infinity);
    prev[0] = 0; // zero subarrays cover zero elements

    for (let j = 1; j <= m; j++) {
        const target = andValues[j - 1];
        const cur = new Array(n + 1).fill(Infinity);
        let groups = []; // [andValue, minPrev], ordered by start index

        for (let i = 1; i <= n; i++) {
            const x = nums[i - 1];
            const next = [];
            const push = (a, b) => {
                const last = next[next.length - 1];
                if (last && last[0] === a) {
                    if (b < last[1]) last[1] = b;
                } else {
                    next.push([a, b]);
                }
            };
            for (const [a, b] of groups) push(a & x, b);
            push(x, prev[i - 1]); // new subarray starting at index i-1
            groups = next;

            for (const [a, b] of groups) {
                if (a === target && b < Infinity) {
                    cur[i] = b + x;
                    break;
                }
            }
        }
        prev = cur;
    }
    return prev[n] === Infinity ? -1 : prev[n];
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
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../../0001-0500/0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/)
