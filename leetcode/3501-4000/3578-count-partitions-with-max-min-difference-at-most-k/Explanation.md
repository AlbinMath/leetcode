# LeetCode 3578: Count Partitions With Max-Min Difference at Most K

**LeetCode Problem #3578 — Count Partitions With Max-Min Difference at Most K**
Solve LeetCode Count Partitions With Max-Min Difference at Most K using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Partitions With Max-Min Difference at Most K |
| LeetCode | #3578 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`. Your task is to partition `nums` into one or more **non-empty** contiguous segments such that in each segment, the difference between its **maximum** and **minimum** elements is **at most** `k`.

Return the total number of ways to partition `nums` under this condition.

Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `2 <= nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [9,4,1,3,7], k = 4`
- **Output:** `6`
- **Explanation:** There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most `k = 4`: 

 
 `[[9], [4], [1], [3], [7]]` 
 `[[9], [4], [1], [3, 7]]` 
 `[[9], [4], [1, 3], [7]]` 
 `[[9], [4, 1], [3], [7]]` 
 `[[9], [4, 1], [3, 7]]` 
 `[[9], [4, 1, 3], [7]]`

### Example 2
- **Input:** `nums = [3,3,4], k = 0`
- **Output:** `2`
- **Explanation:** There are 2 valid partitions that satisfy the given conditions: 

 
 `[[3], [3], [4]]` 
 `[[3, 3], [4]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Partitions With Max-Min Difference at Most K**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [9,4,1,3,7], k = 4`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most `k = 4`: 

 
 `[[9], [4], [1], [3], [7]]` 
 `[[9], [4], [1], [3, 7]]` 
 `[[9], [4], [1, 3], [7]]` 
 `[[9], [4, 1], [3], [7]]` 
 `[[9], [4, 1], [3, 7]]` 
 `[[9], [4, 1, 3], [7]]`

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
 * @param {number} k
 * @return {number}
 */
var countPartitions = function (nums, k) {
    const MOD = 1000000007;
    const n = nums.length;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;

    const maxQ = new Array(n), minQ = new Array(n);
    let maxH = 0, maxT = 0, minH = 0, minT = 0;
    let l = 0;      // smallest valid start index (0-indexed into nums)
    let sum = 1;    // sum of dp[l..i-1], starts as dp[0]

    for (let i = 1; i <= n; i++) {
        const r = i - 1;
        while (maxH < maxT && nums[maxQ[maxT - 1]] <= nums[r]) maxT--;
        maxQ[maxT++] = r;
        while (minH < minT && nums[minQ[minT - 1]] >= nums[r]) minT--;
        minQ[minT++] = r;

        while (nums[maxQ[maxH]] - nums[minQ[minH]] > k) {
            sum = (sum - dp[l] + MOD) % MOD;
            l++;
            if (maxQ[maxH] < l) maxH++;
            if (minQ[minH] < l) minH++;
        }

        dp[i] = sum;
        sum = (sum + dp[i]) % MOD;
    }
    return dp[n];
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
- [2962. Count Subarrays Where Max Element Appears at Least K Times](../../2501-3000/2962-count-subarrays-where-max-element-appears-at-least-k-times/)
- [2006. Count Number of Pairs With Absolute Difference K](../../2001-2500/2006-count-number-of-pairs-with-absolute-difference-k/)
- [3432. Count Partitions with Even Sum Difference](../../3001-3500/3432-count-partitions-with-even-sum-difference/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/)
