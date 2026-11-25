# LeetCode 3432: Count Partitions with Even Sum Difference

**LeetCode Problem #3432 — Count Partitions with Even Sum Difference**
Solve LeetCode Count Partitions with Even Sum Difference using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Partitions with Even Sum Difference |
| LeetCode | #3432 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

A **partition** is defined as an index `i` where `0 <= i < n - 1`, splitting the array into two **non-empty** subarrays such that:

Left subarray contains indices `[0, i]`. 
 Right subarray contains indices `[i + 1, n - 1]`.

Return the number of **partitions** where the **difference** between the **sum** of the left and right subarrays is **even**.

## Constraints
- `2 <= n == nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [10,10,3,7,6]`
- **Output:** `4`
- **Explanation:** The 4 partitions are: 

 
 `[10]`, `[10, 3, 7, 6]` with a sum difference of `10 - 26 = -16`, which is even. 
 `[10, 10]`, `[3, 7, 6]` with a sum difference of `20 - 16 = 4`, which is even. 
 `[10, 10, 3]`, `[7, 6]` with a sum difference of `23 - 13 = 10`, which is even. 
 `[10, 10, 3, 7]`, `[6]` with a sum difference of `30 - 6 = 24`, which is even.

### Example 2
- **Input:** `nums = [1,2,2]`
- **Output:** `0`
- **Explanation:** No partition results in an even sum difference.

### Example 3
- **Input:** `nums = [2,4,6,8]`
- **Output:** `3`
- **Explanation:** All partitions result in an even sum difference.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Partitions with Even Sum Difference**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,10,3,7,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The 4 partitions are: 

 
 `[10]`, `[10, 3, 7, 6]` with a sum difference of `10 - 26 = -16`, which is even. 
 `[10, 10]`, `[3, 7, 6]` with a sum difference of `20 - 16 = 4`, which is even. 
 `[10, 10, 3]`, `[7, 6]` with a sum difference of `23 - 13 = 10`, which is even. 
 `[10, 10, 3, 7]`, `[6]` with a sum difference of `30 - 6 = 24`, which is even.

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
var countPartitions = function(nums) {
    const totalSum = nums.reduce((sum, num) => sum + num, 0);

    if (totalSum % 2 === 0) {
        return nums.length - 1;
    }

    return 0;
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
- [3578. Count Partitions With Max-Min Difference at Most K](../../3501-4000/3578-count-partitions-with-max-min-difference-at-most-k/)
- [2180. Count Integers With Even Digit Sum](../../2001-2500/2180-count-integers-with-even-digit-sum/)
- [3910. Count Connected Subgraphs with Even Node Sum](../../3501-4000/3910-count-connected-subgraphs-with-even-node-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-partitions-with-even-sum-difference/)
