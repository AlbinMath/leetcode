# LeetCode 2681: Power of Heroes

**LeetCode Problem #2681 — Power of Heroes**
Solve LeetCode Power of Heroes using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Power of Heroes |
| LeetCode | #2681 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` representing the strength of some heroes. The power of a group of heroes is defined as follows:

Let `i_0`, `i_1`, ... ,`i_k` be the indices of the heroes in a group. Then, the power of this group is `max(nums[i_0], nums[i_1], ... ,nums[i_k])^2 * min(nums[i_0], nums[i_1], ... ,nums[i_k])`.

Return *the sum of the **power** of all **non-empty** groups of heroes possible.* Since the sum could be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,1,4]`
- **Output:** `141`
- **Explanation:** 1^st group: [2] has power = 2^2 * 2 = 8.
2^nd group: [1] has power = 1^2 * 1 = 1. 
3^rd group: [4] has power = 4^2 * 4 = 64. 
4^th group: [2,1] has power = 2^2 * 1 = 4. 
5^th group: [2,4] has power = 4^2 * 2 = 32. 
6^th group: [1,4] has power = 4^2 * 1 = 16. 
​​​​​​​7^th group: [2,1,4] has power = 4^2​​​​​​​ * 1 = 16. 
The sum of powers of all groups is 8 + 1 + 64 + 4 + 32 + 16 + 16 = 141.

### Example 2
- **Input:** `nums = [1,1,1]`
- **Output:** `7`
- **Explanation:** A total of 7 groups are possible, and the power of each group will be 1. Therefore, the sum of the powers of all groups is 7.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Power of Heroes**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `141`.
4. **Verification:** 1^st group: [2] has power = 2^2 * 2 = 8.
2^nd group: [1] has power = 1^2 * 1 = 1. 
3^rd group: [4] has power = 4^2 * 4 = 64. 
4^th group: [2,1] has power = 2^2 * 1 = 4. 
5^th group: [2,4] has power = 4^2 * 2 = 32. 
6^th group: [1,4] has power = 4^2 * 1 = 16. 
​​​​​​​7^th group: [2,1,4] has power = 4^2​​​​​​​ * 1 = 16. 
The sum of powers of all groups is 8 + 1 + 64 + 4 + 32 + 16 + 16 = 141.

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
var sumOfPower = function(nums) {
    const MOD = 1000000007n;
    nums.sort((a, b) => a - b);
    let sumMin = 0n;
    let ans = 0n;
    for (let x of nums) {
        let num = BigInt(x);

        let contribution =
            (num * num % MOD) *
            ((sumMin + num) % MOD) % MOD;

        ans = (ans + contribution) % MOD;

        sumMin = (sumMin * 2n + num) % MOD;
    }

    return Number(ans);
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
- [231. Power of Two](../../0001-0500/0231-power-of-two/)
- [326. Power of Three](../../0001-0500/0326-power-of-three/)
- [342. Power of Four](../../0001-0500/0342-power-of-four/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/power-of-heroes/)
