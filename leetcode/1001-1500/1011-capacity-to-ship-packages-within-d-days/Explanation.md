# LeetCode 1011: Capacity To Ship Packages Within D Days

**LeetCode Problem #1011 — Capacity To Ship Packages Within D Days**
Solve LeetCode Capacity To Ship Packages Within D Days using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Capacity To Ship Packages Within D Days |
| LeetCode | #1011 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `i^th` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

## Constraints
- `1 <= days <= weights.length <= 5 * 10^4`
- `1 <= weights[i] <= 500`

## Examples
### Example 1
- **Input:** `weights = [1,2,3,4,5,6,7,8,9,10], days = 5`
- **Output:** `15`
- **Explanation:** A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

### Example 2
- **Input:** `weights = [3,2,2,4,1,4], days = 3`
- **Output:** `6`
- **Explanation:** A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

### Example 3
- **Input:** `weights = [1,2,3,1,1], days = 4`
- **Output:** `3`
- **Explanation:** 1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Capacity To Ship Packages Within D Days**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `weights = [1,2,3,4,5,6,7,8,9,10], days = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

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
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2

            need, load = 1, 0
            for w in weights:
                if load + w > mid:
                    need += 1
                    load = 0
                load += w

            if need <= days:
                hi = mid
            else:
                lo = mid + 1

        return lo
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
- [3814. Maximum Capacity Within Budget](../../3501-4000/3814-maximum-capacity-within-budget/)
- [2279. Maximum Bags With Full Capacity of Rocks](../../2001-2500/2279-maximum-bags-with-full-capacity-of-rocks/)
- [957. Prison Cells After N Days](../../0501-1000/0957-prison-cells-after-n-days/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
