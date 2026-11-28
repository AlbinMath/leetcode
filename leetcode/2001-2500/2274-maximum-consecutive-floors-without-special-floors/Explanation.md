# LeetCode 2274: Maximum Consecutive Floors Without Special Floors

**LeetCode Problem #2274 — Maximum Consecutive Floors Without Special Floors**
Solve LeetCode Maximum Consecutive Floors Without Special Floors using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Consecutive Floors Without Special Floors |
| LeetCode | #2274 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice manages a company and has rented some floors of a building as office space. Alice has decided some of these floors should be **special floors**, used for relaxation only.

You are given two integers `bottom` and `top`, which denote that Alice has rented all the floors from `bottom` to `top` (**inclusive**). You are also given the integer array `special`, where `special[i]` denotes a special floor that Alice has designated for relaxation.

Return *the **maximum** number of consecutive floors without a special floor*.

## Constraints
- `1 <= special.length <= 10^5`
- `1 <= bottom <= special[i] <= top <= 10^9`
- All the values of `special` are **unique**.

## Examples
### Example 1
- **Input:** `bottom = 2, top = 9, special = [4,6]`
- **Output:** `3`
- **Explanation:** The following are the ranges (inclusive) of consecutive floors without a special floor:
- (2, 3) with a total amount of 2 floors.
- (5, 5) with a total amount of 1 floor.
- (7, 9) with a total amount of 3 floors.
Therefore, we return the maximum number which is 3 floors.

### Example 2
- **Input:** `bottom = 6, top = 8, special = [7,6,8]`
- **Output:** `0`
- **Explanation:** Every floor rented is a special floor, so we return 0.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Consecutive Floors Without Special Floors**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `bottom = 2, top = 9, special = [4,6]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The following are the ranges (inclusive) of consecutive floors without a special floor:
- (2, 3) with a total amount of 2 floors.
- (5, 5) with a total amount of 1 floor.
- (7, 9) with a total amount of 3 floors.
Therefore, we return the maximum number which is 3 floors.

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
var maxConsecutive = function(bottom, top, special) {
    special.sort((a, b) => a - b);

    let maxGap = 0;
    let previous = bottom - 1;

    for (const floor of special) {
        const gap = floor - previous - 1;

        maxGap = Math.max(maxGap, gap);
        previous = floor;
    }
    const lastGap = top - previous;

    maxGap = Math.max(maxGap, lastGap);

    return maxGap;
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
- [1798. Maximum Number of Consecutive Values You Can Make](../../1501-2000/1798-maximum-number-of-consecutive-values-you-can-make/)
- [3413. Maximum Coins From K Consecutive Bags](../../3001-3500/3413-maximum-coins-from-k-consecutive-bags/)
- [600. Non-negative Integers without Consecutive Ones](../../0501-1000/0600-non-negative-integers-without-consecutive-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/)
