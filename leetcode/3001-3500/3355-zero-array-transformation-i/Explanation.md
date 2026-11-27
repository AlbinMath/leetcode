# LeetCode 3355: Zero Array Transformation I

**LeetCode Problem #3355 — Zero Array Transformation I**
Solve LeetCode Zero Array Transformation I using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Zero Array Transformation I |
| LeetCode | #3355 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and a 2D array `queries`, where `queries[i] = [l_i, r_i]`.

For each `queries[i]`:

Select a subset of indices within the range `[l_i, r_i]` in `nums`. 
 Decrement the values at the selected indices by 1.

A **Zero Array** is an array where all elements are equal to 0.

Return `true` if it is *possible* to transform `nums` into a **Zero Array **after processing all the queries sequentially, otherwise return `false`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= l_i <= r_i < nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,0,1], queries = [[0,2]]`
- **Output:** `true`

### Example 2
- **Input:** `nums = [4,3,2,1], queries = [[1,3],[0,2]]`
- **Output:** `false`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Zero Array Transformation I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,0,1], queries = [[0,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
var isZeroArray = function(nums, queries) {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);
    for (const [l, r] of queries) {
        diff[l]++;
        diff[r + 1]--;
    }
    let operations = 0;
    for (let i = 0; i < n; i++) {
        operations += diff[i];
        if (operations < nums[i]) {
            return false;
        }
    }
    return true;
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
- [3356. Zero Array Transformation II](../../3001-3500/3356-zero-array-transformation-ii/)
- [3362. Zero Array Transformation III](../../3001-3500/3362-zero-array-transformation-iii/)
- [2626. Array Reduce Transformation](../../2501-3000/2626-array-reduce-transformation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/zero-array-transformation-i/)
