# LeetCode 3505: Minimum Operations to Make Elements Within K Subarrays Equal

**LeetCode Problem #3505 — Minimum Operations to Make Elements Within K Subarrays Equal**
Solve LeetCode Minimum Operations to Make Elements Within K Subarrays Equal using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make Elements Within K Subarrays Equal |
| LeetCode | #3505 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and two integers, `x` and `k`. You can perform the following operation any number of times (**including zero**):

Increase or decrease any element of `nums` by 1.

Return the **minimum** number of operations needed to have **at least** `k` *non-overlapping subarrays * of size **exactly** `x` in `nums`, where all elements within each subarray are equal.

## Constraints
- `2 <= nums.length <= 10^5`
- `-10^6 <= nums[i] <= 10^6`
- `2 <= x <= nums.length`
- `1 <= k <= 15`
- `2 <= k * x <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2`
- **Output:** `8`
- **Explanation:** Use 3 operations to add 3 to `nums[1]` and use 2 operations to subtract 2 from `nums[3]`. The resulting array is `[5, 1, 1, 1, 7, 3, 6, 4, -1]`. 
 Use 1 operation to add 1 to `nums[5]` and use 2 operations to subtract 2 from `nums[6]`. The resulting array is `[5, 1, 1, 1, 7, 4, 4, 4, -1]`. 
 Now, all elements within each subarray `[1, 1, 1]` (from indices 1 to 3) and `[4, 4, 4]` (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

### Example 2
- **Input:** `nums = [9,-2,-2,-2,1,5], x = 2, k = 2`
- **Output:** `3`
- **Explanation:** Use 3 operations to subtract 3 from `nums[4]`. The resulting array is `[9, -2, -2, -2, -2, 5]`. 
 Now, all elements within each subarray `[-2, -2]` (from indices 1 to 2) and `[-2, -2]` (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Operations to Make Elements Within K Subarrays Equal**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Use 3 operations to add 3 to `nums[1]` and use 2 operations to subtract 2 from `nums[3]`. The resulting array is `[5, 1, 1, 1, 7, 3, 6, 4, -1]`. 
 Use 1 operation to add 1 to `nums[5]` and use 2 operations to subtract 2 from `nums[6]`. The resulting array is `[5, 1, 1, 1, 7, 4, 4, 4, -1]`. 
 Now, all elements within each subarray `[1, 1, 1]` (from indices 1 to 3) and `[4, 4, 4]` (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        cost = self._window_costs(nums, x)  # length n - x + 1

        INF = float('inf')
        prev = [0] * (n + 1)  # dp for j = 0
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x and prev[i - x] != INF:
                    cur[i] = min(cur[i], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]

    def _window_costs(self, nums, x):
        n = len(nums)
        lo = []  # max-heap via negatives
        hi = []  # min-heap
        delayed = defaultdict(int)
        lo_size = hi_size = 0
        lo_sum = hi_sum = 0

        def prune(heap, is_lo):
            while heap:
                v = -heap[0] if is_lo else heap[0]
                if delayed[v] > 0:
                    delayed[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            target = (lo_size + hi_size + 1) // 2
            while lo_size > target:
                prune(lo, True)
                v = -heapq.heappop(lo)
                heapq.heappush(hi, v)
                lo_size -= 1; hi_size += 1
                lo_sum -= v; hi_sum += v
            while lo_size < target:
                prune(hi, False)
                v = heapq.heappop(hi)
                heapq.heappush(lo, -v)
                hi_size -= 1; lo_size += 1
                hi_sum -= v; lo_sum += v

        def add(v):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            prune(lo, True)
            if not lo or v <= -lo[0]:
                heapq.heappush(lo, -v)
                lo_size += 1; lo_sum += v
            else:
                heapq.heappush(hi, v)
                hi_size += 1; hi_sum += v
            rebalance()

        def remove(v):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            prune(lo, True)
            delayed[v] += 1
            if v <= -lo[0]:
                lo_size -= 1; lo_sum -= v
                prune(lo, True)
            else:
                hi_size -= 1; hi_sum -= v
                prune(hi, False)
            rebalance()

        res = []
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                prune(lo, True)
                med = -lo[0]
                res.append(med * lo_size - lo_sum + hi_sum - med * hi_size)
        return res
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../../3001-3500/3191-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/)
