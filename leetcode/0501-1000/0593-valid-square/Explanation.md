# LeetCode 593: Valid Square

**LeetCode Problem #593 — Valid Square**
Solve LeetCode Valid Square using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Square |
| LeetCode | #593 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the coordinates of four points in 2D space `p1`, `p2`, `p3` and `p4`, return `true` *if the four points construct a square*.

The coordinate of a point `p_i` is represented as `[x_i, y_i]`. The input is **not** given in any order.

A **valid square** has four equal sides with positive length and four equal angles (90-degree angles).

## Constraints
- `p1.length == p2.length == p3.length == p4.length == 2`
- `-10^4 <= x_i, y_i <= 10^4`

## Examples
### Example 1
- **Input:** `p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]`
- **Output:** `true`

### Example 2
- **Input:** `p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]`
- **Output:** `false`

### Example 3
- **Input:** `p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]`
- **Output:** `true`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Valid Square**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pts = [p1, p2, p3, p4]
        d = []
        for i in range(4):
            for j in range(i + 1, 4):
                dx = pts[i][0] - pts[j][0]
                dy = pts[i][1] - pts[j][1]
                d.append(dx * dx + dy * dy)
        d.sort()
        return d[0] > 0 and d[0] == d[1] == d[2] == d[3] and d[4] == d[5]
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
- [367. Valid Perfect Square](../../0001-0500/0367-valid-perfect-square/)
- [221. Maximal Square](../../0001-0500/0221-maximal-square/)
- [473. Matchsticks to Square](../../0001-0500/0473-matchsticks-to-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-square/)
