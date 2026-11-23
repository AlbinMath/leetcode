# LeetCode 2996: Smallest Missing Integer Greater Than Sequential Prefix Sum

**LeetCode Problem #2996 — Smallest Missing Integer Greater Than Sequential Prefix Sum**
Solve LeetCode Smallest Missing Integer Greater Than Sequential Prefix Sum using Rust and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Missing Integer Greater Than Sequential Prefix Sum |
| LeetCode | #2996 |
| Difficulty | Easy |
| Language | Rust |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
**Note: **The updated title is **"Smallest Missing Integer Greater Than or Equal to Sequential Prefix Sum".**

You are given a **0-indexed** array of integers `nums`.

A prefix `nums[0..i]` is **sequential** if, for all `1 <= j <= i`, `nums[j] = nums[j - 1] + 1`. In particular, the prefix consisting only of `nums[0]` is **sequential**.

Return *the **smallest** integer* `x` *missing from* `nums` *such that* `x` *is greater than or equal to the sum of the **longest** sequential prefix.*

## Constraints
- `1 <= nums.length <= 50`
- `1 <= nums[i] <= 50`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,2,5]`
- **Output:** `6`
- **Explanation:** The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

### Example 2
- **Input:** `nums = [3,4,5,1,12,14,13]`
- **Output:** `15`
- **Explanation:** The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Missing Integer Greater Than Sequential Prefix Sum**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,2,5]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Rust

## Source Code
- [solution.rs](./solution.rs)


```rust
impl Solution {
    pub fn missing_integer(nums: Vec<i32>) -> i32 {
        let mut sum = nums[0];

        // Find the longest sequential prefix
        for i in 1..nums.len() {
            if nums[i] == nums[i - 1] + 1 {
                sum += nums[i];
            } else {
                break;
            }
        }

        // Find the smallest missing integer >= sum
        let mut ans = sum;

        while nums.contains(&ans) {
            ans += 1;
        }

        ans
    }
}
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
- [3091. Apply Operations to Make Sum of Array Greater Than or Equal to k](../../3001-3500/3328-apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/)
- [744. Find Smallest Letter Greater Than Target](../../0501-1000/0745-find-smallest-letter-greater-than-target/)
- [3720. Lexicographically Smallest Permutation Greater Than Target](../../4001-4500/4020-lexicographically-smallest-permutation-greater-than-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/)
