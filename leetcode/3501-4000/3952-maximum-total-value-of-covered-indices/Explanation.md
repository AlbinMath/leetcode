# LeetCode 3952: Maximum Total Value of Covered Indices

**LeetCode Problem #3952 — Maximum Total Value of Covered Indices**
Solve LeetCode Maximum Total Value of Covered Indices using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Total Value of Covered Indices |
| LeetCode | #3952 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and a binary string `s` of length `n`, where `s[i] == '1'` means index `i` initially contains a **token** and `s[i] == '0'` means it does not.

You may perform the following operation any number of times:

Choose a token currently located at index `i`, where `i > 0`, such that this token has **not** been moved before. 
 Move this token from index `i` to index `i - 1`.

An index is considered **covered** if it contains a token after all moves.

Return an integer denoting the **maximum total value** of `nums` at the covered indices after optimally performing the operations.

## Constraints
- `1 <= n == nums.length == s.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- ​​​​​​​`s[i]` is either `'0'` or `'1'`

## Examples
### Example 1
- **Input:** `nums = [9,2,6,1], s = "0101"`
- **Output:** `15`
- **Explanation:** Initially, indices 1 and 3 contain tokens. 
 Move the token from index 3 to index 2. 
 Move the token from index 1 to index 0. 
 The covered indices are `[0, 2]`, so the total value is `nums[0] + nums[2] = 9 + 6 = 15`.

### Example 2
- **Input:** `nums = [5,1,4], s = "001"`
- **Output:** `4`
- **Explanation:** Initially, only index 2 contains a token. 
 It is optimal to leave the token at index 2. 
 The covered index is `[2]`, so the total value is `nums[2] = 4`.

### Example 3
- **Input:** `nums = [9,3,5], s = "011"`
- **Output:** `14`
- **Explanation:** Initially, indices 1 and 2 contain tokens. 
 Move the token from index 1 to index 0. 
 The covered indices are `[0, 2]`, so the total value is `nums[0] + nums[2] = 9 + 5 = 14`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Total Value of Covered Indices**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [9,2,6,1], s = "0101"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** Initially, indices 1 and 3 contain tokens. 
 Move the token from index 3 to index 2. 
 Move the token from index 1 to index 0. 
 The covered indices are `[0, 2]`, so the total value is `nums[0] + nums[2] = 9 + 6 = 15`.

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
var maxTotal = function(nums, s) {
    const NEG_INF = -Infinity;

    let prev = -1;
    let dpLeft = NEG_INF;
    let dpStay = NEG_INF;

    for (let i = 0; i < nums.length; i++) {
        if (s[i] === '0') continue;

        if (prev === -1) {
            dpLeft = i > 0 ? nums[i - 1] : NEG_INF;
            dpStay = nums[i];
        } else {
            const best = Math.max(dpLeft, dpStay);

            if (i === prev + 1) {
                dpLeft = dpLeft + nums[i - 1];
                dpStay = best + nums[i];
            } else {
                dpLeft = best + nums[i - 1];
                dpStay = best + nums[i];
            }
        }

        prev = i;
    }

    if (prev === -1) return 0;

    return Math.max(dpLeft, dpStay);
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
- [3689. Maximum Total Subarray Value I](../../3501-4000/3689-maximum-total-subarray-value-i/)
- [3691. Maximum Total Subarray Value II](../../3501-4000/3691-maximum-total-subarray-value-ii/)
- [3971. Maximum Total Value](../../3501-4000/3971-maximum-total-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-total-value-of-covered-indices/)
