# LeetCode 1007: Minimum Domino Rotations For Equal Row

**LeetCode Problem #1007 — Minimum Domino Rotations For Equal Row**
Solve LeetCode Minimum Domino Rotations For Equal Row using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Domino Rotations For Equal Row |
| LeetCode | #1007 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
In a row of dominoes, `tops[i]` and `bottoms[i]` represent the top and bottom halves of the `i^th` domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the `i^th` domino, so that `tops[i]` and `bottoms[i]` swap values.

Return the minimum number of rotations so that all the values in `tops` are the same, or all the values in `bottoms` are the same.

If it cannot be done, return `-1`.

## Constraints
- `2 <= tops.length <= 2 * 10^4`
- `bottoms.length == tops.length`
- `1 <= tops[i], bottoms[i] <= 6`

## Examples
### Example 1
- **Input:** `tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]`
- **Output:** `2`
- **Explanation:** The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

### Example 2
- **Input:** `tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]`
- **Output:** `-1`
- **Explanation:** In this case, it is not possible to rotate the dominoes to make one row of values equal.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Domino Rotations For Equal Row**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

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
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        def check(x: int) -> int:
            rot_top = rot_bottom = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return -1
                if t != x:
                    rot_top += 1      # must rotate to bring x to the top
                elif b != x:
                    rot_bottom += 1   # must rotate to bring x to the bottom
            return min(rot_top, rot_bottom)

        r = check(tops[0])
        if r != -1:
            return r
        return check(bottoms[0])
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
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../../0001-0500/0462-minimum-moves-to-equal-array-elements-ii/)
- [1247. Minimum Swaps to Make Strings Equal](../../1001-1500/1247-minimum-swaps-to-make-strings-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)
