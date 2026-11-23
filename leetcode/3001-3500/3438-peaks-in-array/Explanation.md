# LeetCode 3187: Peaks in Array

**LeetCode Problem #3187 — Peaks in Array**
Solve LeetCode Peaks in Array using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Peaks in Array |
| LeetCode | #3187 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **peak** in an array `arr` is an element that is **greater** than its previous and next element in `arr`.

You are given an integer array `nums` and a 2D integer array `queries`.

You have to process queries of two types:

`queries[i] = [1, l_i, r_i]`, determine the count of **peak** elements in the subarray `nums[l_i..r_i]`. 
 `queries[i] = [2, index_i, val_i]`, change `nums[index_i]` to ` val_i `.

Return an array `answer` containing the results of the queries of the first type in order.

**Notes:**

The **first** and the **last** element of an array or a subarray **cannot** be a peak.

## Constraints
- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i][0] == 1` or `queries[i][0] == 2`
- For all `i` that:
 
 `queries[i][0] == 1`: `0 <= queries[i][1] <= queries[i][2] <= nums.length - 1`
- `queries[i][0] == 2`: `0 <= queries[i][1] <= nums.length - 1`, `1 <= queries[i][2] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]`
- **Output:** `[0]`
- **Explanation:** First query: We change `nums[3]` to 4 and `nums` becomes `[3,1,4,4,5]`. 

 Second query: The number of peaks in the `[3,1,4,4,5]` is 0.

### Example 2
- **Input:** `nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]`
- **Output:** `[0,1]`
- **Explanation:** First query: `nums[2]` should become 4, but it is already set to 4. 

 Second query: The number of peaks in the `[4,1,4]` is 0. 

 Third query: The second 4 is a peak in the `[4,1,4,2,1]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Peaks in Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0]`.
4. **Verification:** First query: We change `nums[3]` to 4 and `nums` becomes `[3,1,4,4,5]`. 

 Second query: The number of peaks in the `[3,1,4,4,5]` is 0.

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
var countOfPeaks = function(nums, queries) {
    const n = nums.length;
    const bit = new Array(n + 1).fill(0);

    function isPeak(i) {
        return i > 0 &&
               i < n - 1 &&
               nums[i] > nums[i - 1] &&
               nums[i] > nums[i + 1];
    }

    function update(i, delta) {
        for (i++; i <= n; i += i & -i) {
            bit[i] += delta;
        }
    }

    function query(i) {
        let sum = 0;

        for (i++; i > 0; i -= i & -i) {
            sum += bit[i];
        }

        return sum;
    }

    function rangeSum(left, right) {
        if (left > right) return 0;
        return query(right) - (left > 0 ? query(left - 1) : 0);
    }

    // Initialize peak indicators.
    for (let i = 1; i < n - 1; i++) {
        if (isPeak(i)) update(i, 1);
    }

    const answer = [];

    for (const [type, a, b] of queries) {
        if (type === 1) {
            // Endpoints of the queried subarray cannot be peaks.
            answer.push(rangeSum(a + 1, b - 1));
        } else {
            const index = a;
            const value = b;

            // Only these positions can change peak status.
            for (let i = Math.max(1, index - 1);
                 i <= Math.min(n - 2, index + 1);
                 i++) {
                if (isPeak(i)) update(i, -1);
            }

            nums[index] = value;

            for (let i = Math.max(1, index - 1);
                 i <= Math.min(n - 2, index + 1);
                 i++) {
                if (isPeak(i)) update(i, 1);
            }
        }
    }

    return answer;
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
- [4017. Peaks in Array II](../../4001-4500/4336-peaks-in-array-ii/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/peaks-in-array/)
