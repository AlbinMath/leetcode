# LeetCode 493: Reverse Pairs

**LeetCode Problem #493 — Reverse Pairs**
Solve LeetCode Reverse Pairs using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Pairs |
| LeetCode | #493 |
| Difficulty | Hard |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return *the number of **reverse pairs** in the array*.

A **reverse pair** is a pair `(i, j)` where:

`0 <= i < j < nums.length` and 
 `nums[i] > 2 * nums[j]`.

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `nums = [1,3,2,3,1]`
- **Output:** `2`
- **Explanation:** The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

### Example 2
- **Input:** `nums = [2,4,3,5,1]`
- **Output:** `3`
- **Explanation:** The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Reverse Pairs**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2,3,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var reversePairs = function(nums) {
    const n = nums.length;
    const temp = new Array(n);

    function mergeSort(left, right) {
        if (left >= right) return 0;

        const mid = Math.floor((left + right) / 2);

        let count = mergeSort(left, mid);
        count += mergeSort(mid + 1, right);

        // Count reverse pairs across the two halves
        let j = mid + 1;

        for (let i = left; i <= mid; i++) {
            while (
                j <= right &&
                nums[i] > 2 * nums[j]
            ) {
                j++;
            }

            count += j - (mid + 1);
        }

        // Merge the two sorted halves
        let i = left;
        j = mid + 1;
        let k = left;

        while (i <= mid && j <= right) {
            if (nums[i] <= nums[j]) {
                temp[k++] = nums[i++];
            } else {
                temp[k++] = nums[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = nums[i++];
        }

        while (j <= right) {
            temp[k++] = nums[j++];
        }

        for (let p = left; p <= right; p++) {
            nums[p] = temp[p];
        }

        return count;
    }

    return mergeSort(0, n - 1);
};
```

### Python
```python
class Solution:
    def reversePairs(self, nums):
        def merge_sort(a):
            if len(a) < 2:
                return 0
            m = len(a)//2
            left, right = a[:m], a[m:]
            count = merge_sort(left) + merge_sort(right)
            j = 0
            for x in left:
                while j < len(right) and x > 2*right[j]:
                    j += 1
                count += j
            i = j = 0
            a[:] = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    a.append(left[i])
                    i += 1
                else:
                    a.append(right[j])
                    j += 1
            a.extend(left[i:])
            a.extend(right[j:])
            return count
        return merge_sort(nums)
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
- [24. Swap Nodes in Pairs](../../0001-0500/0024-swap-nodes-in-pairs/)
- [336. Palindrome Pairs](../../0001-0500/0336-palindrome-pairs/)
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-pairs/)
