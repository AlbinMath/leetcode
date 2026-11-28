# LeetCode 2938: Separate Black and White Balls

**LeetCode Problem #2938 — Separate Black and White Balls**
Solve LeetCode Separate Black and White Balls using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Separate Black and White Balls |
| LeetCode | #2938 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` balls on a table, each ball has a color black or white.

You are given a **0-indexed** binary string `s` of length `n`, where `1` and `0` represent black and white balls, respectively.

In each step, you can choose two adjacent balls and swap them.

Return *the **minimum** number of steps to group all the black balls to the right and all the white balls to the left*.

## Constraints
- `1 <= n == s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "101"`
- **Output:** `1`
- **Explanation:** We can group all the black balls to the right in the following way:
- Swap s[0] and s[1], s = "011".
Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.

### Example 2
- **Input:** `s = "100"`
- **Output:** `2`
- **Explanation:** We can group all the black balls to the right in the following way:
- Swap s[0] and s[1], s = "010".
- Swap s[1] and s[2], s = "001".
It can be proven that the minimum number of steps needed is 2.

### Example 3
- **Input:** `s = "0111"`
- **Output:** `0`
- **Explanation:** All the black balls are already grouped to the right.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Separate Black and White Balls**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "101"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** We can group all the black balls to the right in the following way:
- Swap s[0] and s[1], s = "011".
Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.

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
var minimumSteps = function(s) {
    let ones = 0;
    let swaps = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            ones++;
        } else {
            swaps += ones;
        }
    }

    return swaps;
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
- [2209. Minimum White Tiles After Covering With Carpets](../../2001-2500/2209-minimum-white-tiles-after-covering-with-carpets/)
- [2271. Maximum White Tiles Covered by a Carpet](../../2001-2500/2271-maximum-white-tiles-covered-by-a-carpet/)
- [1977. Number of Ways to Separate Numbers](../../1501-2000/1977-number-of-ways-to-separate-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/separate-black-and-white-balls/)
