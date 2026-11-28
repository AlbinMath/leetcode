# LeetCode 2332: The Latest Time to Catch a Bus

**LeetCode Problem #2332 — The Latest Time to Catch a Bus**
Solve LeetCode The Latest Time to Catch a Bus using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Latest Time to Catch a Bus |
| LeetCode | #2332 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `buses` of length `n`, where `buses[i]` represents the departure time of the `i^th` bus. You are also given a **0-indexed** integer array `passengers` of length `m`, where `passengers[j]` represents the arrival time of the `j^th` passenger. All bus departure times are unique. All passenger arrival times are unique.

You are given an integer `capacity`, which represents the **maximum** number of passengers that can get on each bus.

When a passenger arrives, they will wait in line for the next available bus. You can get on a bus that departs at `x` minutes if you arrive at `y` minutes where `y <= x`, and the bus is not full. Passengers with the **earliest** arrival times get on the bus first.

More formally when a bus arrives, either:

If `capacity` or fewer passengers are waiting for a bus, they will **all** get on the bus, or 
 The `capacity` passengers with the **earliest** arrival times will get on the bus.

Return *the latest time you may arrive at the bus station to catch a bus*. You **cannot** arrive at the same time as another passenger.

**Note: **The arrays `buses` and `passengers` are not necessarily sorted.

## Constraints
- `n == buses.length`
- `m == passengers.length`
- `1 <= n, m, capacity <= 10^5`
- `2 <= buses[i], passengers[i] <= 10^9`
- Each element in `buses` is **unique**.
- Each element in `passengers` is **unique**.

## Examples
### Example 1
- **Input:** `buses = [10,20], passengers = [2,17,18,19], capacity = 2`
- **Output:** `16`
- **Explanation:** Suppose you arrive at time 16.
At time 10, the first bus departs with the 0^th passenger. 
At time 20, the second bus departs with you and the 1^st passenger.
Note that you may not arrive at the same time as another passenger, which is why you must arrive before the 1^st passenger to catch the bus.

### Example 2
- **Input:** `buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2`
- **Output:** `20`
- **Explanation:** Suppose you arrive at time 20.
At time 10, the first bus departs with the 3^rd passenger. 
At time 20, the second bus departs with the 5^th and 1^st passengers.
At time 30, the third bus departs with the 0^th passenger and you.
Notice if you had arrived any later, then the 6^th passenger would have taken your seat on the third bus.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **The Latest Time to Catch a Bus**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `buses = [10,20], passengers = [2,17,18,19], capacity = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** Suppose you arrive at time 16.
At time 10, the first bus departs with the 0^th passenger. 
At time 20, the second bus departs with you and the 1^st passenger.
Note that you may not arrive at the same time as another passenger, which is why you must arrive before the 1^st passenger to catch the bus.

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
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        seen = set(passengers)

        j = 0
        cnt = 0
        for b in buses:
            cnt = 0
            while j < len(passengers) and passengers[j] <= b and cnt < capacity:
                j += 1
                cnt += 1

        cand = buses[-1] if cnt < capacity else passengers[j - 1]

        while cand in seen:
            cand -= 1
        return cand
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
- [1736. Latest Time by Replacing Hidden Digits](../../1501-2000/1736-latest-time-by-replacing-hidden-digits/)
- [3114. Latest Time You Can Obtain After Replacing Characters](../../3001-3500/3114-latest-time-you-can-obtain-after-replacing-characters/)
- [815. Bus Routes](../../0501-1000/0815-bus-routes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-latest-time-to-catch-a-bus/)
