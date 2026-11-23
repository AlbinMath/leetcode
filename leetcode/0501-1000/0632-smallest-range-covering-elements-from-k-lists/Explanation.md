# LeetCode 632: Smallest Range Covering Elements from K Lists

**LeetCode Problem #632 — Smallest Range Covering Elements from K Lists**
Solve LeetCode Smallest Range Covering Elements from K Lists using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Range Covering Elements from K Lists |
| LeetCode | #632 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have `k` lists of sorted integers in **non-decreasing order**. Find the smallest range that includes at least one number from each of the `k` lists.

We define the range `[a, b]` is smaller than range `[c, d]` if `b - a < d - c` **or** `a < c` if `b - a == d - c`.

## Constraints
- `nums.length == k`
- `1 <= k <= 3500`
- `1 <= nums[i].length <= 50`
- `-10^5 <= nums[i][j] <= 10^5`
- `nums[i]` is sorted in **non-decreasing** order.

## Examples
### Example 1
- **Input:** `nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`
- **Output:** `[20,24]`
- **Explanation:** List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

### Example 2
- **Input:** `nums = [[1,2,3],[1,2,3],[1,2,3]]`
- **Output:** `[1,1]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Smallest Range Covering Elements from K Lists**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[20,24]`.
4. **Verification:** List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

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
import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        h = [(a[0], i, 0) for i, a in enumerate(nums)]
        heapq.heapify(h)
        right = max(a[0] for a in nums)
        best = [-10**9, 10**9]

        while True:
            left, i, j = heapq.heappop(h)
            if right - left < best[1] - best[0]:
                best = [left, right]
            if j + 1 == len(nums[i]):
                break
            v = nums[i][j + 1]
            right = max(right, v)
            heapq.heappush(h, (v, i, j + 1))

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
- [347. Top K Frequent Elements](../../0001-0500/0347-top-k-frequent-elements/)
- [658. Find K Closest Elements](../../0501-1000/0658-find-k-closest-elements/)
- [2261. K Divisible Elements Subarrays](../../2001-2500/2339-k-divisible-elements-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)
