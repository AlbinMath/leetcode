# LeetCode 324: Wiggle Sort II

**LeetCode Problem #324 — Wiggle Sort II**
Solve LeetCode Wiggle Sort II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Wiggle Sort II |
| LeetCode | #324 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`.

You may assume the input array always has a valid answer.

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`
- It is guaranteed that there will be an answer for the given input `nums`.

## Examples
### Example 1
- **Input:** `nums = [1,5,1,1,6,4]`
- **Output:** `[1,6,1,5,1,4]`
- **Explanation:** [1,4,1,5,1,6] is also accepted.

### Example 2
- **Input:** `nums = [1,3,2,2,3,1]`
- **Output:** `[2,3,1,3,1,2]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Wiggle Sort II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,5,1,1,6,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,6,1,5,1,4]`.
4. **Verification:** [1,4,1,5,1,6] is also accepted.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort = function(nums) {
    const arr = [...nums].sort((a, b) => a - b);
    const n = nums.length;
    let mid = Math.floor((n - 1) / 2);
    let end = n - 1;

    for (let i = 0; i < n; i++) {
        nums[i] = i % 2 === 0 ? arr[mid--] : arr[end--];
    }
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [376. Wiggle Subsequence](../../0001-0500/0376-wiggle-subsequence/)
- [75. Sort Colors](../../0001-0500/0075-sort-colors/)
- [147. Insertion Sort List](../../0001-0500/0147-insertion-sort-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/wiggle-sort-ii/)
