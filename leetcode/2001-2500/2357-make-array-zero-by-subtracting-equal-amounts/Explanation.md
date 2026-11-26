# LeetCode 2357: Make Array Zero by Subtracting Equal Amounts

**LeetCode Problem #2357 — Make Array Zero by Subtracting Equal Amounts**
Solve LeetCode Make Array Zero by Subtracting Equal Amounts using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Array Zero by Subtracting Equal Amounts |
| LeetCode | #2357 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a non-negative integer array `nums`. In one operation, you must:

Choose a positive integer `x` such that `x` is less than or equal to the **smallest non-zero** element in `nums`. 
 Subtract `x` from every **positive** element in `nums`.

Return *the **minimum** number of operations to make every element in *`nums`* equal to *`0`.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,5,0,3,5]`
- **Output:** `3`
- **Explanation:** In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

### Example 2
- **Input:** `nums = [0]`
- **Output:** `0`
- **Explanation:** Each element in nums is already 0 so no operations are needed.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Make Array Zero by Subtracting Equal Amounts**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,5,0,3,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

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
var minimumOperations = function(nums) {
    // Store distinct non-zero elements in a Set
    const uniquePositives = new Set();
    for (const num of nums) {
        if (num > 0) {
            uniquePositives.add(num);
        }
    }
    return uniquePositives.size;
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
- [2772. Apply Operations to Make All Array Elements Equal to Zero](../../2501-3000/2772-apply-operations-to-make-all-array-elements-equal-to-zero/)
- [3354. Make Array Elements Equal to Zero](../../3001-3500/3354-make-array-elements-equal-to-zero/)
- [1787. Make the XOR of All Segments Equal to Zero](../../1501-2000/1787-make-the-xor-of-all-segments-equal-to-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/)
