# LeetCode 3300: Minimum Element After Replacement With Digit Sum

**LeetCode Problem #3300 — Minimum Element After Replacement With Digit Sum**
Solve LeetCode Minimum Element After Replacement With Digit Sum using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Element After Replacement With Digit Sum |
| LeetCode | #3300 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

You replace each element in `nums` with the **sum** of its digits.

Return the **minimum** element in `nums` after all replacements.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [10,12,13,14]`
- **Output:** `1`
- **Explanation:** `nums` becomes `[1, 3, 4, 5]` after all replacements, with minimum element 1.

### Example 2
- **Input:** `nums = [1,2,3,4]`
- **Output:** `1`
- **Explanation:** `nums` becomes `[1, 2, 3, 4]` after all replacements, with minimum element 1.

### Example 3
- **Input:** `nums = [999,19,199]`
- **Output:** `10`
- **Explanation:** `nums` becomes `[27, 10, 19]` after all replacements, with minimum element 10.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Element After Replacement With Digit Sum**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,12,13,14]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** `nums` becomes `[1, 3, 4, 5]` after all replacements, with minimum element 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int minElement(vector<int>& nums) {
        int ans = INT_MAX;

        for (int num : nums) {
            int sum = 0;

            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }

            ans = min(ans, sum);
        }

        return ans;
    }
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
- [3551. Minimum Swaps to Sort by Digit Sum](../../3501-4000/3847-minimum-swaps-to-sort-by-digit-sum/)
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3501-4000/3688-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)
- [4066. Maximum Equal Adjacent Pairs After at Most One Replacement](../../4001-4500/4420-maximum-equal-adjacent-pairs-after-at-most-one-replacement/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/)
