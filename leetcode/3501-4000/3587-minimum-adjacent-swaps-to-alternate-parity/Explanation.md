# LeetCode 3587: Minimum Adjacent Swaps to Alternate Parity

**LeetCode Problem #3587 — Minimum Adjacent Swaps to Alternate Parity**
Solve LeetCode Minimum Adjacent Swaps to Alternate Parity using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Adjacent Swaps to Alternate Parity |
| LeetCode | #3587 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` of **distinct** integers.

In one operation, you can swap any two **adjacent** elements in the array.

An arrangement of the array is considered **valid** if the parity of adjacent elements **alternates**, meaning every pair of neighboring elements consists of one even and one odd number.

Return the **minimum** number of adjacent swaps required to transform `nums` into any valid arrangement.

If it is impossible to rearrange `nums` such that no two adjacent elements have the same parity, return `-1`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- All elements in `nums` are **distinct**.

## Examples
### Example 1
- **Input:** `nums = [2,4,6,5,7]`
- **Output:** `3`
- **Explanation:** Swapping 5 and 6, the array becomes `[2,4,5,6,7]` 

 Swapping 5 and 4, the array becomes `[2,5,4,6,7]` 

 Swapping 6 and 7, the array becomes `[2,5,4,7,6]`. The array is now a valid arrangement. Thus, the answer is 3.

### Example 2
- **Input:** `nums = [2,4,5,7]`
- **Output:** `1`
- **Explanation:** By swapping 4 and 5, the array becomes `[2,5,4,7]`, which is a valid arrangement. Thus, the answer is 1.

### Example 3
- **Input:** `nums = [1,2,3]`
- **Output:** `0`
- **Explanation:** The array is already a valid arrangement. Thus, no operations are needed.

### Example 4
- **Input:** `nums = [4,5,6,8]`
- **Output:** `-1`
- **Explanation:** No valid arrangement is possible. Thus, the answer is -1.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Adjacent Swaps to Alternate Parity**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4,6,5,7]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Swapping 5 and 6, the array becomes `[2,4,5,6,7]` 

 Swapping 5 and 4, the array becomes `[2,5,4,6,7]` 

 Swapping 6 and 7, the array becomes `[2,5,4,7,6]`. The array is now a valid arrangement. Thus, the answer is 3.

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
var minSwaps = function(nums) {
    const even = [];
    const odd = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % 2 === 0) {
            even.push(i);
        } else {
            odd.push(i);
        }
    }
    if (Math.abs(even.length - odd.length) > 1) {
        return -1;
    }
    function calculateCost(indices) {
        let swaps = 0;

        for (let i = 0; i < indices.length; i++) {
            swaps += Math.abs(indices[i] - 2 * i);
        }

        return swaps;
    }
    if (even.length > odd.length) {
        return calculateCost(even);
    }
    if (odd.length > even.length) {
        return calculateCost(odd);
    }
    return Math.min(
        calculateCost(even),
        calculateCost(odd)
    );
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
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1505-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../../1501-2000/1703-minimum-adjacent-swaps-for-k-consecutive-ones/)
- [1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number](../../1501-2000/1850-minimum-adjacent-swaps-to-reach-the-kth-smallest-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/)
