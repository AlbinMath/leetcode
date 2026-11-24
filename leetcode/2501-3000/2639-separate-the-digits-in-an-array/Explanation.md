# LeetCode 2553: Separate the Digits in an Array

**LeetCode Problem #2553 — Separate the Digits in an Array**
Solve LeetCode Separate the Digits in an Array using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Separate the Digits in an Array |
| LeetCode | #2553 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of positive integers `nums`, return *an array *`answer`* that consists of the digits of each integer in *`nums`* after separating them in **the same order** they appear in *`nums`.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer `10921`, the separation of its digits is `[1,0,9,2,1]`.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [13,25,83,77]`
- **Output:** `[1,3,2,5,8,3,7,7]`
- **Explanation:** - The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.

### Example 2
- **Input:** `nums = [7,1,3,9]`
- **Output:** `[7,1,3,9]`
- **Explanation:** The separation of each integer in nums is itself.
answer = [7,1,3,9].

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
For each number, extract its digits (by converting to string or using modulo) and append them to the result array in order.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [13,25,83,77]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,2,5,8,3,7,7]`.
4. **Verification:** - The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.

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
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> ans;

        for (int num : nums) {
            vector<int> digits;

            while (num > 0) {
                digits.push_back(num % 10);
                num /= 10;
            }

            reverse(digits.begin(), digits.end());

            for (int digit : digits) {
                ans.push_back(digit);
            }
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
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/separate-the-digits-in-an-array/)
