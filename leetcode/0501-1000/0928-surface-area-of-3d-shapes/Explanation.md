# LeetCode 892: Surface Area of 3D Shapes

**LeetCode Problem #892 — Surface Area of 3D Shapes**
Solve LeetCode Surface Area of 3D Shapes using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Surface Area of 3D Shapes |
| LeetCode | #892 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `n x n` `grid` where you have placed some `1 x 1 x 1` cubes. Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of cell `(i, j)`.

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return *the total surface area of the resulting shapes*.

**Note:** The bottom face of each shape counts toward its surface area.

## Constraints
- `n == grid.length == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] <= 50`

## Examples
### Example 1
- **Input:** `grid = [[1,2],[3,4]]`
- **Output:** `34`

### Example 2
- **Input:** `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- **Output:** `32`

### Example 3
- **Input:** `grid = [[2,2,2],[2,1,2],[2,2,2]]`
- **Output:** `46`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Surface Area of 3D Shapes**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2],[3,4]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `34`.

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
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                height = grid[i][j]

                if height == 0:
                    continue

                # Top and bottom faces
                area += 2

                # Four side faces
                area += 4 * height

                # Remove overlapping faces with top neighbor
                if i > 0:
                    area -= 2 * min(height, grid[i - 1][j])

                # Remove overlapping faces with left neighbor
                if j > 0:
                    area -= 2 * min(height, grid[i][j - 1])

        return area
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
- [883. Projection Area of 3D Shapes](../../0501-1000/0919-projection-area-of-3d-shapes/)
- [223. Rectangle Area](../../0001-0500/0223-rectangle-area/)
- [695. Max Area of Island](../../0501-1000/0695-max-area-of-island/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/surface-area-of-3d-shapes/)
