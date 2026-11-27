# LeetCode 3576: Transform Array to All Equal Elements

**LeetCode Problem #3576 — Transform Array to All Equal Elements**
Solve LeetCode Transform Array to All Equal Elements using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Transform Array to All Equal Elements |
| LeetCode | #3576 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of size `n` containing only `1` and `-1`, and an integer `k`.

You can perform the following operation at most `k` times:

Choose an index `i` (`0 <= i < n - 1`), and **multiply** both `nums[i]` and `nums[i + 1]` by `-1`.

**Note** that you can choose the same index i more than once in **different** operations.

Return `true` if it is possible to make all elements of the array **equal** after at most `k` operations, and `false` otherwise.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `nums[i]` is either -1 or 1.
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `nums = [1,-1,1,-1,1], k = 3`
- **Output:** `true`
- **Explanation:** We can make all elements in the array equal in 2 operations as follows: 

 
 Choose index `i = 1`, and multiply both `nums[1]` and `nums[2]` by -1. Now `nums = [1,1,-1,-1,1]`. 
 Choose index `i = 2`, and multiply both `nums[2]` and `nums[3]` by -1. Now `nums = [1,1,1,1,1]`.

### Example 2
- **Input:** `nums = [-1,-1,-1,1,1,1], k = 5`
- **Output:** `false`
- **Explanation:** It is not possible to make all array elements equal in at most 5 operations.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Transform Array to All Equal Elements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,-1,1,-1,1], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We can make all elements in the array equal in 2 operations as follows: 

 
 Choose index `i = 1`, and multiply both `nums[1]` and `nums[2]` by -1. Now `nums = [1,1,-1,-1,1]`. 
 Choose index `i = 2`, and multiply both `nums[2]` and `nums[3]` by -1. Now `nums = [1,1,1,1,1]`.

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
var canMakeEqual = function(nums, k) {
    const n = nums.length;

    function check(target) {
        let operations = 0;
        for (let i = 0; i < n - 1; i++) {
            if (nums[i] !== target) {
                nums[i] *= -1;
                nums[i + 1] *= -1;
                operations++;
            }
        }
        return nums[n - 1] === target && operations <= k;
    }
    const original = nums.slice();

    if (check(1)) {
        return true;
    }
    for (let i = 0; i < n; i++) {
        nums[i] = original[i];
    }
    return check(-1);
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
- [2772. Apply Operations to Make All Array Elements Equal to Zero](../../2501-3000/2772-apply-operations-to-make-all-array-elements-equal-to-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/transform-array-to-all-equal-elements/)
