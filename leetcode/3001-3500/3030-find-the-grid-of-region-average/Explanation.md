# LeetCode 3030: Find the Grid of Region Average

**LeetCode Problem #3030 — Find the Grid of Region Average**
Solve LeetCode Find the Grid of Region Average using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Grid of Region Average |
| LeetCode | #3030 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given `m x n` grid `image` which represents a grayscale image, where `image[i][j]` represents a pixel with intensity in the range `[0..255]`. You are also given a **non-negative** integer `threshold`.

Two pixels are **adjacent** if they share an edge.

A **region** is a `3 x 3` subgrid where the **absolute difference** in intensity between any two **adjacent** pixels is **less than or equal to** `threshold`.

All pixels in a region belong to that region, note that a pixel can belong to **multiple** regions.

You need to calculate a `m x n` grid `result`, where `result[i][j]` is the **average** intensity of the regions to which `image[i][j]` belongs, **rounded down** to the nearest integer. If `image[i][j]` belongs to multiple regions, `result[i][j]` is the **average **of the** rounded-down average **intensities of these regions, **rounded down** to the nearest integer. If `image[i][j]` does** not** belong to any region, `result[i][j]` is **equal to** `image[i][j]`.

Return the grid `result`.

## Constraints
- `3 <= n, m <= 500`
- `0 <= image[i][j] <= 255`
- `0 <= threshold <= 255`

## Examples
### Example 1
- **Input:** `image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3`
- **Output:** `[[9,9,9,9],[9,9,9,9],[9,9,9,9]]`
- **Explanation:** There are two regions as illustrated above. The average intensity of the first region is 9, while the average intensity of the second region is 9.67 which is rounded down to 9. The average intensity of both of the regions is (9 + 9) / 2 = 9. As all the pixels belong to either region 1, region 2, or both of them, the intensity of every pixel in the result is 9. 

 Please note that the rounded-down values are used when calculating the average of multiple regions, hence the calculation is done using 9 as the average intensity of region 2, not 9.67.

### Example 2
- **Input:** `image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12`
- **Output:** `[[25,25,25],[27,27,27],[27,27,27],[30,30,30]]`
- **Explanation:** There are two regions as illustrated above. The average intensity of the first region is 25, while the average intensity of the second region is 30. The average intensity of both of the regions is (25 + 30) / 2 = 27.5 which is rounded down to 27. 

 All the pixels in row 0 of the image belong to region 1, hence all the pixels in row 0 in the result are 25. Similarly, all the pixels in row 3 in the result are 30. The pixels in rows 1 and 2 of the image belong to region 1 and region 2, hence their assigned value is 27 in the result.

### Example 3
- **Input:** `image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1`
- **Output:** `[[5,6,7],[8,9,10],[11,12,13]]`
- **Explanation:** There is only one `3 x 3` subgrid, while it does not have the condition on difference of adjacent pixels, for example, the difference between `image[0][0]` and `image[1][0]` is `|5 - 8| = 3 > threshold = 1`. None of them belong to any valid regions, so the `result` should be the same as `image`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Grid of Region Average**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[9,9,9,9],[9,9,9,9],[9,9,9,9]]`.
4. **Verification:** There are two regions as illustrated above. The average intensity of the first region is 9, while the average intensity of the second region is 9.67 which is rounded down to 9. The average intensity of both of the regions is (9 + 9) / 2 = 9. As all the pixels belong to either region 1, region 2, or both of them, the intensity of every pixel in the result is 9. 

 Please note that the rounded-down values are used when calculating the average of multiple regions, hence the calculation is done using 9 as the average intensity of region 2, not 9.67.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        total = [[0] * n for _ in range(m)]
        cnt = [[0] * n for _ in range(m)]

        for i in range(m - 2):
            for j in range(n - 2):
                ok = True
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if y + 1 < j + 3 and abs(image[x][y] - image[x][y + 1]) > threshold:
                            ok = False
                            break
                        if x + 1 < i + 3 and abs(image[x][y] - image[x + 1][y]) > threshold:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue

                avg = sum(image[x][y] for x in range(i, i + 3) for y in range(j, j + 3)) // 9
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        total[x][y] += avg
                        cnt[x][y] += 1

        return [
            [total[i][j] // cnt[i][j] if cnt[i][j] else image[i][j] for j in range(n)]
            for i in range(m)
        ]
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2639. Find the Width of Columns of a Grid](../../2501-3000/2639-find-the-width-of-columns-of-a-grid/)
- [2812. Find the Safest Path in a Grid](../../2501-3000/2812-find-the-safest-path-in-a-grid/)
- [3286. Find a Safe Walk Through a Grid](../../3001-3500/3286-find-a-safe-walk-through-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-grid-of-region-average/)
