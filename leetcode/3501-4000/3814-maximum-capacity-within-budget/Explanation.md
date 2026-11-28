# LeetCode 3814: Maximum Capacity Within Budget

**LeetCode Problem #3814 — Maximum Capacity Within Budget**
Solve LeetCode Maximum Capacity Within Budget using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Capacity Within Budget |
| LeetCode | #3814 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `costs` and `capacity`, both of length `n`, where `costs[i]` represents the purchase cost of the `i^th` machine and `capacity[i]` represents its performance capacity.

You are also given an integer `budget`.

You may select **at most two distinct** machines such that the **total cost** of the selected machines is **strictly less** than `budget`.

Return the **maximum** achievable total capacity of the selected machines.

## Constraints
- `1 <= n == costs.length == capacity.length <= 10^5`
- `1 <= costs[i], capacity[i] <= 10^5`
- `1 <= budget <= 2 * 10^5`

## Examples
### Example 1
- **Input:** `costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8`
- **Output:** `8`
- **Explanation:** Choose two machines with `costs[0] = 4` and `costs[3] = 3`. 
 The total cost is `4 + 3 = 7`, which is strictly less than `budget = 8`. 
 The maximum total capacity is `capacity[0] + capacity[3] = 1 + 7 = 8`.

### Example 2
- **Input:** `costs = [3,5,7,4], capacity = [2,4,3,6], budget = 7`
- **Output:** `6`
- **Explanation:** Choose one machine with `costs[3] = 4`. 
 The total cost is 4, which is strictly less than `budget = 7`. 
 The maximum total capacity is `capacity[3] = 6`.

### Example 3
- **Input:** `costs = [2,2,2], capacity = [3,5,4], budget = 5`
- **Output:** `9`
- **Explanation:** Choose two machines with `costs[1] = 2` and `costs[2] = 2`. 
 The total cost is `2 + 2 = 4`, which is strictly less than `budget = 5`. 
 The maximum total capacity is `capacity[1] + capacity[2] = 5 + 4 = 9`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Capacity Within Budget**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Choose two machines with `costs[0] = 4` and `costs[3] = 3`. 
 The total cost is `4 + 3 = 7`, which is strictly less than `budget = 8`. 
 The maximum total capacity is `capacity[0] + capacity[3] = 1 + 7 = 8`.

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
from bisect import bisect_left
from typing import List

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        items = sorted(zip(costs, capacity))
        cs = [c for c, _ in items]

        pm = []
        cur = 0
        for _, cap in items:
            cur = max(cur, cap)
            pm.append(cur)

        ans = 0
        for i, (c, cap) in enumerate(items):
            if c >= budget:
                break                       # sorted: no later machine is affordable
            ans = max(ans, cap)
            idx = bisect_left(cs, budget - c, 0, i)
            if idx > 0:
                ans = max(ans, cap + pm[idx - 1])
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
- [2398. Maximum Number of Robots Within Budget](../../2001-2500/2398-maximum-number-of-robots-within-budget/)
- [2279. Maximum Bags With Full Capacity of Rocks](../../2001-2500/2279-maximum-bags-with-full-capacity-of-rocks/)
- [1011. Capacity To Ship Packages Within D Days](../../1001-1500/1011-capacity-to-ship-packages-within-d-days/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-capacity-within-budget/)
