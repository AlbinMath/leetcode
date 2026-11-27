# LeetCode 2279: Maximum Bags With Full Capacity of Rocks

**LeetCode Problem #2279 — Maximum Bags With Full Capacity of Rocks**
Solve LeetCode Maximum Bags With Full Capacity of Rocks using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Bags With Full Capacity of Rocks |
| LeetCode | #2279 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have `n` bags numbered from `0` to `n - 1`. You are given two **0-indexed** integer arrays `capacity` and `rocks`. The `i^th` bag can hold a maximum of `capacity[i]` rocks and currently contains `rocks[i]` rocks. You are also given an integer `additionalRocks`, the number of additional rocks you can place in **any** of the bags.

Return* the **maximum** number of bags that could have full capacity after placing the additional rocks in some bags.*

## Constraints
- `n == capacity.length == rocks.length`
- `1 <= n <= 5 * 10^4`
- `1 <= capacity[i] <= 10^9`
- `0 <= rocks[i] <= capacity[i]`
- `1 <= additionalRocks <= 10^9`

## Examples
### Example 1
- **Input:** `capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2`
- **Output:** `3`
- **Explanation:** Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.

### Example 2
- **Input:** `capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100`
- **Output:** `3`
- **Explanation:** Place 8 rocks in bag 0 and 2 rocks in bag 2.
The number of rocks in each bag are now [10,2,2].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that we did not use all of the additional rocks.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Bags With Full Capacity of Rocks**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.

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
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need = sorted(c - r for c, r in zip(capacity, rocks))
        count = 0
        for x in need:
            if x > additionalRocks:
                break
            additionalRocks -= x
            count += 1
        return count
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
- [3413. Maximum Coins From K Consecutive Bags](../../3001-3500/3413-maximum-coins-from-k-consecutive-bags/)
- [1011. Capacity To Ship Packages Within D Days](../../1001-1500/1011-capacity-to-ship-packages-within-d-days/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/)
