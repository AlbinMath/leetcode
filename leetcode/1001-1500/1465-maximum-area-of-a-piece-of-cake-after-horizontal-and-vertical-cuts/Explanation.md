# LeetCode 1465: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

**LeetCode Problem #1465 — Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts**
Solve LeetCode Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts |
| LeetCode | #1465 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a rectangular cake of size `h x w` and two arrays of integers `horizontalCuts` and `verticalCuts` where:

`horizontalCuts[i]` is the distance from the top of the rectangular cake to the `i^th` horizontal cut and similarly, and 
 `verticalCuts[j]` is the distance from the left of the rectangular cake to the `j^th` vertical cut.

Return *the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays* `horizontalCuts` *and* `verticalCuts`. Since the answer can be a large number, return this **modulo** `10^9 + 7`.

## Constraints
- `2 <= h, w <= 10^9`
- `1 <= horizontalCuts.length <= min(h - 1, 10^5)`
- `1 <= verticalCuts.length <= min(w - 1, 10^5)`
- `1 <= horizontalCuts[i] < h`
- `1 <= verticalCuts[i] < w`
- All the elements in `horizontalCuts` are distinct.
- All the elements in `verticalCuts` are distinct.

## Examples
### Example 1
- **Input:** `h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]`
- **Output:** `4`
- **Explanation:** The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

### Example 2
- **Input:** `h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]`
- **Output:** `6`
- **Explanation:** The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.

### Example 3
- **Input:** `h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]`
- **Output:** `9`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

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
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7

        def max_gap(cuts: List[int], limit: int) -> int:
            cuts = sorted(cuts)
            best = cuts[0]  # gap from 0 to the first cut
            for i in range(1, len(cuts)):
                best = max(best, cuts[i] - cuts[i - 1])
            return max(best, limit - cuts[-1])  # gap from the last cut to the edge

        return (max_gap(horizontalCuts, h) * max_gap(verticalCuts, w)) % MOD
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
- [1637. Widest Vertical Area Between Two Points Containing No Points](../../1501-2000/1637-widest-vertical-area-between-two-points-containing-no-points/)
- [2975. Maximum Square Area by Removing Fences From a Field](../../2501-3000/2975-maximum-square-area-by-removing-fences-from-a-field/)
- [3380. Maximum Area Rectangle With Point Constraints I](../../3001-3500/3380-maximum-area-rectangle-with-point-constraints-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)
