# LeetCode 373: Find K Pairs with Smallest Sums

**LeetCode Problem #373 — Find K Pairs with Smallest Sums**
Solve LeetCode Find K Pairs with Smallest Sums using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find K Pairs with Smallest Sums |
| LeetCode | #373 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2` sorted in **non-decreasing order** and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element from the second array.

Return *the* `k` *pairs* `(u_1, v_1), (u_2, v_2), ..., (u_k, v_k)` *with the smallest sums*.

## Constraints
- `1 <= nums1.length, nums2.length <= 10^5`
- `-10^9 <= nums1[i], nums2[i] <= 10^9`
- `nums1` and `nums2` both are sorted in **non-decreasing order**.
- `1 <= k <= 10^4`
- `k <= nums1.length * nums2.length`

## Examples
### Example 1
- **Input:** `nums1 = [1,7,11], nums2 = [2,4,6], k = 3`
- **Output:** `[[1,2],[1,4],[1,6]]`
- **Explanation:** The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

### Example 2
- **Input:** `nums1 = [1,1,2], nums2 = [1,2,3], k = 2`
- **Output:** `[[1,1],[1,1]]`
- **Explanation:** The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find K Pairs with Smallest Sums**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,7,11], nums2 = [2,4,6], k = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2],[1,4],[1,6]]`.
4. **Verification:** The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

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
var kSmallestPairs = function(nums1, nums2, k) {
    const result = [];
    const heap = [];

    function push(node) {
        heap.push(node);
        let i = heap.length - 1;

        while (i > 0) {
            let p = Math.floor((i - 1) / 2);

            if (heap[p].sum <= heap[i].sum) break;

            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
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
                let left = 2 * i + 1;
                let right = 2 * i + 2;

                if (
                    left < heap.length &&
                    heap[left].sum < heap[smallest].sum
                ) {
                    smallest = left;
                }

                if (
                    right < heap.length &&
                    heap[right].sum < heap[smallest].sum
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

    // Initialize the heap with the first pair from each row.
    for (let i = 0; i < Math.min(nums1.length, k); i++) {
        push({
            i: i,
            j: 0,
            sum: nums1[i] + nums2[0]
        });
    }

    while (result.length < k && heap.length > 0) {
        const current = pop();
        const { i, j } = current;

        result.push([nums1[i], nums2[j]]);

        // Add the next pair from the same row.
        if (j + 1 < nums2.length) {
            push({
                i: i,
                j: j + 1,
                sum: nums1[i] + nums2[j + 1]
            });
        }
    }

    return result;
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
- [3821. Find Nth Smallest Integer With K One Bits](../../3501-4000/3821-find-nth-smallest-integer-with-k-one-bits/)
- [440. K-th Smallest in Lexicographical Order](../../0001-0500/0440-k-th-smallest-in-lexicographical-order/)
- [632. Smallest Range Covering Elements from K Lists](../../0501-1000/0632-smallest-range-covering-elements-from-k-lists/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
