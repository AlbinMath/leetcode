# LeetCode 2334: Subarray With Elements Greater Than Varying Threshold

**LeetCode Problem #2334 — Subarray With Elements Greater Than Varying Threshold**
Solve LeetCode Subarray With Elements Greater Than Varying Threshold using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subarray With Elements Greater Than Varying Threshold |
| LeetCode | #2334 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `threshold`.

Find any subarray of `nums` of length `k` such that **every** element in the subarray is **greater** than `threshold / k`.

Return* the **size** of **any** such subarray*. If there is no such subarray, return `-1`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i], threshold <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,3,4,3,1], threshold = 6`
- **Output:** `3`
- **Explanation:** The subarray [3,4,3] has a size of 3, and every element is greater than 6 / 3 = 2.
Note that this is the only valid subarray.

### Example 2
- **Input:** `nums = [6,5,6,5,8], threshold = 7`
- **Output:** `1`
- **Explanation:** The subarray [8] has a size of 1, and 8 > 7 / 1 = 7. So 1 is returned.
Note that the subarray [6,5] has a size of 2, and every element is greater than 7 / 2 = 3.5. 
Similarly, the subarrays [6,5,6], [6,5,6,5], [6,5,6,5,8] also satisfy the given conditions.
Therefore, 2, 3, 4, or 5 may also be returned.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Subarray With Elements Greater Than Varying Threshold**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,4,3,1], threshold = 6`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The subarray [3,4,3] has a size of 3, and every element is greater than 6 / 3 = 2.
Note that this is the only valid subarray.

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

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int) -> int:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.size[rx] < self.size[ry]:
                rx, ry = ry, rx
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]
        return self.size[rx]


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        dsu = DSU(n)
        active = [False] * n

        # Process indices ordered by value descending
        indices = sorted(range(n), key=lambda i: nums[i], reverse=True)

        for i in indices:
            active[i] = True
            k = 1

            if i > 0 and active[i - 1]:
                k = dsu.union(i, i - 1)
            if i + 1 < n and active[i + 1]:
                k = dsu.union(i, i + 1)

            if nums[i] * k > threshold:
                return k

        return -1
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
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
- [1608. Special Array With X Elements Greater Than or Equal X](../../1501-2000/1730-special-array-with-x-elements-greater-than-or-equal-x/)
- [713. Subarray Product Less Than K](../../0501-1000/0713-subarray-product-less-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/)
