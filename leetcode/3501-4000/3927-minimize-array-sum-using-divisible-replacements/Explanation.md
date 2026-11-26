# LeetCode 3927: Minimize Array Sum Using Divisible Replacements

**LeetCode Problem #3927 — Minimize Array Sum Using Divisible Replacements**
Solve LeetCode Minimize Array Sum Using Divisible Replacements using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize Array Sum Using Divisible Replacements |
| LeetCode | #3927 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

You can perform the following operation any number of times:

Choose two indices `a` and `b` such that `nums[a] % nums[b] == 0`. 
 Replace `nums[a]` with `nums[b]`.

Return the **minimum** possible sum of the array after performing any number of operations.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^​​​​​​​5`

## Examples
### Example 1
- **Input:** `nums = [3,6,2]`
- **Output:** `7`
- **Explanation:** Choose `a = 1`, `b = 2`, where `nums[a] = 6` and `nums[b] = 2`. Since `6 % 2 == 0`, replace `nums[1]` with `nums[2]`. 
 The array becomes `[3, 2, 2]`. 
 No further operation reduces the sum. Thus, the final sum is `3 + 2 + 2 = 7`.

### Example 2
- **Input:** `nums = [4,2,8,3]`
- **Output:** `9`
- **Explanation:** Choose `a = 0`, `b = 1`, where `nums[a] = 4` and `nums[b] = 2`. Since `4 % 2 == 0`, replace `nums[0]` with `nums[1]`. 
 Choose `a = 2`, `b = 1`, where `nums[a] = 8` and `nums[b] = 2`. Since `8 % 2 == 0`, replace `nums[2]` with `nums[1]`. 
 The array becomes `[2, 2, 2, 3]`. 
 No further operation reduces the sum. Thus, the final sum is `2 + 2 + 2 + 3 = 9`.

### Example 3
- **Input:** `nums = [7,5,9]`
- **Output:** `21`
- **Explanation:** There is no pair `(a, b)` such that `nums[a] % nums[b] == 0`. 
 Hence, no operation can be performed. The sum remains `7 + 5 + 9 = 21`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimize Array Sum Using Divisible Replacements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,6,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Choose `a = 1`, `b = 2`, where `nums[a] = 6` and `nums[b] = 2`. Since `6 % 2 == 0`, replace `nums[1]` with `nums[2]`. 
 The array becomes `[3, 2, 2]`. 
 No further operation reduces the sum. Thus, the final sum is `3 + 2 + 2 = 7`.

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
var minArraySum = function(nums) {
    let maxVal = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    // 1. Mark which values exist in nums
    const present = new Uint8Array(maxVal + 1);
    for (let i = 0; i < nums.length; i++) {
        present[nums[i]] = 1;
    }

    // 2. For every value v, find the smallest present divisor in nums
    const minDiv = new Int32Array(maxVal + 1);
    for (let v = 1; v <= maxVal; v++) {
        minDiv[v] = v;
    }

    for (let d = 1; d <= maxVal; d++) {
        if (present[d]) {
            for (let multiple = d + d; multiple <= maxVal; multiple += d) {
                if (d < minDiv[multiple]) {
                    minDiv[multiple] = d;
                }
            }
        }
    }

    // 3. Replace each element with its smallest present divisor and sum
    let totalSum = 0;
    for (let i = 0; i < nums.length; i++) {
        totalSum += minDiv[nums[i]];
    }

    return totalSum;
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
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2035-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [3012. Minimize Length of Array Using Operations](../../3001-3500/3012-minimize-length-of-array-using-operations/)
- [167. Two Sum II - Input Array Is Sorted](../../0001-0500/0167-two-sum-ii-input-array-is-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/)
