# LeetCode 4009: Minimum Possible Maximum Waiting Time

**LeetCode Problem #4009 — Minimum Possible Maximum Waiting Time**
Solve LeetCode Minimum Possible Maximum Waiting Time using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Possible Maximum Waiting Time |
| LeetCode | #4009 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `demand`, where `demand[i]` is the amount of fuel required by the `i^th` car.

You are also given an integer array `fuel` of length 2. There are **exactly** two fuel dispensers, numbered 0 and 1, where `fuel[j]` is the initial amount of fuel available in dispenser `j`.

Cars are allowed to start refueling in **increasing** index order. Car 0 becomes allowed at time 0, and for each `i > 0`, car `i` becomes allowed **exactly** when car `i - 1` starts refueling.

The refueling process follows these rules:

Each dispenser can serve **at most** one car at a time. 
 When a car becomes allowed, you must choose a dispenser with **at least** `demand[i]` fuel remaining. If both dispensers have enough fuel remaining, you may choose **either** of them, regardless of when they become free. 
 The car waits until the chosen dispenser becomes free and starts refueling **immediately**. It cannot switch dispensers or intentionally wait after the chosen dispenser becomes free. 
 When a car starts refueling, the remaining fuel in the chosen dispenser decreases by `demand[i]`, and the dispenser remains occupied for `demand[i]` seconds. 
 Once started, refueling cannot be interrupted. 
 If neither dispenser has at least `demand[i]` fuel remaining when car `i` becomes allowed, the process terminates and no further cars can be served.

The **waiting time** of a car is the time between when it becomes allowed to start refueling and when it actually starts.

Return the **minimum** possible value of the **maximum** waiting time among all served cars over all assignments that **maximize** the number of served cars. If no car can be served, return -1.

## Constraints
- `1 <= demand.length <= 50`
- `1 <= demand[i] <= 20`
- `fuel.length == 2`
- `1 <= fuel[i] <= 50`

## Examples
### Example 1
- **Input:** `demand = [6,8,4,6,5], fuel = [16,13]`
- **Output:** `6`
- **Explanation:** The following assignment serves all five cars: 

 
 
 
 Car 
 Becomes allowed at 
 Starts refueling at 
 Dispenser used 
 Remaining fuel before start 
 (dispenser 0, dispenser 1) 
 Waiting time 
 
 
 0 
 0 
 0 
 0 
 (16, 13) 
 0 
 
 
 1 
 0 
 0 
 1 
 (10, 13) 
 0 
 
 
 2 
 0 
 6 
 0 
 (10, 5) 
 6 
 
 
 3 
 6 
 10 
 0 
 (6, 5) 
 4 
 
 
 4 
 10 
 10 
 1 
 (0, 5) 
 0 
 
 
 

 Thus, all five cars are served, and the maximum waiting time is 6. 

 To serve all five cars, dispenser 0 must serve the cars with demands 6, 4, and 6, while dispenser 1 must serve the cars with demands 8 and 5. Therefore, car 2 must wait until time 6 for dispenser 0 to become free, so no assignment serving all five cars can have a maximum waiting time less than 6.

### Example 2
- **Input:** `demand = [10,15], fuel = [12,17]`
- **Output:** `0`
- **Explanation:** At time 0, Car 0 becomes allowed and starts refuelling using dispenser 0. 
 Car 1 becomes allowed at time 0 (when Car 0 starts) and immediately starts refuelling using dispenser 1. 
 Both cars start without waiting, so the maximum waiting time is 0.

### Example 3
- **Input:** `demand = [10,5], fuel = [8,8]`
- **Output:** `-1`
- **Explanation:** At time 0, Car 0 becomes allowed. However, neither dispenser has enough fuel to serve it, so the process terminates immediately. 
 No car is served, so the answer is -1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Possible Maximum Waiting Time**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `demand = [6,8,4,6,5], fuel = [16,13]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The following assignment serves all five cars: 

 
 
 
 Car 
 Becomes allowed at 
 Starts refueling at 
 Dispenser used 
 Remaining fuel before start 
 (dispenser 0, dispenser 1) 
 Waiting time 
 
 
 0 
 0 
 0 
 0 
 (16, 13) 
 0 
 
 
 1 
 0 
 0 
 1 
 (10, 13) 
 0 
 
 
 2 
 0 
 6 
 0 
 (10, 5) 
 6 
 
 
 3 
 6 
 10 
 0 
 (6, 5) 
 4 
 
 
 4 
 10 
 10 
 1 
 (0, 5) 
 0 
 
 
 

 Thus, all five cars are served, and the maximum waiting time is 6. 

 To serve all five cars, dispenser 0 must serve the cars with demands 6, 4, and 6, while dispenser 1 must serve the cars with demands 8 and 5. Therefore, car 2 must wait until time 6 for dispenser 0 to become free, so no assignment serving all five cars can have a maximum waiting time less than 6.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        F0, F1 = fuel
        cur = {(0, 0, 0): 0}
        pref = 0
        best = -1
        for p in demand:
            nxt = {}
            for (s0, d0, d1), mx in cur.items():
                s1 = pref - s0
                # dispenser 0
                if s0 + p <= F0:
                    key = (s0 + p, p, max(d1 - d0, 0))
                    val = max(mx, d0)
                    if key not in nxt or val < nxt[key]:
                        nxt[key] = val
                # dispenser 1
                if s1 + p <= F1:
                    key = (s0, max(d0 - d1, 0), p)
                    val = max(mx, d1)
                    if key not in nxt or val < nxt[key]:
                        nxt[key] = val
            if not nxt:
                break
            cur = nxt
            pref += p
            best = min(cur.values())
        return best
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [4025. Minimize the Maximum Waiting Time at Synchronized Traffic Lights](../../4001-4500/4025-minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/)
- [539. Minimum Time Difference](../../0501-1000/0539-minimum-time-difference/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-possible-maximum-waiting-time/)
