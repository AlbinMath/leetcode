# LeetCode 2444: Count Subarrays With Fixed Bounds

**LeetCode Problem #2444 — Count Subarrays With Fixed Bounds**
Solve LeetCode Count Subarrays With Fixed Bounds using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subarrays With Fixed Bounds |
| LeetCode | #2444 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and two integers `minK` and `maxK`.

A **fixed-bound subarray** of `nums` is a subarray that satisfies the following conditions:

The **minimum** value in the subarray is equal to `minK`. 
 The **maximum** value in the subarray is equal to `maxK`.

Return *the **number** of fixed-bound subarrays*.

A **subarray** is a **contiguous** part of an array.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i], minK, maxK <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,3,5,2,7,5], minK = 1, maxK = 5`
- **Output:** `2`
- **Explanation:** The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

### Example 2
- **Input:** `nums = [1,1,1,1], minK = 1, maxK = 1`
- **Output:** `10`
- **Explanation:** Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Subarrays With Fixed Bounds**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,5,2,7,5], minK = 1, maxK = 5`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

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
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function (nums, minK, maxK) {
    let bad = -1, lastMin = -1, lastMax = -1;
    let ans = 0;

    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        if (x < minK || x > maxK) bad = i;
        if (x === minK) lastMin = i;
        if (x === maxK) lastMax = i;
        ans += Math.max(0, Math.min(lastMin, lastMax) - bad);
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
- [3768. Minimum Inversion Count in Subarrays of Fixed Length](../../3501-4000/3768-minimum-inversion-count-in-subarrays-of-fixed-length/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1248-count-number-of-nice-subarrays/)
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)
