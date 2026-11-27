# LeetCode 3107: Minimum Operations to Make Median of Array Equal to K

**LeetCode Problem #3107 — Minimum Operations to Make Median of Array Equal to K**
Solve LeetCode Minimum Operations to Make Median of Array Equal to K using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make Median of Array Equal to K |
| LeetCode | #3107 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and a **non-negative** integer `k`. In one operation, you can increase or decrease any element by 1.

Return the **minimum** number of operations needed to make the **median** of `nums` *equal* to `k`.

The median of an array is defined as the middle element of the array when it is sorted in non-decreasing order. If there are two choices for a median, the larger of the two values is taken.

## Constraints
- `1 <= nums.length <= 2 * 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,5,6,8,5], k = 4`
- **Output:** `2`
- **Explanation:** We can subtract one from `nums[1]` and `nums[4]` to obtain `[2, 4, 6, 8, 4]`. The median of the resulting array is equal to `k`.

### Example 2
- **Input:** `nums = [2,5,6,8,5], k = 7`
- **Output:** `3`
- **Explanation:** We can add one to `nums[1]` twice and add one to `nums[2]` once to obtain `[2, 7, 7, 8, 5]`.

### Example 3
- **Input:** `nums = [1,2,3,4,5,6], k = 4`
- **Output:** `0`
- **Explanation:** The median of the array is already equal to `k`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Make Median of Array Equal to K**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,5,6,8,5], k = 4`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can subtract one from `nums[1]` and `nums[4]` to obtain `[2, 4, 6, 8, 4]`. The median of the resulting array is equal to `k`.

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
var minOperationsToMakeMedianK = function(nums, k) {
    nums.sort((a, b) => a - b);

    const mid = Math.floor(nums.length / 2);
    let operations = 0;

    if (nums[mid] > k) {
        for (let i = mid; i >= 0; i--) {
            if (nums[i] > k) {
                operations += nums[i] - k;
            } else {
                break;
            }
        }
    } else {
        for (let i = mid; i < nums.length; i++) {
            if (nums[i] < k) {
                operations += k - nums[i];
            } else {
                break;
            }
        }
    }

    return operations;
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
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [1551. Minimum Operations to Make Array Equal](../../1501-2000/1551-minimum-operations-to-make-array-equal/)
- [2111. Minimum Operations to Make the Array K-Increasing](../../2001-2500/2111-minimum-operations-to-make-the-array-k-increasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/)
