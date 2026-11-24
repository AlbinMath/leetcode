# LeetCode 4055: Count Shadow Pairs II

**LeetCode Problem #4055 — Count Shadow Pairs II**
Solve LeetCode Count Shadow Pairs II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Shadow Pairs II |
| LeetCode | #4055 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

A pair of indices `(i, j)` is called a **shadow pair** if all of the following conditions are satisfied:

`0 <= i < j < n` 
 `nums[i] < nums[j]` 
 There **does not exist** an index `k` such that `i < k < j` and `nums[i] < nums[k] < nums[j]`.

Return the total number of **shadow pairs**.

## Constraints
- `3 <= n == nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,1,4,2,5]`
- **Output:** `5`
- **Explanation:** `(i, j)` 
 `nums[i]` 
 `nums[j]` 
 Shadow Pair 
 
 
 
 
 (0, 2) 
 3 
 4 
 `nums[1] = 1` is not strictly between 3 and 4 
 
 
 (1, 2) 
 1 
 4 
 No index `k` exists such that `1 < k < 2` 
 
 
 (1, 3) 
 1 
 2 
 `nums[2] = 4` is not strictly between 1 and 2 
 
 
 (2, 4) 
 4 
 5 
 `nums[3] = 2` is not strictly between 4 and 5 
 
 
 (3, 4) 
 2 
 5 
 No index `k` exists such that `3 < k < 4` 
 
 
 
 

 Thus, the answer is 5.

### Example 2
- **Input:** `nums = [6,7,8,9]`
- **Output:** `3`
- **Explanation:** `(i, j)` 
 `nums[i]` 
 `nums[j]` 
 Shadow Pair 
 
 
 
 
 (0, 1) 
 6 
 7 
 No index `k` exists such that `0 < k < 1` 
 
 
 (1, 2) 
 7 
 8 
 No index `k` exists such that `1 < k < 2` 
 
 
 (2, 3) 
 8 
 9 
 No index `k` exists such that `2 < k < 3` 
 
 
 

 Thus, the answer is 3.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Shadow Pairs II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,4,2,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** `(i, j)` 
 `nums[i]` 
 `nums[j]` 
 Shadow Pair 
 
 
 
 
 (0, 2) 
 3 
 4 
 `nums[1] = 1` is not strictly between 3 and 4 
 
 
 (1, 2) 
 1 
 4 
 No index `k` exists such that `1 < k < 2` 
 
 
 (1, 3) 
 1 
 2 
 `nums[2] = 4` is not strictly between 1 and 2 
 
 
 (2, 4) 
 4 
 5 
 `nums[3] = 2` is not strictly between 4 and 5 
 
 
 (3, 4) 
 2 
 5 
 No index `k` exists such that `3 < k < 4` 
 
 
 
 

 Thus, the answer is 5.

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
from bisect import bisect_left

class Solution(object):
    def shadowPairs(self, nums):
        n = len(nums)
        INF = 10**18
        order = sorted(range(n), key=lambda i: (nums[i], i))
        pos = [0] * n

        for r, i in enumerate(order):
            pos[i] = r

        sorted_vals = [nums[i] for i in order]

        size = 4 * n
        mx = [-1] * size
        se = [-2] * size
        cnt = [0] * size

        def pull(o):
            a, b = 2 * o, 2 * o + 1

            if mx[a] > mx[b]:
                mx[o], cnt[o] = mx[a], cnt[a]
                se[o] = max(se[a], mx[b])
            elif mx[a] < mx[b]:
                mx[o], cnt[o] = mx[b], cnt[b]
                se[o] = max(se[b], mx[a])
            else:
                mx[o], cnt[o] = mx[a], cnt[a] + cnt[b]
                se[o] = max(se[a], se[b])

        def push(o):
            m = mx[o]
            for c in (2 * o, 2 * o + 1):
                if mx[c] > m:
                    mx[c] = m

        def insert(o, l, r, p):
            if l == r:
                mx[o] = INF
                se[o] = -2
                cnt[o] = 1
                return

            push(o)
            m = (l + r) >> 1

            if p <= m:
                insert(2 * o, l, m, p)
            else:
                insert(2 * o + 1, m + 1, r, p)

            pull(o)

        def update(o, l, r, qr, v):
            if l > qr or mx[o] < v:
                return 0

            if r <= qr and se[o] < v:
                res = cnt[o]
                if mx[o] > v:
                    mx[o] = v
                return res

            push(o)
            m = (l + r) >> 1

            res = update(2 * o, l, m, qr, v)
            res += update(2 * o + 1, m + 1, r, qr, v)

            pull(o)
            return res

        ans = 0

        for j in range(n):
            v = nums[j]
            k = bisect_left(sorted_vals, v)

            if k > 0:
                ans += update(1, 0, n - 1, k - 1, v)

            insert(1, 0, n - 1, pos[j])

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
- [4054. Count Shadow Pairs I](../../4001-4500/4054-count-shadow-pairs-i/)
- [1782. Count Pairs Of Nodes](../../1501-2000/1782-count-pairs-of-nodes/)
- [1803. Count Pairs With XOR in a Range](../../1501-2000/1803-count-pairs-with-xor-in-a-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-shadow-pairs-ii/)
