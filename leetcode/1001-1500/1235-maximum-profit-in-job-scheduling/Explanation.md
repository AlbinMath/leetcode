# LeetCode 1235: Maximum Profit in Job Scheduling

**LeetCode Problem #1235 — Maximum Profit in Job Scheduling**
Solve LeetCode Maximum Profit in Job Scheduling using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Profit in Job Scheduling |
| LeetCode | #1235 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`.

You're given the `startTime`, `endTime` and `profit` arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time `X` you will be able to start another job that starts at time `X`.

## Constraints
- `1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4`
- `1 <= startTime[i] < endTime[i] <= 10^9`
- `1 <= profit[i] <= 10^4`

## Examples
### Example 1
- **Input:** `startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]`
- **Output:** `120`
- **Explanation:** The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

### Example 2
- **Input:** `startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]`
- **Output:** `150`
- **Explanation:** The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

### Example 3
- **Input:** `startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]`
- **Output:** `6`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Profit in Job Scheduling**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `120`.
4. **Verification:** The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

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
from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        ends = []
        best = [0]

        for e, s, p in jobs:
            idx = bisect_right(ends, s)       # jobs already processed that end <= s
            take = best[idx] + p
            ends.append(e)
            best.append(max(best[-1], take))

        return best[-1]
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
- [1599. Maximum Profit of Operating a Centennial Wheel](../../1501-2000/1599-maximum-profit-of-operating-a-centennial-wheel/)
- [3530. Maximum Profit from Valid Topological Order in DAG](../../3501-4000/3530-maximum-profit-from-valid-topological-order-in-dag/)
- [826. Most Profit Assigning Work](../../0501-1000/0826-most-profit-assigning-work/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)
