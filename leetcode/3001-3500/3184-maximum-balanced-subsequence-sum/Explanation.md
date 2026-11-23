# LeetCode 2926: Maximum Balanced Subsequence Sum

**LeetCode Problem #2926 — Maximum Balanced Subsequence Sum**
Solve LeetCode Maximum Balanced Subsequence Sum using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Balanced Subsequence Sum |
| LeetCode | #2926 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`.

A **subsequence** of `nums` having length `k` and consisting of **indices** `i_0 < i_1 < ... < i_k-1` is **balanced** if the following holds:

`nums[i_j] - nums[i_j-1] >= i_j - i_j-1`, for every `j` in the range `[1, k - 1]`.

A **subsequence** of `nums` having length `1` is considered balanced.

Return *an integer denoting the **maximum** possible **sum of elements** in a **balanced** subsequence of *`nums`.

A **subsequence** of an array is a new **non-empty** array that is formed from the original array by deleting some (**possibly none**) of the elements without disturbing the relative positions of the remaining elements.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,3,5,6]`
- **Output:** `14`
- **Explanation:** In this example, the subsequence [3,5,6] consisting of indices 0, 2, and 3 can be selected.
nums[2] - nums[0] >= 2 - 0.
nums[3] - nums[2] >= 3 - 2.
Hence, it is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
The subsequence consisting of indices 1, 2, and 3 is also valid.
It can be shown that it is not possible to get a balanced subsequence with a sum greater than 14.

### Example 2
- **Input:** `nums = [5,-1,-3,8]`
- **Output:** `13`
- **Explanation:** In this example, the subsequence [5,8] consisting of indices 0 and 3 can be selected.
nums[3] - nums[0] >= 3 - 0.
Hence, it is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
It can be shown that it is not possible to get a balanced subsequence with a sum greater than 13.

### Example 3
- **Input:** `nums = [-2,-1]`
- **Output:** `-1`
- **Explanation:** In this example, the subsequence [-1] can be selected.
It is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Balanced Subsequence Sum**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,3,5,6]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** In this example, the subsequence [3,5,6] consisting of indices 0, 2, and 3 can be selected.
nums[2] - nums[0] >= 2 - 0.
nums[3] - nums[2] >= 3 - 2.
Hence, it is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
The subsequence consisting of indices 1, 2, and 3 is also valid.
It can be shown that it is not possible to get a balanced subsequence with a sum greater than 14.

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
var maxBalancedSubsequenceSum = function(nums) {
    const n = nums.length;
    const values = nums.map((x, i) => x - i);
    const sorted = [...new Set(values)].sort((a, b) => a - b);
    const m = sorted.length;

    const bit = new Array(m + 1).fill(-Infinity);

    function getRank(target) {
        let left = 0;
        let right = m - 1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (sorted[mid] === target) {
                return mid + 1;
            } else if (sorted[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return left + 1;
    }

    function query(i) {
        let best = -Infinity;

        while (i > 0) {
            best = Math.max(best, bit[i]);
            i -= i & -i;
        }

        return best;
    }

    function update(i, value) {
        while (i <= m) {
            bit[i] = Math.max(bit[i], value);
            i += i & -i;
        }
    }

    let answer = -Infinity;

    for (let i = 0; i < n; i++) {
        const rank = getRank(nums[i] - i);
        const bestPrevious = query(rank);
        const current = Math.max(nums[i], nums[i] + bestPrevious);

        update(rank, current);
        answer = Math.max(answer, current);
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
- [3165. Maximum Sum of Subsequence With Non-adjacent Elements](../../3001-3500/3423-maximum-sum-of-subsequence-with-non-adjacent-elements/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-balanced-subsequence-sum/)
