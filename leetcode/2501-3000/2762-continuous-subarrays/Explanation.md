# LeetCode 2762: Continuous Subarrays

**LeetCode Problem #2762 — Continuous Subarrays**
Solve LeetCode Continuous Subarrays using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Continuous Subarrays |
| LeetCode | #2762 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. A subarray of `nums` is called **continuous** if:

Let `i`, `i + 1`, ..., `j`_ be the indices in the subarray. Then, for each pair of indices `i <= i_1, i_2 <= j`, ` 0 <= |nums[i_1] - nums[i_2]| <= 2`.

Return *the total number of **continuous** subarrays.*

A subarray is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [5,4,2,4]`
- **Output:** `8`
- **Explanation:** Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
There are no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.

### Example 2
- **Input:** `nums = [1,2,3]`
- **Output:** `6`
- **Explanation:** Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Continuous Subarrays**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,4,2,4]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
There are no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var continuousSubarrays = function (nums) {
    const n = nums.length;
    const maxQ = new Array(n), minQ = new Array(n);
    let maxH = 0, maxT = 0, minH = 0, minT = 0;
    let l = 0, ans = 0;

    for (let r = 0; r < n; r++) {
        while (maxH < maxT && nums[maxQ[maxT - 1]] <= nums[r]) maxT--;
        maxQ[maxT++] = r;
        while (minH < minT && nums[minQ[minT - 1]] >= nums[r]) minT--;
        minQ[minT++] = r;

        while (nums[maxQ[maxH]] - nums[minQ[minH]] > 2) {
            l++;
            if (maxQ[maxH] < l) maxH++;
            if (minQ[minH] < l) minH++;
        }
        ans += r - l + 1;
    }
    return ans;
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [581. Shortest Unsorted Continuous Subarray](../../0501-1000/0581-shortest-unsorted-continuous-subarray/)
- [674. Longest Continuous Increasing Subsequence](../../0501-1000/0674-longest-continuous-increasing-subsequence/)
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1001-1500/1438-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/continuous-subarrays/)
