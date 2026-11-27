# LeetCode 2952: Minimum Number of Coins to be Added

**LeetCode Problem #2952 — Minimum Number of Coins to be Added**
Solve LeetCode Minimum Number of Coins to be Added using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Coins to be Added |
| LeetCode | #2952 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `coins`, representing the values of the coins available, and an integer `target`.

An integer `x` is **obtainable** if there exists a subsequence of `coins` that sums to `x`.

Return *the** minimum** number of coins **of any value** that need to be added to the array so that every integer in the range* `[1, target]`* is **obtainable***.

A **subsequence** of an array is a new **non-empty** array that is formed from the original array by deleting some (**possibly none**) of the elements without disturbing the relative positions of the remaining elements.

## Constraints
- `1 <= target <= 10^5`
- `1 <= coins.length <= 10^5`
- `1 <= coins[i] <= target`

## Examples
### Example 1
- **Input:** `coins = [1,4,10], target = 19`
- **Output:** `2`
- **Explanation:** We need to add coins 2 and 8. The resulting array will be [1,2,4,8,10].
It can be shown that all integers from 1 to 19 are obtainable from the resulting array, and that 2 is the minimum number of coins that need to be added to the array.

### Example 2
- **Input:** `coins = [1,4,10,5,7,19], target = 19`
- **Output:** `1`
- **Explanation:** We only need to add the coin 2. The resulting array will be [1,2,4,5,7,10,19].
It can be shown that all integers from 1 to 19 are obtainable from the resulting array, and that 1 is the minimum number of coins that need to be added to the array.

### Example 3
- **Input:** `coins = [1,1,1], target = 20`
- **Output:** `3`
- **Explanation:** We need to add coins 4, 8, and 16. The resulting array will be [1,1,1,4,8,16].
It can be shown that all integers from 1 to 20 are obtainable from the resulting array, and that 3 is the minimum number of coins that need to be added to the array.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Coins to be Added**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coins = [1,4,10], target = 19`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We need to add coins 2 and 8. The resulting array will be [1,2,4,8,10].
It can be shown that all integers from 1 to 19 are obtainable from the resulting array, and that 2 is the minimum number of coins that need to be added to the array.

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
var minimumAddedCoins = function(coins, target) {
    coins.sort((a, b) => a - b);

    let missing = 1;
    let i = 0;
    let count = 0;

    while (missing <= target) {
        if (i < coins.length && coins[i] <= missing) {
            missing += coins[i];
            i++;
        } else {
            missing *= 2;
            count++;
        }
    }

    return count;
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
- [2944. Minimum Number of Coins for Fruits](../../2501-3000/2944-minimum-number-of-coins-for-fruits/)
- [1353. Maximum Number of Events That Can Be Attended](../../1001-1500/1353-maximum-number-of-events-that-can-be-attended/)
- [1751. Maximum Number of Events That Can Be Attended II](../../1501-2000/1751-maximum-number-of-events-that-can-be-attended-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-coins-to-be-added/)
