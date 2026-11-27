# LeetCode 4024: Nearest Available Drone

**LeetCode Problem #4024 — Nearest Available Drone**
Solve LeetCode Nearest Available Drone using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Nearest Available Drone |
| LeetCode | #4024 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `drones`, where `drones[i] = [x_i, y_i, range_i]` represents the x-coordinate, y-coordinate, and travel range of the `i^th` drone.

You are also given an integer array `target = [tx, ty]`, representing the coordinates of the target.

A drone `drones[i]` can reach the target if the Manhattan distance between its coordinates and the target coordinates is **less than or equal** to its `range_i`.

Return the **index** of the reachable drone with the **minimum Manhattan distance** to the target. If there is a tie, return the **smallest index**. If no drone can reach the target, return `-1`.

## Constraints
- `1 <= drones.length <= 100`
- `drones[i] = [x_i, y_i, range_i]`
- `target = [tx, ty]`
- `-25 <= x_i, y_i, tx, ty <= 25`
- `1 <= range_i <= 100`

## Examples
### Example 1
- **Input:** `drones = [[0,0,8],[2,2,9]], target = [3,4]`
- **Output:** `1`
- **Explanation:** The distance between `drones[0]` and `target` is `|0 - 3| + |0 - 4| = 7`, which is within its range of 8. 
 The distance between `drones[1]` and `target` is `|2 - 3| + |2 - 4| = 3`, which is within its range of 9. 
 Since `drones[1]` is the nearest drone, the answer is 1.

### Example 2
- **Input:** `drones = [[2,1,5],[4,4,5],[6,6,8]], target = [5,5]`
- **Output:** `1`
- **Explanation:** The distance between `drones[0]` and `target` is `|2 - 5| + |1 - 5| = 7`, which is greater than its range of 5. 
 The distance between `drones[1]` and `target` is `|4 - 5| + |4 - 5| = 2`, which is within its range of 5. 
 The distance between `drones[2]` and `target` is `|6 - 5| + |6 - 5| = 2`, which is within its range of 8. 
 Both `drones[1]` and `drones[2]` are the nearest drones. Since we should return the smallest index, the answer is 1.

### Example 3
- **Input:** `drones = [[4,4,5]], target = [8,6]`
- **Output:** `-1`
- **Explanation:** The distance between `drones[0]` and `target` is `|4 - 8| + |4 - 6| = 6`, which is greater than its range of 5. 
 No drone can reach the target, so the answer is -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Nearest Available Drone**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `drones = [[0,0,8],[2,2,9]], target = [3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The distance between `drones[0]` and `target` is `|0 - 3| + |0 - 4| = 7`, which is within its range of 8. 
 The distance between `drones[1]` and `target` is `|2 - 3| + |2 - 4| = 3`, which is within its range of 9. 
 Since `drones[1]` is the nearest drone, the answer is 1.

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
    def nearestDrone(self, drones: List[List[int]], target: List[int]) -> int:
        tx, ty = target
        best_idx = -1
        best_dist = float('inf')
        for i, (x, y, r) in enumerate(drones):
            d = abs(x - tx) + abs(y - ty)
            if d <= r and d < best_dist:
                best_dist = d
                best_idx = i
        return best_idx
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
- [999. Available Captures for Rook](../../0501-1000/0999-available-captures-for-rook/)
- [3570. Find Books with No Available Copies](../../3501-4000/3570-find-books-with-no-available-copies/)
- [1779. Find Nearest Point That Has the Same X or Y Coordinate](../../1501-2000/1779-find-nearest-point-that-has-the-same-x-or-y-coordinate/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/nearest-available-drone/)
