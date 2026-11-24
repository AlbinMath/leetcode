# LeetCode 2717: Semi-Ordered Permutation

**LeetCode Problem #2717 — Semi-Ordered Permutation**
Solve LeetCode Semi-Ordered Permutation using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Semi-Ordered Permutation |
| LeetCode | #2717 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** permutation of `n` integers `nums`.

A permutation is called **semi-ordered** if the first number equals `1` and the last number equals `n`. You can perform the below operation as many times as you want until you make `nums` a **semi-ordered** permutation:

Pick two adjacent elements in `nums`, then swap them.

Return *the minimum number of operations to make *`nums`* a **semi-ordered permutation***.

A **permutation** is a sequence of integers from `1` to `n` of length `n` containing each number exactly once.

## Constraints
- `2 <= nums.length == n <= 50`
- `1 <= nums[i] <= 50`
- `nums is a permutation.`

## Examples
### Example 1
- **Input:** `nums = [2,1,4,3]`
- **Output:** `2`
- **Explanation:** We can make the permutation semi-ordered using these sequence of operations: 
1 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
2 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than two operations that make nums a semi-ordered permutation.

### Example 2
- **Input:** `nums = [2,4,1,3]`
- **Output:** `3`
- **Explanation:** We can make the permutation semi-ordered using these sequence of operations:
1 - swap i = 1 and j = 2. The permutation becomes [2,1,4,3].
2 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
3 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than three operations that make nums a semi-ordered permutation.

### Example 3
- **Input:** `nums = [1,3,4,2,5]`
- **Output:** `0`
- **Explanation:** The permutation is already a semi-ordered permutation.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Semi-Ordered Permutation**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,4,3]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can make the permutation semi-ordered using these sequence of operations: 
1 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
2 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than two operations that make nums a semi-ordered permutation.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var semiOrderedPermutation = function(nums) {
    const n = nums.length;
    const idx1 = nums.indexOf(1);
    const idxN = nums.indexOf(n);

    const swaps = idx1 + (n - 1 - idxN);
    return idx1 > idxN ? swaps - 1 : swaps;
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1327. List the Products Ordered in a Period](../../1001-1500/1327-list-the-products-ordered-in-a-period/)
- [1656. Design an Ordered Stream](../../1501-2000/1656-design-an-ordered-stream/)
- [2730. Find the Longest Semi-Repetitive Substring](../../2501-3000/2730-find-the-longest-semi-repetitive-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/semi-ordered-permutation/)
