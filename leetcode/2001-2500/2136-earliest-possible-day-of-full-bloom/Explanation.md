# LeetCode 2136: Earliest Possible Day of Full Bloom

**LeetCode Problem #2136 — Earliest Possible Day of Full Bloom**
Solve LeetCode Earliest Possible Day of Full Bloom using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Earliest Possible Day of Full Bloom |
| LeetCode | #2136 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have `n` flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes time and so does the growth of a seed. You are given two **0-indexed** integer arrays `plantTime` and `growTime`, of length `n` each:

`plantTime[i]` is the number of **full days** it takes you to **plant** the `i^th` seed. Every day, you can work on planting exactly one seed. You **do not** have to work on planting the same seed on consecutive days, but the planting of a seed is not complete **until** you have worked `plantTime[i]` days on planting it in total. 
 `growTime[i]` is the number of **full days** it takes the `i^th` seed to grow after being completely planted. **After** the last day of its growth, the flower **blooms** and stays bloomed forever.

From the beginning of day `0`, you can plant the seeds in **any** order.

Return *the **earliest** possible day where **all** seeds are blooming*.

## Constraints
- `n == plantTime.length == growTime.length`
- `1 <= n <= 10^5`
- `1 <= plantTime[i], growTime[i] <= 10^4`

## Examples
### Example 1
- **Input:** `plantTime = [1,4,3], growTime = [2,3,1]`
- **Output:** `9`
- **Explanation:** The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 0, plant the 0^th seed. The seed grows for 2 full days and blooms on day 3.
On days 1, 2, 3, and 4, plant the 1^st seed. The seed grows for 3 full days and blooms on day 8.
On days 5, 6, and 7, plant the 2^nd seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.

### Example 2
- **Input:** `plantTime = [1,2,3,2], growTime = [2,1,2,1]`
- **Output:** `9`
- **Explanation:** The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 1, plant the 0^th seed. The seed grows for 2 full days and blooms on day 4.
On days 0 and 3, plant the 1^st seed. The seed grows for 1 full day and blooms on day 5.
On days 2, 4, and 5, plant the 2^nd seed. The seed grows for 2 full days and blooms on day 8.
On days 6 and 7, plant the 3^rd seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.

### Example 3
- **Input:** `plantTime = [1], growTime = [1]`
- **Output:** `2`
- **Explanation:** On day 0, plant the 0^th seed. The seed grows for 1 full day and blooms on day 2.
Thus, on day 2, all the seeds are blooming.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Earliest Possible Day of Full Bloom**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `plantTime = [1,4,3], growTime = [2,3,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 0, plant the 0^th seed. The seed grows for 2 full days and blooms on day 3.
On days 1, 2, 3, and 4, plant the 1^st seed. The seed grows for 3 full days and blooms on day 8.
On days 5, 6, and 7, plant the 2^nd seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.

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
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        order = sorted(range(len(plantTime)), key=lambda i: -growTime[i])
        t = 0
        ans = 0
        for i in order:
            t += plantTime[i]
            ans = max(ans, t + growTime[i])
        return ans
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
- [894. All Possible Full Binary Trees](../../0501-1000/0894-all-possible-full-binary-trees/)
- [2251. Number of Flowers in Full Bloom](../../2001-2500/2251-number-of-flowers-in-full-bloom/)
- [1900. The Earliest and Latest Rounds Where Players Compete](../../1501-2000/1900-the-earliest-and-latest-rounds-where-players-compete/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/)
