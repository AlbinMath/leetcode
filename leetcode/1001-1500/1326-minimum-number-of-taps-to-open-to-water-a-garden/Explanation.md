# LeetCode 1326: Minimum Number of Taps to Open to Water a Garden

**LeetCode Problem #1326 — Minimum Number of Taps to Open to Water a Garden**
Solve LeetCode Minimum Number of Taps to Open to Water a Garden using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Taps to Open to Water a Garden |
| LeetCode | #1326 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a one-dimensional garden on the x-axis. The garden starts at the point `0` and ends at the point `n`. (i.e., the length of the garden is `n`).

There are `n + 1` taps located at points `[0, 1, ..., n]` in the garden.

Given an integer `n` and an integer array `ranges` of length `n + 1` where `ranges[i]` (0-indexed) means the `i-th` tap can water the area `[i - ranges[i], i + ranges[i]]` if it was open.

Return *the minimum number of taps* that should be open to water the whole garden, If the garden cannot be watered return **-1**.

## Constraints
- `1 <= n <= 10^4`
- `ranges.length == n + 1`
- `0 <= ranges[i] <= 100`

## Examples
### Example 1
- **Input:** `n = 5, ranges = [3,4,1,1,0,0]`
- **Output:** `1`
- **Explanation:** The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]

### Example 2
- **Input:** `n = 3, ranges = [0,0,0,0]`
- **Output:** `-1`
- **Explanation:** Even if you activate all the four taps you cannot water the whole garden.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Number of Taps to Open to Water a Garden**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, ranges = [3,4,1,1,0,0]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]

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

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        reach = list(range(n + 1))  # reach[s] = farthest end of an interval starting at s
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            reach[left] = max(reach[left], right)

        count = 0
        cur_end = 0
        farthest = 0
        for i in range(n + 1):
            if i > cur_end:
                return -1
            farthest = max(farthest, reach[i])
            if i == cur_end and cur_end < n:
                if farthest <= cur_end:
                    return -1
                cur_end = farthest
                count += 1
        return count
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
- [1954. Minimum Garden Perimeter to Collect Enough Apples](../../1501-2000/1954-minimum-garden-perimeter-to-collect-enough-apples/)
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [871. Minimum Number of Refueling Stops](../../0501-1000/0871-minimum-number-of-refueling-stops/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/)
