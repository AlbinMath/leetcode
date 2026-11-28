# LeetCode 849: Maximize Distance to Closest Person

**LeetCode Problem #849 — Maximize Distance to Closest Person**
Solve LeetCode Maximize Distance to Closest Person using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Distance to Closest Person |
| LeetCode | #849 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array representing a row of `seats` where `seats[i] = 1` represents a person sitting in the `i^th` seat, and `seats[i] = 0` represents that the `i^th` seat is empty **(0-indexed)**.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return *that maximum distance to the closest person*.

## Constraints
- `2 <= seats.length <= 2 * 10^4`
- `seats[i]` is `0` or `1`.
- At least one seat is **empty**.
- At least one seat is **occupied**.

## Examples
### Example 1
- **Input:** `seats = [1,0,0,0,1,0,1]`
- **Output:** `2`
- **Explanation:** If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

### Example 2
- **Input:** `seats = [1,0,0,0]`
- **Output:** `3`
- **Explanation:** If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

### Example 3
- **Input:** `seats = [0,1]`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Distance to Closest Person**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `seats = [1,0,0,0,1,0,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

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
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        prev = -1
        max_dist = 0
        
        for i, seat in enumerate(seats):
            if seat == 1:
                if prev == -1:
                    max_dist = i
                else:
                    max_dist = max(max_dist, (i - prev) // 2)
                prev = i
        return max(max_dist, n - 1 - prev)
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
- [3464. Maximize the Distance Between Points on a Square](../../3001-3500/3464-maximize-the-distance-between-points-on-a-square/)
- [72. Edit Distance](../../0001-0500/0072-edit-distance/)
- [461. Hamming Distance](../../0001-0500/0461-hamming-distance/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-distance-to-closest-person/)
