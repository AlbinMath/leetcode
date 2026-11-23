# LeetCode 1493: Longest Subarray of 1's After Deleting One Element

**LeetCode Problem #1493 — Longest Subarray of 1's After Deleting One Element**
Solve LeetCode Longest Subarray of 1's After Deleting One Element using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subarray of 1's After Deleting One Element |
| LeetCode | #1493 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary array `nums`, you should delete **one** element from it.

Return the size of the **longest non-empty subarray** containing only 1's in the resulting array. Return 0 if there is no such **subarray**.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either 0 or 1.

## Examples
### Example 1
- **Input:** `nums = [1,1,0,1]`
- **Output:** `3`
- **Explanation:** After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

### Example 2
- **Input:** `nums = [0,1,1,1,0,1,1,0,1]`
- **Output:** `5`
- **Explanation:** After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

### Example 3
- **Input:** `nums = [1,1,1]`
- **Output:** `2`
- **Explanation:** You must delete one element.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Subarray of 1's After Deleting One Element**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,0,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

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
var longestSubarray = function(nums) {
    let left = 0;
    let zeros = 0;
    let maxLength = 0;

    for (let right = 0; right < nums.length; right++) {
        if (nums[right] === 0) {
            zeros++;
        }

        while (zeros > 1) {
            if (nums[left] === 0) {
                zeros--;
            }
            left++;
        }

        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength - 1;
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
- [3830. Longest Alternating Subarray After Removing At Most One Element](../../4001-4500/4198-longest-alternating-subarray-after-removing-at-most-one-element/)
- [3872. Longest Arithmetic Sequence After Changing At Most One Element](../../4001-4500/4230-longest-arithmetic-sequence-after-changing-at-most-one-element/)
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3501-4000/3688-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)
