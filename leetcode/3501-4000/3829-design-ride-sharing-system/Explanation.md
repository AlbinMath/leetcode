# LeetCode 3829: Design Ride Sharing System

**LeetCode Problem #3829 — Design Ride Sharing System**
Solve LeetCode Design Ride Sharing System using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Ride Sharing System |
| LeetCode | #3829 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A ride sharing system manages ride requests from riders and availability from drivers. Riders request rides, and drivers become available over time. The system should match riders and drivers in the order they arrive.

Implement the `RideSharingSystem` class:

`RideSharingSystem()` Initializes the system. 
 `void addRider(int riderId)` Adds a new rider with the given `riderId`. 
 `void addDriver(int driverId)` Adds a new driver with the given `driverId`. 
 `int[] matchDriverWithRider()` Matches the **earliest** available driver with the **earliest** waiting rider and removes both of them from the system. Returns an integer array of size 2 where `result = [driverId, riderId]` if a match is made. If no match is available, returns `[-1, -1]`. 
 `void cancelRider(int riderId)` Cancels the ride request of the rider with the given `riderId` **if the rider exists** and has **not** yet been matched.

## Constraints
- `1 <= riderId, driverId <= 1000`
- Each `riderId` is **unique** among riders and is added at most **once**.
- Each `driverId` is **unique** among drivers and is added at most **once**.
- At most 1000 calls will be made in **total** to `addRider`​​​​​​​, `addDriver`, `matchDriverWithRider`, and `cancelRider`.

## Examples
### Example 1
- **Input:** `["RideSharingSystem", "addRider", "addDriver", "addRider", "matchDriverWithRider", "addDriver", "cancelRider", "matchDriverWithRider", "matchDriverWithRider"] 
[[], [3], [2], [1], [], [5], [3], [], []]`
- **Output:** `[null, null, null, null, [2, 3], null, null, [5, 1], [-1, -1]]`
- **Explanation:** RideSharingSystem rideSharingSystem = new RideSharingSystem(); // Initializes the system 
rideSharingSystem.addRider(3); // rider 3 joins the queue 
rideSharingSystem.addDriver(2); // driver 2 joins the queue 
rideSharingSystem.addRider(1); // rider 1 joins the queue 
rideSharingSystem.matchDriverWithRider(); // returns [2, 3] 
rideSharingSystem.addDriver(5); // driver 5 becomes available 
rideSharingSystem.cancelRider(3); // rider 3 is already matched, cancel has no effect 
rideSharingSystem.matchDriverWithRider(); // returns [5, 1] 
rideSharingSystem.matchDriverWithRider(); // returns [-1, -1]

### Example 2
- **Input:** `["RideSharingSystem", "addRider", "addDriver", "addDriver", "matchDriverWithRider", "addRider", "cancelRider", "matchDriverWithRider"] 
[[], [8], [8], [6], [], [2], [2], []]`
- **Output:** `[null, null, null, null, [8, 8], null, null, [-1, -1]]`
- **Explanation:** RideSharingSystem rideSharingSystem = new RideSharingSystem(); // Initializes the system 
rideSharingSystem.addRider(8); // rider 8 joins the queue 
rideSharingSystem.addDriver(8); // driver 8 joins the queue 
rideSharingSystem.addDriver(6); // driver 6 joins the queue 
rideSharingSystem.matchDriverWithRider(); // returns [8, 8] 
rideSharingSystem.addRider(2); // rider 2 joins the queue 
rideSharingSystem.cancelRider(2); // rider 2 cancels 
rideSharingSystem.matchDriverWithRider(); // returns [-1, -1]

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Design Ride Sharing System**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["RideSharingSystem", "addRider", "addDriver", "addRider", "matchDriverWithRider", "addDriver", "cancelRider", "matchDriverWithRider", "matchDriverWithRider"] 
[[], [3], [2], [1], [], [5], [3], [], []]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, null, [2, 3], null, null, [5, 1], [-1, -1]]`.
4. **Verification:** RideSharingSystem rideSharingSystem = new RideSharingSystem(); // Initializes the system 
rideSharingSystem.addRider(3); // rider 3 joins the queue 
rideSharingSystem.addDriver(2); // driver 2 joins the queue 
rideSharingSystem.addRider(1); // rider 1 joins the queue 
rideSharingSystem.matchDriverWithRider(); // returns [2, 3] 
rideSharingSystem.addDriver(5); // driver 5 becomes available 
rideSharingSystem.cancelRider(3); // rider 3 is already matched, cancel has no effect 
rideSharingSystem.matchDriverWithRider(); // returns [5, 1] 
rideSharingSystem.matchDriverWithRider(); // returns [-1, -1]

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
from collections import deque
from typing import List

class RideSharingSystem:
    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.waiting = set()      # riders currently in the queue and not cancelled

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.waiting.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        # discard cancelled riders at the front
        while self.riders and self.riders[0] not in self.waiting:
            self.riders.popleft()
        if not self.riders or not self.drivers:
            return [-1, -1]
        rider = self.riders.popleft()
        driver = self.drivers.popleft()
        self.waiting.discard(rider)
        return [driver, rider]

    def cancelRider(self, riderId: int) -> None:
        self.waiting.discard(riderId)   # no effect if matched, cancelled, or unknown
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
- [1396. Design Underground System](../../1001-1500/1396-design-underground-system/)
- [1603. Design Parking System](../../1501-2000/1603-design-parking-system/)
- [1912. Design Movie Rental System](../../1501-2000/1912-design-movie-rental-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-ride-sharing-system/)
