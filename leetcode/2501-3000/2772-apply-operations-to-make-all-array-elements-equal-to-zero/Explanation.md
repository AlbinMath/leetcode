# LeetCode 2772: Apply Operations to Make All Array Elements Equal to Zero

**LeetCode Problem #2772 — Apply Operations to Make All Array Elements Equal to Zero**
Solve LeetCode Apply Operations to Make All Array Elements Equal to Zero using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apply Operations to Make All Array Elements Equal to Zero |
| LeetCode | #2772 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and a positive integer `k`.

You can apply the following operation on the array **any** number of times:

Choose **any** subarray of size `k` from the array and **decrease** all its elements by `1`.

Return `true`* if you can make all the array elements equal to *`0`*, or *`false`* otherwise*.

A **subarray** is a contiguous non-empty part of an array.

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [2,2,3,1,1,0], k = 3`
- **Output:** `true`
- **Explanation:** We can do the following operations:
- Choose the subarray [2,2,3]. The resulting array will be nums = [

### Example 2
- **Input:** `nums = [1,3,1,1], k = 2`
- **Output:** `false`
- **Explanation:** It is not possible to make all the array elements equal to 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Apply Operations to Make All Array Elements Equal to Zero**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,2,3,1,1,0], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We can do the following operations:
- Choose the subarray [2,2,3]. The resulting array will be nums = [

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
var checkArray = function(nums, k) {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);

    let operations = 0;

    for (let i = 0; i < n; i++) {
        operations += diff[i];

        let current = nums[i] - operations;

        if (current < 0) {
            return false;
        }
        if (current === 0) {
            continue;
        }
        if (i + k > n) {
            return false;
        }
        operations += current;
        diff[i + k] -= current;
    }

    return true;
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
- [2602. Minimum Operations to Make All Array Elements Equal](../../2501-3000/2602-minimum-operations-to-make-all-array-elements-equal/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [3354. Make Array Elements Equal to Zero](../../3001-3500/3354-make-array-elements-equal-to-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/)
