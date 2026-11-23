# LeetCode 1776: Car Fleet II

**LeetCode Problem #1776 — Car Fleet II**
Solve LeetCode Car Fleet II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Car Fleet II |
| LeetCode | #1776 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` cars traveling at different speeds in the same direction along a one-lane road. You are given an array `cars` of length `n`, where `cars[i] = [position_i, speed_i]` represents:

`position_i` is the distance between the `i^th` car and the beginning of the road in meters. It is guaranteed that `position_i < position_i+1`. 
 `speed_i` is the initial speed of the `i^th` car in meters per second.

For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the **slowest** car in the fleet.

Return an array `answer`, where `answer[i]` is the time, in seconds, at which the `i^th` car collides with the next car, or `-1` if the car does not collide with the next car. Answers within `10^-5` of the actual answers are accepted.

## Constraints
- `1 <= cars.length <= 10^5`
- `1 <= position_i, speed_i <= 10^6`
- `position_i < position_i+1`

## Examples
### Example 1
- **Input:** `cars = [[1,2],[2,1],[4,3],[7,2]]`
- **Output:** `[1.00000,-1.00000,3.00000,-1.00000]`
- **Explanation:** After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.

### Example 2
- **Input:** `cars = [[3,4],[5,4],[6,3],[9,1]]`
- **Output:** `[2.00000,1.00000,1.50000,-1.00000]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Car Fleet II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `cars = [[1,2],[2,1],[4,3],[7,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1.00000,-1.00000,3.00000,-1.00000]`.
4. **Verification:** After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            p, s = cars[i]
            while stack:
                j = stack[-1]
                pj, sj = cars[j]
                if s <= sj:
                    stack.pop()
                    continue
                t = (pj - p) / (s - sj)
                if ans[j] != -1 and t > ans[j]:
                    stack.pop()
                    continue
                ans[i] = t
                break
            stack.append(i)

        return ans
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [853. Car Fleet](../../0501-1000/0883-car-fleet/)
- [818. Race Car](../../0501-1000/0836-race-car/)
- [1094. Car Pooling](../../1001-1500/1184-car-pooling/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/car-fleet-ii/)
