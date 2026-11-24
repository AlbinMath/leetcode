# LeetCode 3691: Maximum Total Subarray Value II

**LeetCode Problem #3691 — Maximum Total Subarray Value II**
Solve LeetCode Maximum Total Subarray Value II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Total Subarray Value II |
| LeetCode | #3691 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `k`.

You must select **exactly** `k` **distinct** subarrays `nums[l..r]` of `nums`. Subarrays may overlap, but the exact same subarray (same `l` and `r`) **cannot** be chosen more than once.

The **value** of a subarray `nums[l..r]` is defined as: `max(nums[l..r]) - min(nums[l..r])`.

The **total value** is the sum of the **values** of all chosen subarrays.

Return the **maximum** possible total value you can achieve.

## Constraints
- `1 <= n == nums.length <= 5 * 10^​​​​​​​4`
- `0 <= nums[i] <= 10^9`
- `1 <= k <= min(10^5, n * (n + 1) / 2)`

## Examples
### Example 1
- **Input:** `nums = [1,3,2], k = 2`
- **Output:** `4`
- **Explanation:** One optimal approach is: 

 
 Choose `nums[0..1] = [1, 3]`. The maximum is 3 and the minimum is 1, giving a value of `3 - 1 = 2`. 
 Choose `nums[0..2] = [1, 3, 2]`. The maximum is still 3 and the minimum is still 1, so the value is also `3 - 1 = 2`. 
 

 Adding these gives `2 + 2 = 4`.

### Example 2
- **Input:** `nums = [4,2,5,1], k = 3`
- **Output:** `12`
- **Explanation:** One optimal approach is: 

 
 Choose `nums[0..3] = [4, 2, 5, 1]`. The maximum is 5 and the minimum is 1, giving a value of `5 - 1 = 4`. 
 Choose `nums[1..3] = [2, 5, 1]`. The maximum is 5 and the minimum is 1, so the value is also `4`. 
 Choose `nums[2..3] = [5, 1]`. The maximum is 5 and the minimum is 1, so the value is again `4`. 
 

 Adding these gives `4 + 4 + 4 = 12`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Total Subarray Value II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** One optimal approach is: 

 
 Choose `nums[0..1] = [1, 3]`. The maximum is 3 and the minimum is 1, giving a value of `3 - 1 = 2`. 
 Choose `nums[0..2] = [1, 3, 2]`. The maximum is still 3 and the minimum is still 1, so the value is also `3 - 1 = 2`. 
 

 Adding these gives `2 + 2 = 4`.

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

    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        import heapq

        n = len(nums)

        # -------------------------------------------------
        # Segment Tree
        # -------------------------------------------------

        size = 1
        while size < n:
            size <<= 1

        INF = 10**18

        segMax = [-INF] * (2 * size)
        segMin = [INF] * (2 * size)

        # Build leaves
        for i in range(n):
            segMax[size + i] = nums[i]
            segMin[size + i] = nums[i]

        # Build tree
        for i in range(size - 1, 0, -1):
            segMax[i] = max(segMax[i << 1], segMax[i << 1 | 1])
            segMin[i] = min(segMin[i << 1], segMin[i << 1 | 1])

        def getValue(l, r):
            """Return max(nums[l:r+1]) - min(nums[l:r+1])."""

            if l > r:
                return 0

            l += size
            r += size

            mx = -INF
            mn = INF

            while l <= r:

                if l & 1:
                    mx = max(mx, segMax[l])
                    mn = min(mn, segMin[l])
                    l += 1

                if not (r & 1):
                    mx = max(mx, segMax[r])
                    mn = min(mn, segMin[r])
                    r -= 1

                l >>= 1
                r >>= 1

            return mx - mn

        # -------------------------------------------------
        # Max heap
        #
        # Python has a min heap, so store -value.
        #
        # Initially, for every l, choose [l, n-1].
        # This is the largest value for that l.
        # -------------------------------------------------

        heap = []

        for l in range(n):
            value = getValue(l, n - 1)
            heapq.heappush(heap, (-value, l, n - 1))

        answer = 0

        # Extract the k largest subarray values.
        for _ in range(k):

            negValue, l, r = heapq.heappop(heap)

            value = -negValue
            answer += value

            # Move to the next smaller subarray
            # for the same left endpoint.
            if r > l:
                nr = r - 1
                nextValue = getValue(l, nr)

                heapq.heappush(
                    heap,
                    (-nextValue, l, nr)
                )

        return answer
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
- [3689. Maximum Total Subarray Value I](../../4001-4500/4005-maximum-total-subarray-value-i/)
- [2234. Maximum Total Beauty of the Gardens](../../2001-2500/2330-maximum-total-beauty-of-the-gardens/)
- [2285. Maximum Total Importance of Roads](../../2001-2500/2379-maximum-total-importance-of-roads/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-ii/)
