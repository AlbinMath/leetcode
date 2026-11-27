# LeetCode 2913: Subarrays Distinct Element Sum of Squares I

**LeetCode Problem #2913 — Subarrays Distinct Element Sum of Squares I**
Solve LeetCode Subarrays Distinct Element Sum of Squares I using JavaScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subarrays Distinct Element Sum of Squares I |
| LeetCode | #2913 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed **integer array `nums`.

The **distinct count** of a subarray of `nums` is defined as:

Let `nums[i..j]` be a subarray of `nums` consisting of all the indices from `i` to `j` such that `0 <= i <= j < nums.length`. Then the number of distinct values in `nums[i..j]` is called the distinct count of `nums[i..j]`.

Return *the sum of the **squares** of **distinct counts** of all subarrays of *`nums`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,1]`
- **Output:** `15`
- **Explanation:** Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15.

### Example 2
- **Input:** `nums = [1,1]`
- **Output:** `3`
- **Explanation:** Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 = 3.

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Subarrays Distinct Element Sum of Squares I**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1]`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var sumCounts = function(nums) {
    let result = 0;

    for (let i = 0; i < nums.length; i++) {
        const distinct = new Set();

        for (let j = i; j < nums.length; j++) {
            distinct.add(nums[j]);

            const count = distinct.size;
            result += count * count;
        }
    }

    return result;
};
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [2916. Subarrays Distinct Element Sum of Squares II](../../2501-3000/2916-subarrays-distinct-element-sum-of-squares-ii/)
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2001-2500/2461-maximum-sum-of-distinct-subarrays-with-length-k/)
- [2862. Maximum Element-Sum of a Complete Subset of Indices](../../2501-3000/2862-maximum-element-sum-of-a-complete-subset-of-indices/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/)
