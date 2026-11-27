# LeetCode 2789: Largest Element in an Array after Merge Operations

**LeetCode Problem #2789 — Largest Element in an Array after Merge Operations**
Solve LeetCode Largest Element in an Array after Merge Operations using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Element in an Array after Merge Operations |
| LeetCode | #2789 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `nums` consisting of positive integers.

You can do the following operation on the array **any** number of times:

Choose an index `i` such that `0 <= i < nums.length - 1` and `nums[i] <= nums[i + 1]`. Replace the element `nums[i + 1]` with `nums[i] + nums[i + 1]` and delete the element `nums[i]` from the array.

Return *the value of the largest element that you can possibly obtain in the final array.*

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [2,3,7,9,3]`
- **Output:** `21`
- **Explanation:** We can apply the following operations on the array:
- Choose i = 0. The resulting array will be nums = [ 5 ,7,9,3].
- Choose i = 1. The resulting array will be nums = [5, 16 ,3].
- Choose i = 0. The resulting array will be nums = [ 21 ,3].
The largest element in the final array is 21. It can be shown that we cannot obtain a larger element.

### Example 2
- **Input:** `nums = [5,3,3]`
- **Output:** `11`
- **Explanation:** We can do the following operations on the array:
- Choose i = 1. The resulting array will be nums = [5, 6 ].
- Choose i = 0. The resulting array will be nums = [ 11 ].
There is only one element in the final array, which is 11.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Element in an Array after Merge Operations**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,7,9,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `21`.
4. **Verification:** We can apply the following operations on the array:
- Choose i = 0. The resulting array will be nums = [ 5 ,7,9,3].
- Choose i = 1. The resulting array will be nums = [5, 16 ,3].
- Choose i = 0. The resulting array will be nums = [ 21 ,3].
The largest element in the final array is 21. It can be shown that we cannot obtain a larger element.

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
var maxArrayValue = function(nums) {
    let sum = nums[nums.length - 1];
    let max = sum;

    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] <= sum) {
            sum += nums[i];
        } else {
            sum = nums[i];
        }

        max = Math.max(max, sum);
    }

    return max;
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
- [215. Kth Largest Element in an Array](../../0001-0500/0215-kth-largest-element-in-an-array/)
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3001-3500/3346-maximum-frequency-of-an-element-after-performing-operations-i/)
- [3347. Maximum Frequency of an Element After Performing Operations II](../../3001-3500/3347-maximum-frequency-of-an-element-after-performing-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/)
