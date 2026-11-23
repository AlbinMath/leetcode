# LeetCode 2407: Longest Increasing Subsequence II

**LeetCode Problem #2407 — Longest Increasing Subsequence II**
Solve LeetCode Longest Increasing Subsequence II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Increasing Subsequence II |
| LeetCode | #2407 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

Find the longest subsequence of `nums` that meets the following requirements:

The subsequence is **strictly increasing** and 
 The difference between adjacent elements in the subsequence is **at most** `k`.

Return* the length of the **longest** **subsequence** that meets the requirements.*

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i], k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [4,2,1,4,3,4,5,8,15], k = 3`
- **Output:** `5`
- **Explanation:** The longest subsequence that meets the requirements is [1,3,4,5,8].
The subsequence has a length of 5, so we return 5.
Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger than 3.

### Example 2
- **Input:** `nums = [7,4,5,1,8,12,4,7], k = 5`
- **Output:** `4`
- **Explanation:** The longest subsequence that meets the requirements is [4,5,8,12].
The subsequence has a length of 4, so we return 4.

### Example 3
- **Input:** `nums = [1,5], k = 1`
- **Output:** `1`
- **Explanation:** The longest subsequence that meets the requirements is [1].
The subsequence has a length of 1, so we return 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Increasing Subsequence II**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,2,1,4,3,4,5,8,15], k = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The longest subsequence that meets the requirements is [1,3,4,5,8].
The subsequence has a length of 5, so we return 5.
Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger than 3.

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
var lengthOfLIS = function(nums, k) {
    const MAX = 100000;
    const tree = new Array(4 * (MAX + 1)).fill(0);

    function query(node, start, end, left, right) {
        if (right < start || end < left) {
            return 0;
        }

        if (left <= start && end <= right) {
            return tree[node];
        }

        const mid = Math.floor((start + end) / 2);

        return Math.max(
            query(node * 2, start, mid, left, right),
            query(node * 2 + 1, mid + 1, end, left, right)
        );
    }

    function update(node, start, end, index, value) {
        if (start === end) {
            tree[node] = Math.max(tree[node], value);
            return;
        }

        const mid = Math.floor((start + end) / 2);

        if (index <= mid) {
            update(node * 2, start, mid, index, value);
        } else {
            update(node * 2 + 1, mid + 1, end, index, value);
        }

        tree[node] = Math.max(
            tree[node * 2],
            tree[node * 2 + 1]
        );
    }

    let answer = 0;

    for (const x of nums) {
        const left = Math.max(1, x - k);
        const right = x - 1;

        const best = left <= right
            ? query(1, 1, MAX, left, right)
            : 0;

        const current = best + 1;

        update(1, 1, MAX, x, current);

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
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [673. Number of Longest Increasing Subsequence](../../0501-1000/0673-number-of-longest-increasing-subsequence/)
- [674. Longest Continuous Increasing Subsequence](../../0501-1000/0674-longest-continuous-increasing-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-increasing-subsequence-ii/)
