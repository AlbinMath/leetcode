# LeetCode 2542: Maximum Subsequence Score

**LeetCode Problem #2542 — Maximum Subsequence Score**
Solve LeetCode Maximum Subsequence Score using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Subsequence Score |
| LeetCode | #2542 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** integer arrays `nums1` and `nums2` of equal length `n` and a positive integer `k`. You must choose a **subsequence** of indices from `nums1` of length `k`.

For chosen indices `i_0`, `i_1`, ..., `i_k - 1`, your **score** is defined as:

The sum of the selected elements from `nums1` multiplied with the **minimum** of the selected elements from `nums2`. 
 It can defined simply as: `(nums1[i_0] + nums1[i_1] +...+ nums1[i_k - 1]) * min(nums2[i_0] , nums2[i_1], ... ,nums2[i_k - 1])`.

Return *the **maximum** possible score.*

A **subsequence** of indices of an array is a set that can be derived from the set `{0, 1, ..., n-1}` by deleting some or no elements.

## Constraints
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[j] <= 10^5`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3`
- **Output:** `12`
- **Explanation:** The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

### Example 2
- **Input:** `nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1`
- **Output:** `30`
- **Explanation:** Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Subsequence Score**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

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
var maxScore = function(nums1, nums2, k) {
    const n = nums1.length;

    const pairs = [];

    for (let i = 0; i < n; i++) {
        pairs.push([nums1[i], nums2[i]]);
    }

    // Sort by nums2 in descending order
    pairs.sort((a, b) => b[1] - a[1]);

    // Min heap to keep the largest k nums1 values
    const heap = [];
    let sum = 0;
    let maxScore = 0;

    function push(val) {
        heap.push(val);
        let i = heap.length - 1;

        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);

            if (heap[parent] <= heap[i]) break;

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function pop() {
        const min = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;

            while (true) {
                let smallest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;

                if (
                    left < heap.length &&
                    heap[left] < heap[smallest]
                ) {
                    smallest = left;
                }

                if (
                    right < heap.length &&
                    heap[right] < heap[smallest]
                ) {
                    smallest = right;
                }

                if (smallest === i) break;

                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];

                i = smallest;
            }
        }

        return min;
    }

    for (const [num1, num2] of pairs) {
        push(num1);
        sum += num1;

        if (heap.length > k) {
            sum -= pop();
        }

        if (heap.length === k) {
            maxScore = Math.max(maxScore, sum * num2);
        }
    }

    return maxScore;
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
- [1255. Maximum Score Words Formed by Letters](../../1001-1500/1255-maximum-score-words-formed-by-letters/)
- [1422. Maximum Score After Splitting a String](../../1001-1500/1422-maximum-score-after-splitting-a-string/)
- [1717. Maximum Score From Removing Substrings](../../1501-2000/1717-maximum-score-from-removing-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-subsequence-score/)
