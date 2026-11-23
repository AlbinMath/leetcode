# LeetCode 2221: Find Triangular Sum of an Array

**LeetCode Problem #2221 — Find Triangular Sum of an Array**
Solve LeetCode Find Triangular Sum of an Array using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Triangular Sum of an Array |
| LeetCode | #2221 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`, where `nums[i]` is a digit between `0` and `9` (**inclusive**).

The **triangular sum** of `nums` is the value of the only element present in `nums` after the following process terminates:

Let `nums` comprise of `n` elements. If `n == 1`, **end** the process. Otherwise, **create** a new **0-indexed** integer array `newNums` of length `n - 1`. 
 For each index `i`, where `0 <= i < n - 1`, **assign** the value of `newNums[i]` as `(nums[i] + nums[i+1]) % 10`, where `%` denotes modulo operator. 
 **Replace** the array `nums` with `newNums`. 
 **Repeat** the entire process starting from step 1.

Return *the triangular sum of* `nums`.

## Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `8`
- **Explanation:** The above diagram depicts the process from which we obtain the triangular sum of the array.

### Example 2
- **Input:** `nums = [5]`
- **Output:** `5`
- **Explanation:** Since there is only one element in nums, the triangular sum is the value of that element itself.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Triangular Sum of an Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The above diagram depicts the process from which we obtain the triangular sum of the array.

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
var triangularSum = function(nums) {
    while (nums.length > 1) {
        const next = [];

        for (let i = 0; i < nums.length - 1; i++) {
            next.push((nums[i] + nums[i + 1]) % 10);
        }

        nums = next;
    }

    return nums[0];
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
- [3539. Find Sum of Array Product of Magical Sequences](../../3501-4000/3851-find-sum-of-array-product-of-magical-sequences/)
- [167. Two Sum II - Input Array Is Sorted](../../0001-0500/0167-two-sum-ii---input-array-is-sorted/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-triangular-sum-of-an-array/)
