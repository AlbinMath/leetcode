# LeetCode 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

**LeetCode Problem #1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit**
Solve LeetCode Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit |
| LeetCode | #1438 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums` and an integer `limit`.

Return the size of the **longest non-empty subarray** such that the **absolute** difference between **every pair of elements** in this **subarray** is **less than or equal** to `limit`*.*

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [8,2,4,7], limit = 4`
- **Output:** `2`
- **Explanation:** Checking every subarray, where the absolute difference is taken over all pairs of its elements: 
`[8]` with maximum absolute diff `|8-8| = 0 <= 4`. 
`[8,2]` with maximum absolute diff `|8-2| = 6 > 4`. 
`[8,2,4]` with maximum absolute diff `|8-2| = 6 > 4`. 
`[8,2,4,7]` with maximum absolute diff `|8-2| = 6 > 4`. 
`[2]` with maximum absolute diff `|2-2| = 0 <= 4`. 
`[2,4]` with maximum absolute diff `|4-2| = 2 <= 4`. 
`[2,4,7]` with maximum absolute diff `|7-2| = 5 > 4`. Note that the pair `(2, 7)` is not adjacent, but it is still compared. 
`[4]` with maximum absolute diff `|4-4| = 0 <= 4`. 
`[4,7]` with maximum absolute diff `|7-4| = 3 <= 4`. 
`[7]` with maximum absolute diff `|7-7| = 0 <= 4`. 
Therefore, the size of the longest subarray is 2.

### Example 2
- **Input:** `nums = [10,1,2,4,7,2], limit = 5`
- **Output:** `4`
- **Explanation:** The subarray `[2,4,7,2]` is valid because every pair of its elements differs by at most `5`, the largest being `|7-2| = 5`. 

 It cannot be extended to the left, since `[1,2,4,7,2]` contains the pair `(1, 7)` with `|7-1| = 6 > 5`. Therefore, the size of the longest subarray is 4.

### Example 3
- **Input:** `nums = [4,2,2,2,4,4,2,2], limit = 0`
- **Output:** `3`
- **Explanation:** Since `limit = 0`, every pair of elements in the subarray must be equal, so only runs of identical values qualify. 

 The longest such run is `[2,2,2]`, of size 3.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [8,2,4,7], limit = 4`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Checking every subarray, where the absolute difference is taken over all pairs of its elements: 
`[8]` with maximum absolute diff `|8-8| = 0 <= 4`. 
`[8,2]` with maximum absolute diff `|8-2| = 6 > 4`. 
`[8,2,4]` with maximum absolute diff `|8-2| = 6 > 4`. 
`[8,2,4,7]` with maximum absolute diff `|8-2| = 6 > 4`. 
`[2]` with maximum absolute diff `|2-2| = 0 <= 4`. 
`[2,4]` with maximum absolute diff `|4-2| = 2 <= 4`. 
`[2,4,7]` with maximum absolute diff `|7-2| = 5 > 4`. Note that the pair `(2, 7)` is not adjacent, but it is still compared. 
`[4]` with maximum absolute diff `|4-4| = 0 <= 4`. 
`[4,7]` with maximum absolute diff `|7-4| = 3 <= 4`. 
`[7]` with maximum absolute diff `|7-7| = 0 <= 4`. 
Therefore, the size of the longest subarray is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number}
 */
var longestSubarray = function (nums, limit) {
    const n = nums.length;
    const maxQ = new Array(n), minQ = new Array(n);
    let maxH = 0, maxT = 0, minH = 0, minT = 0;
    let l = 0, ans = 0;

    for (let r = 0; r < n; r++) {
        while (maxH < maxT && nums[maxQ[maxT - 1]] <= nums[r]) maxT--;
        maxQ[maxT++] = r;
        while (minH < minT && nums[minQ[minT - 1]] >= nums[r]) minT--;
        minQ[minT++] = r;

        while (nums[maxQ[maxH]] - nums[minQ[minH]] > limit) {
            l++;
            if (maxQ[maxH] < l) maxH++;
            if (minQ[minH] < l) minH++;
        }
        ans = Math.max(ans, r - l + 1);
    }
    return ans;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2311. Longest Binary Subsequence Less Than or Equal to K](../../2001-2500/2311-longest-binary-subsequence-less-than-or-equal-to-k/)
- [713. Subarray Product Less Than K](../../0501-1000/0713-subarray-product-less-than-k/)
- [2831. Find the Longest Equal Subarray](../../2501-3000/2831-find-the-longest-equal-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
