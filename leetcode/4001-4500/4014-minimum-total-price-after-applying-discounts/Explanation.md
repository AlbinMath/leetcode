# LeetCode 4014: Minimum Total Price After Applying Discounts

**LeetCode Problem #4014 — Minimum Total Price After Applying Discounts**
Solve LeetCode Minimum Total Price After Applying Discounts using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Total Price After Applying Discounts |
| LeetCode | #4014 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `prices` and `discounts`.

The value `prices[i]` represents the price of the `i^th` item, and `discounts[j]` represents a discount percentage.

You may apply discounts subject to the following rules:

Each discount can be applied to **at most** one item. 
 Each item can receive **at most** one discount. 
 An item may also receive no discount.

If a discount of `d` percent is applied to an item with price `p`, its final price becomes `(p * (100 - d)) / 100`. The final price is **not** rounded.

Return the **minimum** possible sum of final prices after assigning discounts optimally. Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `1 <= prices.length, discounts.length <= 10^5`
- `1 <= prices[i] <= 10^5`
- `1 <= discounts[j] <= 100`

## Examples
### Example 1
- **Input:** `prices = [10,30,21], discounts = [50,60]`
- **Output:** `32.50000`
- **Explanation:** Apply `discounts[1] = 60` to `prices[1] = 30`, thus `30 * (100 - 60) / 100 = 12`. 
 Apply `discounts[0] = 50` to `prices[2] = 21`, thus `21 * (100 - 50) / 100 = 10.5`. 
 `prices[0] = 10` receives no discount, so it stays 10. 
 

 The total is `12 + 10.5 + 10 = 32.50000`, which is the minimum possible.

### Example 2
- **Input:** `prices = [100,70], discounts = [10,40,50]`
- **Output:** `92.00000`
- **Explanation:** ​​​​​​​ 

 
 Apply `discounts[2] = 50` to `prices[0] = 100`, thus `100 * (100 - 50) / 100 = 50`. 
 Apply `discounts[1] = 40` to `prices[1] = 70`, thus `70 * (100 - 40) / 100 = 42`. 
 

 The total is `50 + 42 = 92.00000`, which is the minimum possible.

### Example 3
- **Input:** `prices = [7,3,9], discounts = [100,100]`
- **Output:** `3.00000`
- **Explanation:** Apply `discounts[0] = 100` to `prices[2] = 9`, thus `9 * (100 - 100) / 100 = 0`. 
 Apply `discounts[1] = 100` to `prices[0] = 7`, thus `7 * (100 - 100) / 100 = 0`. 
 `prices[1] = 3` receives no discount, so it stays 3. 
 

 The total is `0 + 0 + 3 = 3.00000`, which is the minimum possible.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Total Price After Applying Discounts**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `prices = [10,30,21], discounts = [50,60]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `32.50000`.
4. **Verification:** Apply `discounts[1] = 60` to `prices[1] = 30`, thus `30 * (100 - 60) / 100 = 12`. 
 Apply `discounts[0] = 50` to `prices[2] = 21`, thus `21 * (100 - 50) / 100 = 10.5`. 
 `prices[0] = 10` receives no discount, so it stays 10. 
 

 The total is `12 + 10.5 + 10 = 32.50000`, which is the minimum possible.

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
var minPrice = function(prices, discounts) {
    prices.sort((a, b) => b - a);
    discounts.sort((a, b) => b - a);

    let total = 0;
    const limit = Math.min(prices.length, discounts.length);

    for (let i = 0; i < prices.length; i++) {
        if (i < limit) {
            total += prices[i] * (100 - discounts[i]) / 100;
        } else {
            total += prices[i];
        }
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
- [1959. Minimum Total Space Wasted With K Resizing Operations](../../1501-2000/1959-minimum-total-space-wasted-with-k-resizing-operations/)
- [2463. Minimum Total Distance Traveled](../../2001-2500/2463-minimum-total-distance-traveled/)
- [2499. Minimum Total Cost to Make Arrays Unequal](../../2001-2500/2499-minimum-total-cost-to-make-arrays-unequal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-total-price-after-applying-discounts/)
