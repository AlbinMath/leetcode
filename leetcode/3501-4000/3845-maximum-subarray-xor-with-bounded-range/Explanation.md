# LeetCode 3845: Maximum Subarray XOR with Bounded Range

**LeetCode Problem #3845 — Maximum Subarray XOR with Bounded Range**
Solve LeetCode Maximum Subarray XOR with Bounded Range using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Subarray XOR with Bounded Range |
| LeetCode | #3845 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a non-negative integer array `nums` and an integer `k`.

You must select a ** subarray ** of `nums` such that the **difference** between its **maximum** and **minimum** elements is at most `k`. The **value** of this subarray is the bitwise XOR of all elements in the subarray.

Return an integer denoting the **maximum** possible **value** of the selected subarray.

## Constraints
- `1 <= nums.length <= 4 * 10^4`
- `0 <= nums[i] < 2^15`
- `0 <= k < 2^15`

## Examples
### Example 1
- **Input:** `nums = [5,4,5,6], k = 2`
- **Output:** `7`
- **Explanation:** Select the subarray [5,

### Example 2
- **Input:** `nums = [5,4,5,6], k = 1`
- **Output:** `6`
- **Explanation:** Select the subarray [5, 4, 5,

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Subarray XOR with Bounded Range**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,4,5,6], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Select the subarray [5,

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
from typing import List
from collections import deque

class Solution:
    def maxXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        B = 15
        pre = [0] * (n + 1)
        for i, v in enumerate(nums):
            pre[i + 1] = pre[i] ^ v

        size = (n + 1) * B + 2
        ch0 = [0] * size
        ch1 = [0] * size
        cnt = [0] * size
        tot = 1                      # node 0 is the root

        def update(x: int, d: int) -> None:
            nonlocal tot
            node = 0
            for b in range(B - 1, -1, -1):
                if (x >> b) & 1:
                    nxt = ch1[node]
                    if not nxt:
                        nxt = tot
                        tot += 1
                        ch1[node] = nxt
                else:
                    nxt = ch0[node]
                    if not nxt:
                        nxt = tot
                        tot += 1
                        ch0[node] = nxt
                cnt[nxt] += d
                node = nxt

        def query(x: int) -> int:
            node = 0
            res = 0
            for b in range(B - 1, -1, -1):
                bit = (x >> b) & 1
                want = ch0[node] if bit else ch1[node]   # opposite bit
                if want and cnt[want] > 0:
                    res |= 1 << b
                    node = want
                else:
                    node = ch1[node] if bit else ch0[node]
            return res

        mx = deque()   # indices, values decreasing
        mn = deque()   # indices, values increasing
        left = 0
        best = 0
        for r in range(n):
            while mx and nums[mx[-1]] <= nums[r]:
                mx.pop()
            mx.append(r)
            while mn and nums[mn[-1]] >= nums[r]:
                mn.pop()
            mn.append(r)

            update(pre[r], 1)                  # left end l = r becomes available
            while nums[mx[0]] - nums[mn[0]] > k:
                update(pre[left], -1)
                left += 1
                if mx[0] < left:
                    mx.popleft()
                if mn[0] < left:
                    mn.popleft()

            best = max(best, query(pre[r + 1]))
        return best
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
- [3755. Find Maximum Balanced XOR Subarray Length](../../3501-4000/3755-find-maximum-balanced-xor-subarray-length/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)
- [152. Maximum Product Subarray](../../0001-0500/0152-maximum-product-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/)
