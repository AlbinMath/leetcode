# LeetCode 3075: Maximize Happiness of Selected Children

**LeetCode Problem #3075 — Maximize Happiness of Selected Children**
Solve LeetCode Maximize Happiness of Selected Children using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Happiness of Selected Children |
| LeetCode | #3075 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `happiness` of length `n`, and a **positive** integer `k`.

There are `n` children standing in a queue, where the `i^th` child has **happiness value** `happiness[i]`. You want to select `k` children from these `n` children in `k` turns.

In each turn, when you select a child, the **happiness value** of all the children that have **not** been selected till now decreases by `1`. Note that the happiness value **cannot** become negative and gets decremented **only** if it is positive.

Return *the **maximum** sum of the happiness values of the selected children you can achieve by selecting *`k` *children*.

## Constraints
- `1 <= n == happiness.length <= 2 * 10^5`
- `1 <= happiness[i] <= 10^8`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `happiness = [1,2,3], k = 2`
- **Output:** `4`
- **Explanation:** We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.

### Example 2
- **Input:** `happiness = [1,1,1,1], k = 2`
- **Output:** `1`
- **Explanation:** We can pick 2 children in the following way:
- Pick any child with the happiness value == 1. The happiness value of the remaining children becomes [0,0,0].
- Pick the child with the happiness value == 0. The happiness value of the remaining child becomes [0,0].
The sum of the happiness values of the selected children is 1 + 0 = 1.

### Example 3
- **Input:** `happiness = [2,3,4,5], k = 1`
- **Output:** `5`
- **Explanation:** We can pick 1 child in the following way:
- Pick the child with the happiness value == 5. The happiness value of the remaining children becomes [1,2,3].
The sum of the happiness values of the selected children is 5.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Happiness of Selected Children**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `happiness = [1,2,3], k = 2`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.

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
var maximumHappinessSum = function(happiness, k) {
    happiness.sort((a, b) => b - a);

    let total = 0;

    for (let i = 0; i < k; i++) {
        total += Math.max(0, happiness[i] - i);
    }

    return total;
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
- [1659. Maximize Grid Happiness](../../1501-2000/1659-maximize-grid-happiness/)
- [3974. Maximum Total Sum of K Selected Elements](../../3501-4000/3974-maximum-total-sum-of-k-selected-elements/)
- [2226. Maximum Candies Allocated to K Children](../../2001-2500/2226-maximum-candies-allocated-to-k-children/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-happiness-of-selected-children/)
