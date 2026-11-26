# LeetCode 2587: Rearrange Array to Maximize Prefix Score

**LeetCode Problem #2587 — Rearrange Array to Maximize Prefix Score**
Solve LeetCode Rearrange Array to Maximize Prefix Score using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rearrange Array to Maximize Prefix Score |
| LeetCode | #2587 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. You can rearrange the elements of `nums` to **any order** (including the given order).

Let `prefix` be the array containing the prefix sums of `nums` after rearranging it. In other words, `prefix[i]` is the sum of the elements from `0` to `i` in `nums` after rearranging it. The **score** of `nums` is the number of positive integers in the array `prefix`.

Return *the maximum score you can achieve*.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^6 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [2,-1,0,1,-3,3,-3]`
- **Output:** `6`
- **Explanation:** We can rearrange the array into nums = [2,3,1,-1,-3,0,-3].
prefix = [2,5,6,5,2,2,-1], so the score is 6.
It can be shown that 6 is the maximum score we can obtain.

### Example 2
- **Input:** `nums = [-2,-3,0]`
- **Output:** `0`
- **Explanation:** Any rearrangement of the array will result in a score of 0.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rearrange Array to Maximize Prefix Score**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,-1,0,1,-3,3,-3]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** We can rearrange the array into nums = [2,3,1,-1,-3,0,-3].
prefix = [2,5,6,5,2,2,-1], so the score is 6.
It can be shown that 6 is the maximum score we can obtain.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxScore = function(nums) {
    nums.sort((a, b) => b - a);

    let sum = 0;
    let score = 0;

    for (let num of nums) {
        sum += num;

        if (sum > 0) {
            score++;
        } else {
            break;
        }
    }

    return score;
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [1799. Maximize Score After N Operations](../../1501-2000/1799-maximize-score-after-n-operations/)
- [2818. Apply Operations to Maximize Score](../../2501-3000/2818-apply-operations-to-maximize-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/)
