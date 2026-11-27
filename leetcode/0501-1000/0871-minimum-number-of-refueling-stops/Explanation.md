# LeetCode 871: Minimum Number of Refueling Stops

**LeetCode Problem #871 — Minimum Number of Refueling Stops**
Solve LeetCode Minimum Number of Refueling Stops using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Refueling Stops |
| LeetCode | #871 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A car travels from a starting position to a destination which is `target` miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array `stations` where `stations[i] = [position_i, fuel_i]` indicates that the `i^th` gas station is `position_i` miles east of the starting position and has `fuel_i` liters of gas.

The car starts with an infinite tank of gas, which initially has `startFuel` liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return *the minimum number of refueling stops the car must make in order to reach its destination*. If it cannot reach the destination, return `-1`.

Note that if the car reaches a gas station with `0` fuel left, the car can still refuel there. If the car reaches the destination with `0` fuel left, it is still considered to have arrived.

## Constraints
- `1 <= target, startFuel <= 10^9`
- `0 <= stations.length <= 500`
- `1 <= position_i < position_i+1 < target`
- `1 <= fuel_i < 10^9`

## Examples
### Example 1
- **Input:** `target = 1, startFuel = 1, stations = []`
- **Output:** `0`
- **Explanation:** We can reach the target without refueling.

### Example 2
- **Input:** `target = 100, startFuel = 1, stations = [[10,100]]`
- **Output:** `-1`
- **Explanation:** We can not reach the target (or even the first gas station).

### Example 3
- **Input:** `target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]`
- **Output:** `2`
- **Explanation:** We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel. We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas. We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Refueling Stops**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = 1, startFuel = 1, stations = []`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** We can reach the target without refueling.

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
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []  # max-heap via negated fuel
        fuel = startFuel  # farthest position reachable so far
        stops = 0
        for pos, gas in stations + [[target, 0]]:
            while fuel < pos:
                if not heap:
                    return -1
                fuel += -heapq.heappop(heap)
                stops += 1
            heapq.heappush(heap, -gas)
        return stops
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
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-refueling-stops/)
