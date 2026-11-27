# LeetCode 3914: Minimum Operations to Make Array Non Decreasing

**LeetCode Problem #3914 — Minimum Operations to Make Array Non Decreasing**
Solve LeetCode Minimum Operations to Make Array Non Decreasing using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make Array Non Decreasing |
| LeetCode | #3914 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

In one operation, you may choose any ** subarray ** `nums[l..r]` and **increase** each element in that **subarray** by `x`, where `x` is any **positive** integer.

Return the **minimum** possible **sum** of the values of `x` across all operations required to make the array **non-decreasing**.

An array is **non-decreasing** if `nums[i] <= nums[i + 1]` for all `0 <= i < n - 1`.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,3,2,1]`
- **Output:** `2`
- **Explanation:** One optimal set of operations: 

 
 Choose subarray `[2..3]` and add `x = 1` resulting in `[3, 3, 3, 2]` 
 Choose subarray `[3..3]` and add `x = 1` resulting in `[3, 3, 3, 3]` 
 

 The array becomes non-decreasing, and the total sum of chosen `x` values is `1 + 1 = 2`.

### Example 2
- **Input:** `nums = [5,1,2,3]`
- **Output:** `4`
- **Explanation:** One optimal set of operations: 

 
 Choose subarray `[1..3]` and add `x = 4` resulting in `[5, 5, 6, 7]` 
 

 The array becomes non-decreasing, and the total sum of chosen `x` values is `4`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Make Array Non Decreasing**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,3,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One optimal set of operations: 

 
 Choose subarray `[2..3]` and add `x = 1` resulting in `[3, 3, 3, 2]` 
 Choose subarray `[3..3]` and add `x = 1` resulting in `[3, 3, 3, 3]` 
 

 The array becomes non-decreasing, and the total sum of chosen `x` values is `1 + 1 = 2`.

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
var minOperations = function(nums) {
    let ans = 0;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < nums[i - 1]) {
            ans += nums[i - 1] - nums[i];
        }
    }

    return ans;
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
- [3326. Minimum Division Operations to Make Array Non Decreasing](../../3001-3500/3326-minimum-division-operations-to-make-array-non-decreasing/)
- [1551. Minimum Operations to Make Array Equal](../../1501-2000/1551-minimum-operations-to-make-array-equal/)
- [1827. Minimum Operations to Make the Array Increasing](../../1501-2000/1827-minimum-operations-to-make-the-array-increasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/)
