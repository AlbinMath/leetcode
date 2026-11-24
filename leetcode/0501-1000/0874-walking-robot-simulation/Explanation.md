# LeetCode 874: Walking Robot Simulation

**LeetCode Problem #874 — Walking Robot Simulation**
Solve LeetCode Walking Robot Simulation using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Walking Robot Simulation |
| LeetCode | #874 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A robot on an infinite XY-plane starts at point `(0, 0)` facing north. The robot receives an array of integers `commands`, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:

`-2`: Turn left `90` degrees. 
 `-1`: Turn right `90` degrees. 
 `1 <= k <= 9`: Move forward `k` units, one unit at a time.

Some of the grid squares are `obstacles`. The `i^th` obstacle is at grid point `obstacles[i] = (x_i, y_i)`. If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

Return the **maximum squared Euclidean distance** that the robot reaches at any point in its path (i.e. if the distance is `5`, return `25`).

**Note:**

There can be an obstacle at `(0, 0)`. If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to `(0, 0)` due to the obstacle. 
 North means +Y direction. 
 East means +X direction. 
 South means -Y direction. 
 West means -X direction.

## Constraints
- `1 <= commands.length <= 10^4`
- `commands[i]` is either `-2`, `-1`, or an integer in the range `[1, 9]`.
- `0 <= obstacles.length <= 10^4`
- `-3 * 10^4 <= x_i, y_i <= 3 * 10^4`
- The answer is guaranteed to be less than `2^31`.

## Examples
### Example 1
- **Input:** `commands = [4,-1,3], obstacles = []`
- **Output:** `25`
- **Explanation:** The robot starts at `(0, 0)`: 

 
 Move north 4 units to `(0, 4)`. 
 Turn right. 
 Move east 3 units to `(3, 4)`. 
 

 The furthest point the robot ever gets from the origin is `(3, 4)`, which squared is `3^2 + 4^2 = 25` units away.

### Example 2
- **Input:** `commands = [4,-1,4,-2,4], obstacles = [[2,4]]`
- **Output:** `65`
- **Explanation:** The robot starts at `(0, 0)`: 

 
 Move north 4 units to `(0, 4)`. 
 Turn right. 
 Move east 1 unit and get blocked by the obstacle at `(2, 4)`, robot is at `(1, 4)`. 
 Turn left. 
 Move north 4 units to `(1, 8)`. 
 

 The furthest point the robot ever gets from the origin is `(1, 8)`, which squared is `1^2 + 8^2 = 65` units away.

### Example 3
- **Input:** `commands = [6,-1,-1,6], obstacles = [[0,0]]`
- **Output:** `36`
- **Explanation:** The robot starts at `(0, 0)`: 

 
 Move north 6 units to `(0, 6)`. 
 Turn right. 
 Turn right. 
 Move south 5 units and get blocked by the obstacle at `(0,0)`, robot is at `(0, 1)`. 
 

 The furthest point the robot ever gets from the origin is `(0, 6)`, which squared is `6^2 = 36` units away.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Walking Robot Simulation**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `commands = [4,-1,3], obstacles = []`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `25`.
4. **Verification:** The robot starts at `(0, 0)`: 

 
 Move north 4 units to `(0, 4)`. 
 Turn right. 
 Move east 3 units to `(3, 4)`. 
 

 The furthest point the robot ever gets from the origin is `(3, 4)`, which squared is `3^2 + 4^2 = 25` units away.

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
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocked = set(map(tuple, obstacles))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
        x = y = d = 0
        best = 0

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d + 3) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(c):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in blocked:
                        break
                    x, y = nx, ny
                    best = max(best, x * x + y * y)
        return best
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
- [2069. Walking Robot Simulation II](../../2001-2500/2069-walking-robot-simulation-ii/)
- [657. Robot Return to Origin](../../0501-1000/0657-robot-return-to-origin/)
- [1041. Robot Bounded In Circle](../../1001-1500/1041-robot-bounded-in-circle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/walking-robot-simulation/)
