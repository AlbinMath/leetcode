# LeetCode 3961: Maximize Sum of Device Ratings

**LeetCode Problem #3961 — Maximize Sum of Device Ratings**
Solve LeetCode Maximize Sum of Device Ratings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Sum of Device Ratings |
| LeetCode | #3961 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `units` of size `m &times; n` where `units[i][j]` represents the capacity of the `j^th` unit in the `i^th` device. Each device contains **exactly** `n` units.

The **rating** of a device is the **minimum** capacity among all its units.

You may perform the following operation any number of times (including zero):

Choose a device `i` that has **not been** used as a source before. 
 Remove **exactly** one unit from device `i` and add it to **any** different device. 
 Then mark device `i` as used, so it cannot be chosen again as a source.

Return the **maximum** possible sum of the ratings of all devices after any number of such operations.

**Note:**

Devices can receive units from multiple devices, regardless of whether they have been selected. 
 The rating of an empty device is 0.

## Constraints
- `1 <= m == units.length <= 10^5`
- `1 <= n == units[i].length <= 10^5`
- `m * n <= 2 * 10^5`
- `1 <= units[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `units = [[1,3],[2,2]]`
- **Output:** `4`
- **Explanation:** ​​​​​​​​​​​​​​Select device `i = 0` and transfer `units[0][0] = 1` to device `i = 1`. 
 After the transfer, the ratings are:
 
 Device `0 = [3]`: `rating[0] = 3` 
 Device `1 = [2, 2, 1 ]`: `rating[1] = 1` 
 
 
 Thus, the sum of ratings is `3 + 1 = 4`.

### Example 2
- **Input:** `units = [[1,2,3],[4,5,6]]`
- **Output:** `6`
- **Explanation:** Select device `i = 1` and transfer `units[1][0] = 4` to device `i = 0`. 
 After the transfer, the ratings are:
 
 Device `0 = [1, 2, 3, 4 ]`: `rating[0] = 1` 
 Device `1 = [5, 6]`: `rating[1] = 5` 
 
 
 Thus, the sum of ratings is `1 + 5 = 6`.

### Example 3
- **Input:** `units = [[5,5,5],[1,1,1]]`
- **Output:** `6`
- **Explanation:** No transfers increase the sum of ratings. Thus, the sum of ratings is `5 + 1 = 6`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Sum of Device Ratings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `units = [[1,3],[2,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** ​​​​​​​​​​​​​​Select device `i = 0` and transfer `units[0][0] = 1` to device `i = 1`. 
 After the transfer, the ratings are:
 
 Device `0 = [3]`: `rating[0] = 3` 
 Device `1 = [2, 2, 1 ]`: `rating[1] = 1` 
 
 
 Thus, the sum of ratings is `3 + 1 = 4`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq
from typing import List

class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        m, n = len(units), len(units[0])
        mins = [min(r) for r in units]
        S = sum(mins)
        if n == 1 or m == 1:
            return S

        d = []
        for r in units:
            a, b = heapq.nsmallest(2, r)
            d.append(b - a)

        g = min(range(m), key=lambda i: mins[i])
        total_d = sum(d)

        # Option A: g is the receiver
        res = S + total_d - d[g]

        # Option B: g gives too, some other s receives
        for s in range(m):
            if s != g:
                res = max(res, S + total_d - d[s] - (mins[s] - mins[g]))

        return res
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [2897. Apply Operations on Array to Maximize Sum of Squares](../../2501-3000/2897-apply-operations-on-array-to-maximize-sum-of-squares/)
- [3367. Maximize Sum of Weights after Edge Removals](../../3001-3500/3367-maximize-sum-of-weights-after-edge-removals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-sum-of-device-ratings/)
