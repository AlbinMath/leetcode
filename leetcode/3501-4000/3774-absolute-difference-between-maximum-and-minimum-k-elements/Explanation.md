# LeetCode 3774: Absolute Difference Between Maximum and Minimum K Elements

**LeetCode Problem #3774 — Absolute Difference Between Maximum and Minimum K Elements**
Solve LeetCode Absolute Difference Between Maximum and Minimum K Elements using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Absolute Difference Between Maximum and Minimum K Elements |
| LeetCode | #3774 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

Find the absolute difference between:

the **sum** of the `k` **largest** elements in the array; and 
 the **sum** of the `k` **smallest** elements in the array.

Return an integer denoting this difference.

## Constraints
- `1 <= n == nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `nums = [5,2,2,4], k = 2`
- **Output:** `5`
- **Explanation:** The `k = 2` largest elements are 4 and 5. Their sum is `4 + 5 = 9`. 
 The `k = 2` smallest elements are 2 and 2. Their sum is `2 + 2 = 4`. 
 The absolute difference is `abs(9 - 4) = 5`.

### Example 2
- **Input:** `nums = [100], k = 1`
- **Output:** `0`
- **Explanation:** The largest element is 100. 
 The smallest element is 100. 
 The absolute difference is `abs(100 - 100) = 0`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Absolute Difference Between Maximum and Minimum K Elements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,2,2,4], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The `k = 2` largest elements are 4 and 5. Their sum is `4 + 5 = 9`. 
 The `k = 2` smallest elements are 2 and 2. Their sum is `2 + 2 = 4`. 
 The absolute difference is `abs(9 - 4) = 5`.

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
var absDifference = function(nums, k) {
    nums.sort((a, b) => a - b);

    let smallestSum = 0;
    let largestSum = 0;
    const n = nums.length;

    for (let i = 0; i < k; i++) {
        smallestSum += nums[i];
        largestSum += nums[n - 1 - i];
    }

    return Math.abs(largestSum - smallestSum);
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
- [2817. Minimum Absolute Difference Between Elements With Constraint](../../2501-3000/2817-minimum-absolute-difference-between-elements-with-constraint/)
- [1984. Minimum Difference Between Highest and Lowest of K Scores](../../1501-2000/1984-minimum-difference-between-highest-and-lowest-of-k-scores/)
- [3880. Minimum Absolute Difference Between Two Values](../../3501-4000/3880-minimum-absolute-difference-between-two-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/)
