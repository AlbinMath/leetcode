# LeetCode 2626: Array Reduce Transformation

**LeetCode Problem #2626 — Array Reduce Transformation**
Solve LeetCode Array Reduce Transformation using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Array Reduce Transformation |
| LeetCode | #2626 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, a reducer function `fn`, and an initial value `init`, return the final result obtained by executing the `fn` function on each element of the array, sequentially, passing in the return value from the calculation on the preceding element.

This result is achieved through the following operations: `val = fn(init, nums[0]), val = fn(val, nums[1]), val = fn(val, nums[2]), ...` until every element in the array has been processed. The ultimate value of `val` is then returned.

If the length of the array is 0, the function should return `init`.

Please solve it without using the built-in `Array.reduce` method.

## Constraints
- `0 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`
- `0 <= init <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr; }
init = 0`
- **Output:** `10`
- **Explanation:** initially, the value is init=0.
(0) + nums[0] = 1
(1) + nums[1] = 3
(3) + nums[2] = 6
(6) + nums[3] = 10
The final answer is 10.

### Example 2
- **Input:** `nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr * curr; }
init = 100`
- **Output:** `130`
- **Explanation:** initially, the value is init=100.
(100) + nums[0] * nums[0] = 101
(101) + nums[1] * nums[1] = 105
(105) + nums[2] * nums[2] = 114
(114) + nums[3] * nums[3] = 130
The final answer is 130.

### Example 3
- **Input:** `nums = []
fn = function sum(accum, curr) { return 0; }
init = 25`
- **Output:** `25`
- **Explanation:** For empty arrays, the answer is always init.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Initialize an accumulator with `init`. Iterate through the array, updating `accumulator = fn(accumulator, arr[i], i)` at each step. Return the final accumulator value.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr; }
init = 0`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** initially, the value is init=0.
(0) + nums[0] = 1
(1) + nums[1] = 3
(3) + nums[2] = 6
(6) + nums[3] = 10
The final answer is 10.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function reduce(
    nums: number[],
    fn: (accum: number, curr: number) => number,
    init: number
): number {
    let result = init;

    for (let i = 0; i < nums.length; i++) {
        result = fn(result, nums[i]);
    }

    return result;
}
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
- [3690. Split and Merge Array Transformation](../../3501-4000/3690-split-and-merge-array-transformation/)
- [3824. Minimum K to Reduce Array Within Limit](../../3501-4000/3824-minimum-k-to-reduce-array-within-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/array-reduce-transformation/)
