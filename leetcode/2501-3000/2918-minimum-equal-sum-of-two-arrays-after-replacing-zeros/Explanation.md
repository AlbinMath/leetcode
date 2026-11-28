# LeetCode 2918: Minimum Equal Sum of Two Arrays After Replacing Zeros

**LeetCode Problem #2918 — Minimum Equal Sum of Two Arrays After Replacing Zeros**
Solve LeetCode Minimum Equal Sum of Two Arrays After Replacing Zeros using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Equal Sum of Two Arrays After Replacing Zeros |
| LeetCode | #2918 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two arrays `nums1` and `nums2` consisting of positive integers.

You have to replace **all** the `0`'s in both arrays with **strictly** positive integers such that the sum of elements of both arrays becomes **equal**.

Return *the **minimum** equal sum you can obtain, or *`-1`* if it is impossible*.

## Constraints
- `1 <= nums1.length, nums2.length <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums1 = [3,2,0,1,0], nums2 = [6,5,0]`
- **Output:** `12`
- **Explanation:** We can replace 0's in the following way:
- Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.

### Example 2
- **Input:** `nums1 = [2,0,2,0], nums2 = [1,4]`
- **Output:** `-1`
- **Explanation:** It is impossible to make the sum of both arrays equal.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Equal Sum of Two Arrays After Replacing Zeros**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [3,2,0,1,0], nums2 = [6,5,0]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** We can replace 0's in the following way:
- Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.

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
var minSum = function(nums1, nums2) {
    let sum1 = 0;
    let sum2 = 0;

    let zeros1 = 0;
    let zeros2 = 0;

    for (let num of nums1) {
        sum1 += num;

        if (num === 0) zeros1++;
    }

    for (let num of nums2) {
        sum2 += num;

        if (num === 0) zeros2++;
    }

    let minSum1 = sum1 + zeros1;
    let minSum2 = sum2 + zeros2;

    if (zeros1 > 0 && zeros2 > 0) {
        return Math.max(minSum1, minSum2);
    }

    if (zeros1 > 0) {
        return minSum1 <= sum2 ? sum2 : -1;
    }

    if (zeros2 > 0) {
        return minSum2 <= sum1 ? sum1 : -1;
    }

    return sum1 === sum2 ? sum1 : -1;
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
- [1879. Minimum XOR Sum of Two Arrays](../../1501-2000/1879-minimum-xor-sum-of-two-arrays/)
- [1775. Equal Sum Arrays With Minimum Number of Operations](../../1501-2000/1775-equal-sum-arrays-with-minimum-number-of-operations/)
- [599. Minimum Index Sum of Two Lists](../../0501-1000/0599-minimum-index-sum-of-two-lists/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/)
