# LeetCode 2441: Largest Positive Integer That Exists With Its Negative

**LeetCode Problem #2441 — Largest Positive Integer That Exists With Its Negative**
Solve LeetCode Largest Positive Integer That Exists With Its Negative using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Positive Integer That Exists With Its Negative |
| LeetCode | #2441 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` that **does not contain** any zeros, find **the largest positive** integer `k` such that `-k` also exists in the array.

Return *the positive integer *`k`. If there is no such integer, return `-1`.

## Constraints
- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- `nums[i] != 0`

## Examples
### Example 1
- **Input:** `nums = [-1,2,-3,3]`
- **Output:** `3`
- **Explanation:** 3 is the only valid k we can find in the array.

### Example 2
- **Input:** `nums = [-1,10,6,7,-7,1]`
- **Output:** `7`
- **Explanation:** Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

### Example 3
- **Input:** `nums = [-10,8,6,7,-2,-3]`
- **Output:** `-1`
- **Explanation:** There is no a single valid k, we return -1.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Positive Integer That Exists With Its Negative**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-1,2,-3,3]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** 3 is the only valid k we can find in the array.

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
var findMaxK = function(nums) {
    const set = new Set(nums);
    let maxK = -1;

    for (const num of nums) {
        if (num > 0 && set.has(-num)) {
            maxK = Math.max(maxK, num);
        }
    }

    return maxK;
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
- [2529. Maximum Count of Positive Integer and Negative Integer](../../2501-3000/2529-maximum-count-of-positive-integer-and-negative-integer/)
- [1449. Form Largest Integer With Digits That Add up to Target](../../1001-1500/1449-form-largest-integer-with-digits-that-add-up-to-target/)
- [2598. Smallest Missing Non-negative Integer After Operations](../../2501-3000/2598-smallest-missing-non-negative-integer-after-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/)
