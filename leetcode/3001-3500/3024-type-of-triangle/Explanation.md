# LeetCode 3024: Type of Triangle

**LeetCode Problem #3024 — Type of Triangle**
Solve LeetCode Type of Triangle using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Type of Triangle |
| LeetCode | #3024 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of size `3` which can form the sides of a triangle.

A triangle is called **equilateral** if it has all sides of equal length. 
 A triangle is called **isosceles** if it has exactly two sides of equal length. 
 A triangle is called **scalene** if all its sides are of different lengths.

Return *a string representing* *the type of triangle that can be formed **or *`"none"`* if it **cannot** form a triangle.*

## Constraints
- `nums.length == 3`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [3,3,3]`
- **Output:** `"equilateral"`
- **Explanation:** Since all the sides are of equal length, therefore, it will form an equilateral triangle.

### Example 2
- **Input:** `nums = [3,4,5]`
- **Output:** `"scalene"`
- **Explanation:** nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Type of Triangle**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,3,3]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"equilateral"`.
4. **Verification:** Since all the sides are of equal length, therefore, it will form an equilateral triangle.

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
var triangleType = function(nums) {
    const [a, b, c] = nums;

    if (
        a + b <= c ||
        a + c <= b ||
        b + c <= a
    ) {
        return "none";
    }

    if (a === b && b === c) {
        return "equilateral";
    }

    if (a === b || b === c || a === c) {
        return "isosceles";
    }

    return "scalene";
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
- [118. Pascal's Triangle](../../0001-0500/0118-pascals-triangle/)
- [119. Pascal's Triangle II](../../0001-0500/0119-pascals-triangle-ii/)
- [120. Triangle](../../0001-0500/0120-triangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/type-of-triangle/)
