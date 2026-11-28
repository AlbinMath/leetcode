# LeetCode 3487: Maximum Unique Subarray Sum After Deletion

**LeetCode Problem #3487 — Maximum Unique Subarray Sum After Deletion**
Solve LeetCode Maximum Unique Subarray Sum After Deletion using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Unique Subarray Sum After Deletion |
| LeetCode | #3487 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

You are allowed to delete any number of elements from `nums` without making it **empty**. After performing the deletions, select a subarray of `nums` such that:

All elements in the subarray are **unique**. 
 The sum of the elements in the subarray is **maximized**.

Return the **maximum sum** of such a subarray.

## Constraints
- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `15`
- **Explanation:** Select the entire array without deleting any element to obtain the maximum sum.

### Example 2
- **Input:** `nums = [1,1,0,1,1]`
- **Output:** `1`
- **Explanation:** Delete the element `nums[0] == 1`, `nums[1] == 1`, `nums[2] == 0`, and `nums[3] == 1`. Select the entire array `[1]` to obtain the maximum sum.

### Example 3
- **Input:** `nums = [1,2,-1,-2,1,0,-1]`
- **Output:** `3`
- **Explanation:** Delete the elements `nums[2] == -1` and `nums[3] == -2`, and select the subarray `[2, 1]` from `[1, 2, 1, 0, -1]` to obtain the maximum sum.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Unique Subarray Sum After Deletion**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** Select the entire array without deleting any element to obtain the maximum sum.

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
var maxSum = function(nums) {
    const seen = new Set();
    let sum = 0;
    let maxValue = -Infinity;

    for (const num of nums) {
        maxValue = Math.max(maxValue, num);

        if (num > 0 && !seen.has(num)) {
            sum += num;
            seen.add(num);
        }
    }
    return sum > 0 ? sum : maxValue;
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
- [1186. Maximum Subarray Sum with One Deletion](../../1001-1500/1186-maximum-subarray-sum-with-one-deletion/)
- [2841. Maximum Sum of Almost Unique Subarray](../../2501-3000/2841-maximum-sum-of-almost-unique-subarray/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../../3501-4000/3962-maximum-subarray-sum-after-at-most-k-swaps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/)
