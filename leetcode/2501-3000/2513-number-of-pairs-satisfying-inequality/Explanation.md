# LeetCode 2426: Number of Pairs Satisfying Inequality

**LeetCode Problem #2426 — Number of Pairs Satisfying Inequality**
Solve LeetCode Number of Pairs Satisfying Inequality using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Pairs Satisfying Inequality |
| LeetCode | #2426 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** integer arrays `nums1` and `nums2`, each of size `n`, and an integer `diff`. Find the number of **pairs** `(i, j)` such that:

`0 <= i < j <= n - 1` **and** 
 `nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff`.

Return* the **number of pairs** that satisfy the conditions.*

## Constraints
- `n == nums1.length == nums2.length`
- `2 <= n <= 10^5`
- `-10^4 <= nums1[i], nums2[i] <= 10^4`
- `-10^4 <= diff <= 10^4`

## Examples
### Example 1
- **Input:** `nums1 = [3,2,5], nums2 = [2,2,1], diff = 1`
- **Output:** `3`
- **Explanation:** There are 3 pairs that satisfy the conditions:
1. i = 0, j = 1: 3 - 2 <= 2 - 2 + 1. Since i < j and 1 <= 1, this pair satisfies the conditions.
2. i = 0, j = 2: 3 - 5 <= 2 - 1 + 1. Since i < j and -2 <= 2, this pair satisfies the conditions.
3. i = 1, j = 2: 2 - 5 <= 2 - 1 + 1. Since i < j and -3 <= 2, this pair satisfies the conditions.
Therefore, we return 3.

### Example 2
- **Input:** `nums1 = [3,-1], nums2 = [-2,2], diff = -1`
- **Output:** `0`
- **Explanation:** Since there does not exist any pair that satisfies the conditions, we return 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Pairs Satisfying Inequality**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [3,2,5], nums2 = [2,2,1], diff = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are 3 pairs that satisfy the conditions:
1. i = 0, j = 1: 3 - 2 <= 2 - 2 + 1. Since i < j and 1 <= 1, this pair satisfies the conditions.
2. i = 0, j = 2: 3 - 5 <= 2 - 1 + 1. Since i < j and -2 <= 2, this pair satisfies the conditions.
3. i = 1, j = 2: 2 - 5 <= 2 - 1 + 1. Since i < j and -3 <= 2, this pair satisfies the conditions.
Therefore, we return 3.

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
var numberOfPairs = function(nums1, nums2, diff) {
    const n = nums1.length;
    const arr = new Array(n);

    for (let i = 0; i < n; i++) {
        arr[i] = nums1[i] - nums2[i];
    }

    const temp = new Array(n);

    function mergeSort(left, right) {
        if (left >= right) return 0;

        const mid = Math.floor((left + right) / 2);

        let count = mergeSort(left, mid);
        count += mergeSort(mid + 1, right);

        // Count valid pairs across the two halves
        let j = mid + 1;

        for (let i = left; i <= mid; i++) {
            while (
                j <= right &&
                arr[i] > arr[j] + diff
            ) {
                j++;
            }

            count += right - j + 1;
        }

        // Merge the sorted halves
        let i = left;
        j = mid + 1;
        let k = left;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        for (let p = left; p <= right; p++) {
            arr[p] = temp[p];
        }

        return count;
    }

    return mergeSort(0, n - 1);
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
- [1128. Number of Equivalent Domino Pairs](../../1001-1500/1227-number-of-equivalent-domino-pairs/)
- [1512. Number of Good Pairs](../../1501-2000/1635-number-of-good-pairs/)
- [1530. Number of Good Leaf Nodes Pairs](../../1501-2000/1653-number-of-good-leaf-nodes-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-pairs-satisfying-inequality/)
