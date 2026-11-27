# LeetCode 3424: Minimum Cost to Make Arrays Identical

**LeetCode Problem #3424 — Minimum Cost to Make Arrays Identical**
Solve LeetCode Minimum Cost to Make Arrays Identical using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Make Arrays Identical |
| LeetCode | #3424 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `arr` and `brr` of length `n`, and an integer `k`. You can perform the following operations on `arr` *any* number of times:

Split `arr` into *any* number of **contiguous** subarrays and rearrange these subarrays in *any order*. This operation has a fixed cost of `k`. 
 
 Choose any element in `arr` and add or subtract a positive integer `x` to it. The cost of this operation is `x`.

Return the **minimum **total cost to make `arr` **equal** to `brr`.

## Constraints
- `1 <= arr.length == brr.length <= 10^5`
- `0 <= k <= 2 * 10^10`
- `-10^5 <= arr[i] <= 10^5`
- `-10^5 <= brr[i] <= 10^5`

## Examples
### Example 1
- **Input:** `arr = [-7,9,5], brr = [7,-2,-5], k = 2`
- **Output:** `13`
- **Explanation:** Split `arr` into two contiguous subarrays: `[-7]` and `[9, 5]` and rearrange them as `[9, 5, -7]`, with a cost of 2. 
 Subtract 2 from element `arr[0]`. The array becomes `[7, 5, -7]`. The cost of this operation is 2. 
 Subtract 7 from element `arr[1]`. The array becomes `[7, -2, -7]`. The cost of this operation is 7. 
 Add 2 to element `arr[2]`. The array becomes `[7, -2, -5]`. The cost of this operation is 2. 
 

 The total cost to make the arrays equal is `2 + 2 + 7 + 2 = 13`.

### Example 2
- **Input:** `arr = [2,1], brr = [2,1], k = 0`
- **Output:** `0`
- **Explanation:** Since the arrays are already equal, no operations are needed, and the total cost is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Make Arrays Identical**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [-7,9,5], brr = [7,-2,-5], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** Split `arr` into two contiguous subarrays: `[-7]` and `[9, 5]` and rearrange them as `[9, 5, -7]`, with a cost of 2. 
 Subtract 2 from element `arr[0]`. The array becomes `[7, 5, -7]`. The cost of this operation is 2. 
 Subtract 7 from element `arr[1]`. The array becomes `[7, -2, -7]`. The cost of this operation is 7. 
 Add 2 to element `arr[2]`. The array becomes `[7, -2, -5]`. The cost of this operation is 2. 
 

 The total cost to make the arrays equal is `2 + 2 + 7 + 2 = 13`.

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
var minCost = function(arr, brr, k) {
    const n = arr.length;
    let directCost = 0;

    for (let i = 0; i < n; i++) {
        directCost += Math.abs(arr[i] - brr[i]);
    }
    const sortedArr = [...arr].sort((a, b) => a - b);
    const sortedBrr = [...brr].sort((a, b) => a - b);

    let rearrangedCost = k;

    for (let i = 0; i < n; i++) {
        rearrangedCost += Math.abs(sortedArr[i] - sortedBrr[i]);
    }

    return Math.min(directCost, rearrangedCost);
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
- [2499. Minimum Total Cost to Make Arrays Unequal](../../2001-2500/2499-minimum-total-cost-to-make-arrays-unequal/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2448. Minimum Cost to Make Array Equal](../../2001-2500/2448-minimum-cost-to-make-array-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/)
