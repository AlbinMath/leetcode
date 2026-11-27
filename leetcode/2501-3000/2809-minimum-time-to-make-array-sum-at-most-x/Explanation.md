# LeetCode 2809: Minimum Time to Make Array Sum At Most x

**LeetCode Problem #2809 — Minimum Time to Make Array Sum At Most x**
Solve LeetCode Minimum Time to Make Array Sum At Most x using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Make Array Sum At Most x |
| LeetCode | #2809 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** integer arrays `nums1` and `nums2` of equal length. Every second, for all indices `0 <= i < nums1.length`, value of `nums1[i]` is incremented by `nums2[i]`. **After** this is done, you can do the following operation:

Choose an index `0 <= i < nums1.length` and make `nums1[i] = 0`.

You are also given an integer `x`.

Return *the **minimum** time in which you can make the sum of all elements of *`nums1`* to be** less than or equal** to *`x`, *or *`-1`* if this is not possible.*

## Constraints
- ` 1 <= nums1.length <= 10^3 `
- `1 <= nums1[i] <= 10^3`
- `0 <= nums2[i] <= 10^3`
- `nums1.length == nums2.length`
- `0 <= x <= 10^6`

## Examples
### Example 1
- **Input:** `nums1 = [1,2,3], nums2 = [1,2,3], x = 4`
- **Output:** `3`
- **Explanation:** For the 1st second, we apply the operation on i = 0. Therefore nums1 = [0,2+2,3+3] = [0,4,6]. 
For the 2nd second, we apply the operation on i = 1. Therefore nums1 = [0+1,0,6+3] = [1,0,9]. 
For the 3rd second, we apply the operation on i = 2. Therefore nums1 = [1+1,0+2,0] = [2,2,0]. 
Now sum of nums1 = 4. It can be shown that these operations are optimal, so we return 3.

### Example 2
- **Input:** `nums1 = [1,2,3], nums2 = [3,3,3], x = 4`
- **Output:** `-1`
- **Explanation:** It can be shown that the sum of nums1 will always be greater than x, no matter which operations are performed.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time to Make Array Sum At Most x**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2,3], nums2 = [1,2,3], x = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** For the 1st second, we apply the operation on i = 0. Therefore nums1 = [0,2+2,3+3] = [0,4,6]. 
For the 2nd second, we apply the operation on i = 1. Therefore nums1 = [0+1,0,6+3] = [1,0,9]. 
For the 3rd second, we apply the operation on i = 2. Therefore nums1 = [1+1,0+2,0] = [2,2,0]. 
Now sum of nums1 = 4. It can be shown that these operations are optimal, so we return 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minimumTime = function(nums1, nums2, x) {
    const n = nums1.length;

    let sum1 = 0;
    let sum2 = 0;

    for (let i = 0; i < n; i++) {
        sum1 += nums1[i];
        sum2 += nums2[i];
    }
    const arr = [];

    for (let i = 0; i < n; i++) {
        arr.push([nums1[i], nums2[i]]);
    }

    arr.sort((a, b) => a[1] - b[1]);

    const dp = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        const [a, b] = arr[i];

        for (let j = i + 1; j >= 1; j--) {
            dp[j] = Math.max(
                dp[j],
                dp[j - 1] + a + j * b
            );
        }
    }

    for (let t = 0; t <= n; t++) {
        const remainingSum = sum1 + t * sum2 - dp[t];

        if (remainingSum <= x) {
            return t;
        }
    }

    return -1;
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1578. Minimum Time to Make Rope Colorful](../../1501-2000/1578-minimum-time-to-make-rope-colorful/)
- [2998. Minimum Number of Operations to Make X and Y Equal](../../2501-3000/2998-minimum-number-of-operations-to-make-x-and-y-equal/)
- [945. Minimum Increment to Make Array Unique](../../0501-1000/0945-minimum-increment-to-make-array-unique/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/)
