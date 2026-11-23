# LeetCode 327: Count of Range Sum

**LeetCode Problem #327 — Count of Range Sum**
Solve LeetCode Count of Range Sum using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count of Range Sum |
| LeetCode | #327 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and two integers `lower` and `upper`, return *the number of range sums that lie in* `[lower, upper]` *inclusive*.

Range sum `S(i, j)` is defined as the sum of the elements in `nums` between indices `i` and `j` inclusive, where `i <= j`.

## Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `-10^5 <= lower <= upper <= 10^5`
- The answer is **guaranteed** to fit in a **32-bit** integer.

## Examples
### Example 1
- **Input:** `nums = [-2,5,-1], lower = -2, upper = 2`
- **Output:** `3`
- **Explanation:** The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.

### Example 2
- **Input:** `nums = [0], lower = 0, upper = 0`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count of Range Sum**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-2,5,-1], lower = -2, upper = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.

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
var countRangeSum = function(nums, lower, upper) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    const temp = new Array(n + 1);

    function mergeSort(left, right) {
        if (left >= right) return 0;

        const mid = Math.floor((left + right) / 2);
        let count = mergeSort(left, mid) +
                    mergeSort(mid + 1, right);

        let low = mid + 1;
        let high = mid + 1;

        // Count valid ranges crossing the midpoint
        for (let i = left; i <= mid; i++) {
            while (
                low <= right &&
                prefix[low] - prefix[i] < lower
            ) {
                low++;
            }

            while (
                high <= right &&
                prefix[high] - prefix[i] <= upper
            ) {
                high++;
            }

            count += high - low;
        }

        // Merge both sorted halves
        let i = left;
        let j = mid + 1;
        let k = left;

        while (i <= mid && j <= right) {
            if (prefix[i] <= prefix[j]) {
                temp[k++] = prefix[i++];
            } else {
                temp[k++] = prefix[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = prefix[i++];
        }

        while (j <= right) {
            temp[k++] = prefix[j++];
        }

        for (let p = left; p <= right; p++) {
            prefix[p] = temp[p];
        }

        return count;
    }

    return mergeSort(0, n);
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
- [1523. Count Odd Numbers in an Interval Range](../../1501-2000/1630-count-odd-numbers-in-an-interval-range/)
- [1803. Count Pairs With XOR in a Range](../../1501-2000/1907-count-pairs-with-xor-in-a-range/)
- [1925. Count Square Sum Triples](../../2001-2500/2037-count-square-sum-triples/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-of-range-sum/)
