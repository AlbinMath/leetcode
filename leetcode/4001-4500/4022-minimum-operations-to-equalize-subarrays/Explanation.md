# LeetCode 3762: Minimum Operations to Equalize Subarrays

**LeetCode Problem #3762 — Minimum Operations to Equalize Subarrays**
Solve LeetCode Minimum Operations to Equalize Subarrays using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Equalize Subarrays |
| LeetCode | #3762 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase or decrease **any element of `nums` by **exactly** `k`.

You are also given a 2D integer array `queries`, where each `queries[i] = [l_i, r_i]`.

For each query, find the **minimum** number of operations required to make **all** elements in the ** subarray ** `nums[l_i..r_i]` **equal**. If it is impossible, the answer for that query is `-1`.

Return an array `ans`, where `ans[i]` is the answer for the `i^th` query.

## Constraints
- `1 <= n == nums.length <= 4 &times; 10^4`
- `1 <= nums[i] <= 10^9`​​​​​​​
- `1 <= k <= 10^9`
- `1 <= queries.length <= 4 &times; 10^4`
- `^​​​​​​​queries[i] = [l_i, r_i]`
- `0 <= l_i <= r_i <= n - 1`

## Examples
### Example 1
- **Input:** `nums = [1,4,7], k = 3, queries = [[0,1],[0,2]]`
- **Output:** `[1,2]`
- **Explanation:** One optimal set of operations: 

 
 
 
 `i` 
 `[l_i, r_i]` 
 `nums[l_i..r_i]` 
 Possibility 
 Operations 
 Final 
 `nums[l_i..r_i]` 
 `ans[i]` 
 
 
 
 
 0 
 [0, 1] 
 [1, 4] 
 Yes 
 `nums[0] + k = 1 + 3 = 4 = nums[1]` 
 [4, 4] 
 1 
 
 
 1 
 [0, 2] 
 [1, 4, 7] 
 Yes 
 nums[0] + k = 1 + 3 = 4 = nums[1] 
 nums[2] - k = 7 - 3 = 4 = nums[1] 
 [4, 4, 4] 
 2 
 
 
 

 Thus, `ans = [1, 2]`.

### Example 2
- **Input:** `nums = [1,2,4], k = 2, queries = [[0,2],[0,0],[1,2]]`
- **Output:** `[-1,0,1]`
- **Explanation:** One optimal set of operations: 

 
 
 
 `i` 
 `[l_i, r_i]` 
 `nums[l_i..r_i]` 
 Possibility 
 Operations 
 Final 
 `nums[l_i..r_i]` 
 `ans[i]` 
 
 
 0 
 [0, 2] 
 [1, 2, 4] 
 No 
 - 
 [1, 2, 4] 
 -1 
 
 
 1 
 [0, 0] 
 [1] 
 Yes 
 Already equal 
 [1] 
 0 
 
 
 2 
 [1, 2] 
 [2, 4] 
 Yes 
 `nums[1] + k = 2 + 2 = 4 = nums[2]` 
 [4, 4] 
 1 
 
 
 

 Thus, `ans = [-1, 0, 1]`.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Equalize Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,7], k = 3, queries = [[0,1],[0,2]]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.
4. **Verification:** One optimal set of operations: 

 
 
 
 `i` 
 `[l_i, r_i]` 
 `nums[l_i..r_i]` 
 Possibility 
 Operations 
 Final 
 `nums[l_i..r_i]` 
 `ans[i]` 
 
 
 
 
 0 
 [0, 1] 
 [1, 4] 
 Yes 
 `nums[0] + k = 1 + 3 = 4 = nums[1]` 
 [4, 4] 
 1 
 
 
 1 
 [0, 2] 
 [1, 4, 7] 
 Yes 
 nums[0] + k = 1 + 3 = 4 = nums[1] 
 nums[2] - k = 7 - 3 = 4 = nums[1] 
 [4, 4, 4] 
 2 
 
 
 

 Thus, `ans = [1, 2]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minOperations(self, nums, k, queries):
        n = len(nums)

        # Check remainder compatibility in O(1) per query.
        bad = [0] * n
        for i in range(1, n):
            bad[i] = bad[i - 1] + (
                nums[i] % k != nums[i - 1] % k
            )

        # Prefix sums: subarray sum in O(1).
        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x

        # Coordinate compression.
        vals = sorted(set(nums))
        rank = {x: i for i, x in enumerate(vals)}
        m = len(vals)

        # Persistent segment tree.
        left = [0]
        right = [0]
        cnt = [0]
        sm = [0]
        roots = [0]

        def insert(old, lo, hi, p, value):
            cur = len(cnt)
            left.append(left[old])
            right.append(right[old])
            cnt.append(cnt[old] + 1)
            sm.append(sm[old] + value)

            if lo < hi:
                mid = (lo + hi) // 2
                if p <= mid:
                    left[cur] = insert(
                        left[old], lo, mid, p, value
                    )
                else:
                    right[cur] = insert(
                        right[old], mid + 1, hi, p, value
                    )

            return cur

        for x in nums:
            roots.append(
                insert(roots[-1], 0, m - 1, rank[x], x)
            )

        def kth(a, b, lo, hi, target):
            if lo == hi:
                return vals[lo]

            mid = (lo + hi) // 2
            c = cnt[left[b]] - cnt[left[a]]

            if target <= c:
                return kth(left[a], left[b], lo, mid, target)

            return kth(
                right[a], right[b], mid + 1, hi, target - c
            )

        # Count and sum of values whose compressed index < limit.
        def query_less(a, b, lo, hi, limit):
            if hi < limit:
                return cnt[b] - cnt[a], sm[b] - sm[a]

            if lo >= limit:
                return 0, 0

            mid = (lo + hi) // 2

            c1, s1 = query_less(
                left[a], left[b], lo, mid, limit
            )
            c2, s2 = query_less(
                right[a], right[b], mid + 1, hi, limit
            )

            return c1 + c2, s1 + s2

        ans = []

        for l, r in queries:
            if bad[r] != bad[l]:
                ans.append(-1)
                continue

            length = r - l + 1
            a = roots[l]
            b = roots[r + 1]

            # Median of the queried subarray.
            median = kth(
                a, b, 0, m - 1, (length + 1) // 2
            )
            mid_idx = rank[median]

            # Values strictly smaller than the median.
            left_count, left_sum = query_less(
                a, b, 0, m - 1, mid_idx
            )

            # O(1) subarray sum.
            total_sum = pref[r + 1] - pref[l]

            right_count = length - left_count - 1
            right_sum = total_sum - left_sum - median

            # Total operations to make all values equal to median.
            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            ans.append(cost // k)

        return ans
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3505. Minimum Operations to Make Elements Within K Subarrays Equal](../../3501-4000/3717-minimum-operations-to-make-elements-within-k-subarrays-equal/)
- [3666. Minimum Operations to Equalize Binary String](../../3501-4000/3983-minimum-operations-to-equalize-binary-string/)
- [3674. Minimum Operations to Equalize Array](../../3501-4000/3998-minimum-operations-to-equalize-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/)
