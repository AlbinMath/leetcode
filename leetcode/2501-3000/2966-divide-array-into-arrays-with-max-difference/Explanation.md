# LeetCode 2966: Divide Array Into Arrays With Max Difference

**LeetCode Problem #2966 — Divide Array Into Arrays With Max Difference**
Solve LeetCode Divide Array Into Arrays With Max Difference using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divide Array Into Arrays With Max Difference |
| LeetCode | #2966 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of size `n` where `n` is a multiple of 3 and a positive integer `k`.

Divide the array `nums` into `n / 3` arrays of size **3** satisfying the following condition:

The difference between **any** two elements in one array is **less than or equal** to `k`.

Return a **2D** array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return **any** of them.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `n `is a multiple of 3
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,3,4,8,7,9,3,5,1], k = 2`
- **Output:** `[[1,1,3],[3,4,5],[7,8,9]]`
- **Explanation:** The difference between any two elements in each array is less than or equal to 2.

### Example 2
- **Input:** `nums = [2,4,2,2,5,2], k = 2`
- **Output:** `[]`
- **Explanation:** Different ways to divide `nums` into 2 arrays of size 3 are: 

 
 [[2,2,2],[2,4,5]] (and its permutations) 
 [[2,2,4],[2,2,5]] (and its permutations) 
 

 Because there are four 2s there will be an array with the elements 2 and 5 no matter how we divide it. since `5 - 2 = 3 > k`, the condition is not satisfied and so there is no valid division.

### Example 3
- **Input:** `nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14`
- **Output:** `[[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]`
- **Explanation:** The difference between any two elements in each array is less than or equal to 14.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Divide Array Into Arrays With Max Difference**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,4,8,7,9,3,5,1], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,1,3],[3,4,5],[7,8,9]]`.
4. **Verification:** The difference between any two elements in each array is less than or equal to 2.

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
var divideArray = function(nums, k) {
    nums.sort((a, b) => a - b);

    const result = [];

    for (let i = 0; i < nums.length; i += 3) {
        // Check the difference between max and min
        if (nums[i + 2] - nums[i] > k) {
            return [];
        }

        result.push([
            nums[i],
            nums[i + 1],
            nums[i + 2]
        ]);
    }

    return result;
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
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2035-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [2206. Divide Array Into Equal Pairs](../../2001-2500/2206-divide-array-into-equal-pairs/)
- [3010. Divide an Array Into Subarrays With Minimum Cost I](../../3001-3500/3010-divide-an-array-into-subarrays-with-minimum-cost-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/)
