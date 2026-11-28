# LeetCode 3264: Final Array State After K Multiplication Operations I

**LeetCode Problem #3264 — Final Array State After K Multiplication Operations I**
Solve LeetCode Final Array State After K Multiplication Operations I using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Final Array State After K Multiplication Operations I |
| LeetCode | #3264 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

You need to perform `k` operations on `nums`. In each operation:

Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first**. 
 Replace the selected minimum value `x` with `x * multiplier`.

Return an integer array denoting the *final state* of `nums` after performing all `k` operations.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= 10`
- `1 <= multiplier <= 5`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,5,6], k = 5, multiplier = 2`
- **Output:** `[8,4,6,5,6]`
- **Explanation:** Operation 
 Result 
 
 
 After operation 1 
 [2, 2, 3, 5, 6] 
 
 
 After operation 2 
 [4, 2, 3, 5, 6] 
 
 
 After operation 3 
 [4, 4, 3, 5, 6] 
 
 
 After operation 4 
 [4, 4, 6, 5, 6] 
 
 
 After operation 5 
 [8, 4, 6, 5, 6]

### Example 2
- **Input:** `nums = [1,2], k = 3, multiplier = 4`
- **Output:** `[16,8]`
- **Explanation:** Operation 
 Result 
 
 
 After operation 1 
 [4, 2] 
 
 
 After operation 2 
 [4, 8] 
 
 
 After operation 3 
 [16, 8]

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Final Array State After K Multiplication Operations I**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,5,6], k = 5, multiplier = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[8,4,6,5,6]`.
4. **Verification:** Operation 
 Result 
 
 
 After operation 1 
 [2, 2, 3, 5, 6] 
 
 
 After operation 2 
 [4, 2, 3, 5, 6] 
 
 
 After operation 3 
 [4, 4, 3, 5, 6] 
 
 
 After operation 4 
 [4, 4, 6, 5, 6] 
 
 
 After operation 5 
 [8, 4, 6, 5, 6]

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
var getFinalState = function(nums, k, multiplier) {
    const n = nums.length;
    const heap = Array.from({ length: n }, (_, i) => i);

    const less = (a, b) =>
        nums[heap[a]] !== nums[heap[b]]
            ? nums[heap[a]] < nums[heap[b]]
            : heap[a] < heap[b];

    const siftDown = (idx) => {
        while (true) {
            let smallest = idx;
            const left = (idx << 1) + 1;
            const right = left + 1;
            if (left < n && less(left, smallest)) smallest = left;
            if (right < n && less(right, smallest)) smallest = right;
            if (smallest === idx) break;
            [heap[idx], heap[smallest]] = [heap[smallest], heap[idx]];
            idx = smallest;
        }
    };

    for (let i = (n >> 1) - 1; i >= 0; i--) {
        siftDown(i);
    }

    for (let op = 0; op < k; op++) {
        const minIdx = heap[0];
        nums[minIdx] *= multiplier;
        siftDown(0);
    }

    return nums;
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
- [3266. Final Array State After K Multiplication Operations II](../../3001-3500/3266-final-array-state-after-k-multiplication-operations-ii/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [2111. Minimum Operations to Make the Array K-Increasing](../../2001-2500/2111-minimum-operations-to-make-the-array-k-increasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/)
