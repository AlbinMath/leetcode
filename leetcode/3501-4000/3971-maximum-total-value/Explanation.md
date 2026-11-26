# LeetCode 3971: Maximum Total Value

**LeetCode Problem #3971 — Maximum Total Value**
Solve LeetCode Maximum Total Value using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Total Value |
| LeetCode | #3971 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `value` and `decay`, and an integer `m`.

`value[i]` represents the initial value at index `i`. 
 `decay[i]` represents how much the value decreases after each selection of index `i`.

You may select any index **multiple** times. The total number of selections across all indices must not exceed `m`.

If you select index `i` for the `t^th` time, where `t` is 1-indexed, the value gained is `value[i] - decay[i] * (t - 1)`.

Return the **maximum** total value you can obtain. Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= value.length == decay.length <= 10^5`
- `1 <= value[i], decay[i] <= 10^9​​​​​​​`
- `1 <= m <= 10^9`

## Examples
### Example 1
- **Input:** `value = [6,5,4], decay = [2,1,1], m = 4`
- **Output:** `19`
- **Explanation:** One optimal sequence of selections is as follows: 

 
 By selecting index 0, the value gained is 6. 
 By selecting index 1, the value gained is 5. 
 By selecting index 2, the value gained is 4. 
 By selecting index 0 again, the value gained is `6 - 2 = 4`. 
 

 The total value is `6 + 5 + 4 + 4 = 19`. No other sequence of at most 4 selections gives a higher total value.

### Example 2
- **Input:** `value = [7,2,2], decay = [3,2,1], m = 2`
- **Output:** `11`
- **Explanation:** One optimal sequence of selections is as follows: 

 
 By selecting index 0, the value gained is 7. 
 By selecting index 0 again, the value gained is `7 - 3 = 4`. 
 

 The total value is `7 + 4 = 11`.

### Example 3
- **Input:** `value = [4,3], decay = [5,4], m = 5`
- **Output:** `7`
- **Explanation:** One optimal sequence of selections is as follows: 

 
 By selecting index 0, the value gained is 4. 
 By selecting index 1, the value gained is 3. 
 

 The total value is `4 + 3 = 7`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Total Value**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `value = [6,5,4], decay = [2,1,1], m = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `19`.
4. **Verification:** One optimal sequence of selections is as follows: 

 
 By selecting index 0, the value gained is 6. 
 By selecting index 1, the value gained is 5. 
 By selecting index 2, the value gained is 4. 
 By selecting index 0 again, the value gained is `6 - 2 = 4`. 
 

 The total value is `6 + 5 + 4 + 4 = 19`. No other sequence of at most 4 selections gives a higher total value.

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
    def maxTotalValue(self, value: List[int], decay: List[int], m: int) -> int:
        MOD = 10**9 + 7

        def cnt(T):
            total = 0
            for v, d in zip(value, decay):
                if v >= T:
                    total += (v - T) // d + 1
            return total

        def series(T):
            # sum and count of all gains >= T
            s = c = 0
            for v, d in zip(value, decay):
                if v >= T:
                    k = (v - T) // d + 1
                    s += k * v - d * k * (k - 1) // 2
                    c += k
            return s, c

        if cnt(1) <= m:
            return series(1)[0] % MOD

        # largest T with cnt(T) >= m (cnt(1) > m, so T=1 qualifies)
        lo, hi = 1, max(value)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if cnt(mid) >= m:
                lo = mid
            else:
                hi = mid - 1
        T = lo

        s, c = series(T + 1)        # all gains strictly greater than T
        return (s + (m - c) * T) % MOD
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
- [3689. Maximum Total Subarray Value I](../../3501-4000/3689-maximum-total-subarray-value-i/)
- [3691. Maximum Total Subarray Value II](../../3501-4000/3691-maximum-total-subarray-value-ii/)
- [2234. Maximum Total Beauty of the Gardens](../../2001-2500/2234-maximum-total-beauty-of-the-gardens/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-total-value/)
