# LeetCode 4017: Peaks in Array II

**LeetCode Problem #4017 — Peaks in Array II**
Solve LeetCode Peaks in Array II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Peaks in Array II |
| LeetCode | #4017 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and a 2D integer array `queries`.

A ** subarray ** `nums[i..j]` is called a **peak subarray** if:

Its length is **at least** 3. 
 There exists an index `k` such that `i < k < j` and:
 
 `nums[k] > nums[k - 1]` 
 `nums[k] > nums[k + 1]`

You have to process queries of two types:

`[1, l_i, r_i]`: Calculate the number of **peak subarrays** fully contained within `nums[l_i..r_i]`. 
 `[2, index_i, val_i]`: Update `nums[index_i]` to `val_i`. This update applies to all subsequent queries.

Return an array `answer`, where `answer[i]` is the answer to the `i^th` query of type 1 in the order they appear.

## Constraints
- `3 <= n == nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i] = [1, l_i, r_i]` or `queries[i] = [2, index_i, val_i]`
- `0 <= l_i < r_i <= n - 1`
- `0 <= index_i <= n - 1`
- `0 <= val_i <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,3,2,4], queries = [[1,0,3],[2,1,1],[1,0,3]]`
- **Output:** `[2,0]`
- **Explanation:** ​​​​​​​ 

 
 Query `[1, 0, 3]`:

 
 `[1, 3, 2]`: choose `k = 1`. Then `nums[k] = 3`, `nums[k - 1] = 1`, and `nums[k + 1] = 2`. Since `3 > 1` and `3 > 2`, this is a peak subarray. 
 `[1, 3, 2, 4]`: choose `k = 1`. Then `nums[k] = 3`, `nums[k - 1] = 1`, and `nums[k + 1] = 2`. Since `3 > 1` and `3 > 2`, this is a peak subarray. 
 
 
 Query `[2, 1, 1]`: Update `nums[1]` to 1. The array becomes `[1, 1, 2, 4]`. 
 Query `[1, 0, 3]`: There are no peak subarrays now. 
 Thus, `answer = [2, 0]`.

### Example 2
- **Input:** `nums = [9,8,9,8], queries = [[1,1,3],[2,2,1],[1,0,2]]`
- **Output:** `[1,0]`
- **Explanation:** Query `[1, 1, 3]`:

 
 `nums[1..3] = [8, 9, 8]`: choose `k = 2`. Then `nums[k] = 9`, `nums[k - 1] = 8`, and `nums[k + 1] = 8`. Since `9 > 8` and `9 > 8`, this is a peak subarray. 
 
 
 Query `[2, 2, 1]`: Update `nums[2]` to 1. The array becomes `[9, 8, 1, 8]`. 
 Query `[1, 0, 2]`: There are no peak subarrays. 
 Thus, `answer = [1, 0]`.

### Example 3
- **Input:** `nums = [3,6,2,7,1], queries = [[1,1,3],[2,3,0],[1,0,4]]`
- **Output:** `[0,3]`
- **Explanation:** Query `[1, 1, 3]`: The only subarray of length at least 3 is `[6, 2, 7]`. Its only possible peak index is `k = 2`, but `nums[2] = 2` is less than both `nums[1] = 6` and `nums[3] = 7`, so it is not a peak subarray. 
 Query `[2, 3, 0]`: Update `nums[3]` to 0. The array becomes `[3, 6, 2, 0, 1]`. 
 Query `[1, 0, 4]`:
 
 `[3, 6, 2]`: choose `k = 1`. Then `nums[k] = 6`, `nums[k - 1] = 3`, and `nums[k + 1] = 2`. Since `6 > 3` and `6 > 2`, this is a peak subarray. 
 `[3, 6, 2, 0]`: choose `k = 1`. Then `nums[k] = 6`, `nums[k - 1] = 3`, and `nums[k + 1] = 2`. Since `6 > 3` and `6 > 2`, this is a peak subarray. 
 `[3, 6, 2, 0, 1]`: choose `k = 1`. Then `nums[k] = 6`, `nums[k - 1] = 3`, and `nums[k + 1] = 2`. Since `6 > 3` and `6 > 2`, this is a peak subarray. 
 
 
 Thus, `answer = [0, 3]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Peaks in Array II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2,4], queries = [[1,0,3],[2,1,1],[1,0,3]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,0]`.
4. **Verification:** ​​​​​​​ 

 
 Query `[1, 0, 3]`:

 
 `[1, 3, 2]`: choose `k = 1`. Then `nums[k] = 3`, `nums[k - 1] = 1`, and `nums[k + 1] = 2`. Since `3 > 1` and `3 > 2`, this is a peak subarray. 
 `[1, 3, 2, 4]`: choose `k = 1`. Then `nums[k] = 3`, `nums[k - 1] = 1`, and `nums[k + 1] = 2`. Since `3 > 1` and `3 > 2`, this is a peak subarray. 
 
 
 Query `[2, 1, 1]`: Update `nums[1]` to 1. The array becomes `[1, 1, 2, 4]`. 
 Query `[1, 0, 3]`: There are no peak subarrays now. 
 Thus, `answer = [2, 0]`.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def countOfPeaks(self, nums, queries):
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a
            return (a[0], b[1], a[2] + b[2] + (b[0] - a[1]) * b[0])

        def leaf(i):
            if 1 <= i <= n - 2 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return (i, i, 0)
            return None

        tree = [None] * (2 * size)
        for i in range(n):
            tree[size + i] = leaf(i)
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def refresh(i):
            if i < 0 or i >= n:
                return
            pos = size + i
            tree[pos] = leaf(i)
            pos >>= 1
            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos >>= 1

        def query(lo, hi):
            lo += size
            hi += size + 1
            left = right = None
            while lo < hi:
                if lo & 1:
                    left = merge(left, tree[lo])
                    lo += 1
                if hi & 1:
                    hi -= 1
                    right = merge(tree[hi], right)
                lo >>= 1
                hi >>= 1
            return merge(left, right)

        ans = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                res = query(l + 1, r - 1) if r - l >= 2 else None
                if res is None:
                    ans.append(0)
                else:
                    first, last, B = res
                    ans.append((first - l) * (r - first) + r * (last - first) - B)
            else:
                idx, val = q[1], q[2]
                nums[idx] = val
                refresh(idx - 1)
                refresh(idx)
                refresh(idx + 1)
        return ans
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
- [3187. Peaks in Array](../../3001-3500/3438-peaks-in-array/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/peaks-in-array-ii/)
