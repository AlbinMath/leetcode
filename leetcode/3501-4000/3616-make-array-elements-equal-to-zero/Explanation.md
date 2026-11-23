# LeetCode 3354: Make Array Elements Equal to Zero

**LeetCode Problem #3354 — Make Array Elements Equal to Zero**
Solve LeetCode Make Array Elements Equal to Zero using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Array Elements Equal to Zero |
| LeetCode | #3354 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Start by selecting a starting position `curr` such that `nums[curr] == 0`, and choose a movement **direction** of either left or right.

After that, you repeat the following process:

If `curr` is out of the range `[0, n - 1]`, this process ends. 
 If `nums[curr] == 0`, move in the current direction by **incrementing** `curr` if you are moving right, or **decrementing** `curr` if you are moving left. 
 Else if `nums[curr] > 0`:
 
 Decrement `nums[curr]` by 1. 
 **Reverse** your movement direction (left becomes right and vice versa). 
 Take a step in your new direction.

A selection of the initial position `curr` and movement direction is considered **valid** if every element in `nums` becomes 0 by the end of the process.

Return the number of possible **valid** selections.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`
- There is at least one element `i` where `nums[i] == 0`.

## Examples
### Example 1
- **Input:** `nums = [1,0,2,0,3]`
- **Output:** `2`
- **Explanation:** The only possible valid selections are the following: 

 
 Choose `curr = 3`, and a movement direction to the left.

 
 [1,0,2,

### Example 2
- **Input:** `nums = [2,3,4,0,4,1,0]`
- **Output:** `0`
- **Explanation:** There are no possible valid selections.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Make Array Elements Equal to Zero**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,0,2,0,3]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The only possible valid selections are the following: 

 
 Choose `curr = 3`, and a movement direction to the left.

 
 [1,0,2,

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
var countValidSelections = function(nums) {
    let totalSum = 0;
    for (const num of nums) totalSum += num;

    let leftSum = 0;
    let validSelections = 0;

    for (const num of nums) {
        if (num === 0) {
            const rightSum = totalSum - leftSum;
            const diff = Math.abs(leftSum - rightSum);
            if (diff === 0) {
                validSelections += 2;
            } else if (diff === 1) {
                validSelections += 1;
            }
        } else {
            leftSum += num;
        }
    }

    return validSelections;
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
- [1887. Reduction Operations to Make the Array Elements Equal](../../2001-2500/2016-reduction-operations-to-make-the-array-elements-equal/)
- [2357. Make Array Zero by Subtracting Equal Amounts](../../2001-2500/2436-make-array-zero-by-subtracting-equal-amounts/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2753-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-array-elements-equal-to-zero/)
