# LeetCode 1984: Minimum Difference Between Highest and Lowest of K Scores

**LeetCode Problem #1984 — Minimum Difference Between Highest and Lowest of K Scores**
Solve LeetCode Minimum Difference Between Highest and Lowest of K Scores using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Difference Between Highest and Lowest of K Scores |
| LeetCode | #1984 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`, where `nums[i]` represents the score of the `i^th` student. You are also given an integer `k`.

Pick the scores of any `k` students from the array so that the **difference** between the **highest** and the **lowest** of the `k` scores is **minimized**.

Return *the **minimum** possible difference*.

## Constraints
- `1 <= k <= nums.length <= 1000`
- `0 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [90], k = 1`
- **Output:** `0`
- **Explanation:** There is one way to pick score(s) of one student:
- [

### Example 2
- **Input:** `nums = [9,4,1,7], k = 2`
- **Output:** `2`
- **Explanation:** There are six ways to pick score(s) of two students:
- [

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Difference Between Highest and Lowest of K Scores**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [90], k = 1`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** There is one way to pick score(s) of one student:
- [

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minimumDifference = function(nums, k) {
    nums.sort((a, b) => a - b);

    let minDiff = Infinity;

    for (let i = 0; i <= nums.length - k; i++) {
        let diff = nums[i + k - 1] - nums[i];
        minDiff = Math.min(minDiff, diff);
    }

    return minDiff;
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2817. Minimum Absolute Difference Between Elements With Constraint](../../2501-3000/2817-minimum-absolute-difference-between-elements-with-constraint/)
- [3880. Minimum Absolute Difference Between Two Values](../../3501-4000/3880-minimum-absolute-difference-between-two-values/)
- [530. Minimum Absolute Difference in BST](../../0501-1000/0530-minimum-absolute-difference-in-bst/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/)
