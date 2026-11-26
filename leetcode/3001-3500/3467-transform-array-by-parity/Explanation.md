# LeetCode 3467: Transform Array by Parity

**LeetCode Problem #3467 — Transform Array by Parity**
Solve LeetCode Transform Array by Parity using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Transform Array by Parity |
| LeetCode | #3467 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. Transform `nums` by performing the following operations in the **exact** order specified:

Replace each even number with 0. 
 Replace each odd numbers with 1. 
 Sort the modified array in **non-decreasing** order.

Return the resulting array after performing these operations.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [4,3,2,1]`
- **Output:** `[0,0,1,1]`
- **Explanation:** Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, `nums = [0, 1, 0, 1]`. 
 After sorting `nums` in non-descending order, `nums = [0, 0, 1, 1]`.

### Example 2
- **Input:** `nums = [1,5,1,4,2]`
- **Output:** `[0,0,1,1,1]`
- **Explanation:** Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, `nums = [1, 1, 1, 0, 0]`. 
 After sorting `nums` in non-descending order, `nums = [0, 0, 1, 1, 1]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Transform Array by Parity**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,3,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,0,1,1]`.
4. **Verification:** Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, `nums = [0, 1, 0, 1]`. 
 After sorting `nums` in non-descending order, `nums = [0, 0, 1, 1]`.

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
var transformArray = function(nums) {
    return nums
        .map(num => num % 2 === 0 ? 0 : 1)
        .sort((a, b) => a - b);
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
- [1331. Rank Transform of an Array](../../1001-1500/1331-rank-transform-of-an-array/)
- [2635. Apply Transform Over Each Element in Array](../../2501-3000/2635-apply-transform-over-each-element-in-array/)
- [3896. Minimum Operations to Transform Array into Alternating Prime](../../3501-4000/3896-minimum-operations-to-transform-array-into-alternating-prime/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/transform-array-by-parity/)
