# LeetCode 3732: Maximum Product of Three Elements After One Replacement

**LeetCode Problem #3732 — Maximum Product of Three Elements After One Replacement**
Solve LeetCode Maximum Product of Three Elements After One Replacement using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Three Elements After One Replacement |
| LeetCode | #3732 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

You **must** replace **exactly one** element in the array with **any** integer value in the range `[-10^5, 10^5]` (inclusive).

After performing this single replacement, determine the **maximum possible product** of **any three** elements at **distinct indices** from the modified array.

Return an integer denoting the **maximum product** achievable.

## Constraints
- `3 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [-5,7,0]`
- **Output:** `3500000`
- **Explanation:** Replacing 0 with -10^5 gives the array `[-5, 7, -10^5]`, which has a product `(-5) * 7 * (-10^5) = 3500000`. The maximum product is 3500000.

### Example 2
- **Input:** `nums = [-4,-2,-1,-3]`
- **Output:** `1200000`
- **Explanation:** Two ways to achieve the maximum product include: 

 
 `[-4, -2, -3]` &rarr; replace -2 with 10^5 &rarr; product = `(-4) * 10^5 * (-3) = 1200000`. 
 `[-4, -1, -3]` &rarr; replace -1 with 10^5 &rarr; product = `(-4) * 10^5 * (-3) = 1200000`. 
 
The maximum product is 1200000.

### Example 3
- **Input:** `nums = [0,10,0]`
- **Output:** `0`
- **Explanation:** There is no way to replace an element with another integer and not have a 0 in the array. Hence, the product of all three elements will always be 0, and the maximum product is 0.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Product of Three Elements After One Replacement**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-5,7,0]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3500000`.
4. **Verification:** Replacing 0 with -10^5 gives the array `[-5, 7, -10^5]`, which has a product `(-5) * 7 * (-10^5) = 3500000`. The maximum product is 3500000.

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
var maxProduct = function(nums) {
    let max1 = 0;
    let max2 = 0;

    for (const num of nums) {
        const value = Math.abs(num);

        if (value >= max1) {
            max2 = max1;
            max1 = value;
        } else if (value > max2) {
            max2 = value;
        }
    }

    return 100000 * max1 * max2;
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
- [4066. Maximum Equal Adjacent Pairs After at Most One Replacement](../../4001-4500/4066-maximum-equal-adjacent-pairs-after-at-most-one-replacement/)
- [1464. Maximum Product of Two Elements in an Array](../../1001-1500/1464-maximum-product-of-two-elements-in-an-array/)
- [3397. Maximum Number of Distinct Elements After Operations](../../3001-3500/3397-maximum-number-of-distinct-elements-after-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/)
