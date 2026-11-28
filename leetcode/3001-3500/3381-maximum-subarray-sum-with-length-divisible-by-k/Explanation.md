# LeetCode 3381: Maximum Subarray Sum With Length Divisible by K

**LeetCode Problem #3381 — Maximum Subarray Sum With Length Divisible by K**
Solve LeetCode Maximum Subarray Sum With Length Divisible by K using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Subarray Sum With Length Divisible by K |
| LeetCode | #3381 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums` and an integer `k`.

Return the **maximum** sum of a subarray of `nums`, such that the size of the subarray is **divisible** by `k`.

## Constraints
- `1 <= k <= nums.length <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2], k = 1`
- **Output:** `3`
- **Explanation:** The subarray `[1, 2]` with sum 3 has length equal to 2 which is divisible by 1.

### Example 2
- **Input:** `nums = [-1,-2,-3,-4,-5], k = 4`
- **Output:** `-10`
- **Explanation:** The maximum sum subarray is `[-1, -2, -3, -4]` which has length equal to 4 which is divisible by 4.

### Example 3
- **Input:** `nums = [-5,1,2,-3,4], k = 2`
- **Output:** `4`
- **Explanation:** The maximum sum subarray is `[1, 2, -3, 4]` which has length equal to 4 which is divisible by 2.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Subarray Sum With Length Divisible by K**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2], k = 1`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The subarray `[1, 2]` with sum 3 has length equal to 2 which is divisible by 1.

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
var maxSubarraySum = function(nums, k) {
    const minPrefix = new Array(k).fill(Infinity);
    minPrefix[0] = 0;

    let prefixSum = 0;
    let ans = -Infinity;

    for (let i = 0; i < nums.length; i++) {
        prefixSum += nums[i];
        const remainder = (i + 1) % k;
        ans = Math.max(
            ans,
            prefixSum - minPrefix[remainder]
        );
        minPrefix[remainder] = Math.min(
            minPrefix[remainder],
            prefixSum
        );
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
- [3795. Minimum Subarray Length With Distinct Sum At Least K](../../3501-4000/3795-minimum-subarray-length-with-distinct-sum-at-least-k/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../../3501-4000/3962-maximum-subarray-sum-after-at-most-k-swaps/)
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2001-2500/2461-maximum-sum-of-distinct-subarrays-with-length-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/)
