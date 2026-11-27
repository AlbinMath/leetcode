# LeetCode 2943: Maximize Area of Square Hole in Grid

**LeetCode Problem #2943 — Maximize Area of Square Hole in Grid**
Solve LeetCode Maximize Area of Square Hole in Grid using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Area of Square Hole in Grid |
| LeetCode | #2943 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given the two integers, `n` and `m` and two integer arrays, `hBars` and `vBars`. The grid has `n + 2` horizontal and `m + 2` vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from `1`.

You can **remove** some of the bars in `hBars` from horizontal bars and some of the bars in `vBars` from vertical bars. Note that other bars are fixed and cannot be removed.

Return an integer denoting the **maximum area** of a *square-shaped* hole in the grid, after removing some bars (possibly none).

## Constraints
- `1 <= n <= 10^9`
- `1 <= m <= 10^9`
- `1 <= hBars.length <= 100`
- `2 <= hBars[i] <= n + 1`
- `1 <= vBars.length <= 100`
- `2 <= vBars[i] <= m + 1`
- All values in `hBars` are distinct.
- All values in `vBars` are distinct.

## Examples
### Example 1
- **Input:** `n = 2, m = 1, hBars = [2,3], vBars = [2]`
- **Output:** `4`
- **Explanation:** The left image shows the initial grid formed by the bars. The horizontal bars are `[1,2,3,4]`, and the vertical bars are `[1,2,3]`. 

 One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

### Example 2
- **Input:** `n = 1, m = 1, hBars = [2], vBars = [2]`
- **Output:** `4`
- **Explanation:** To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.

### Example 3
- **Input:** `n = 2, m = 3, hBars = [2,3], vBars = [2,4]`
- **Output:** `4`
- **Explanation:** One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Area of Square Hole in Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, m = 1, hBars = [2,3], vBars = [2]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The left image shows the initial grid formed by the bars. The horizontal bars are `[1,2,3,4]`, and the vertical bars are `[1,2,3]`. 

 One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximizeSquareHoleArea = function(n, m, hBars, vBars) {
    const getMaxGap = function(bars) {
        bars.sort((a, b) => a - b);

        let maxConsecutive = 1;
        let currentConsecutive = 1;

        for (let i = 1; i < bars.length; i++) {
            if (bars[i] === bars[i - 1] + 1) {
                currentConsecutive++;
            } else {
                currentConsecutive = 1;
            }

            maxConsecutive = Math.max(
                maxConsecutive,
                currentConsecutive
            );
        }

        return maxConsecutive + 1;
    };

    const horizontalGap = getMaxGap(hBars);
    const verticalGap = getMaxGap(vBars);

    const side = Math.min(horizontalGap, verticalGap);

    return side * side;
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2975. Maximum Square Area by Removing Fences From a Field](../../2501-3000/2975-maximum-square-area-by-removing-fences-from-a-field/)
- [3047. Find the Largest Area of Square Inside Two Rectangles](../../3001-3500/3047-find-the-largest-area-of-square-inside-two-rectangles/)
- [4016. Maximum Area of Two Non-Overlapping Square Submatrices](../../4001-4500/4016-maximum-area-of-two-non-overlapping-square-submatrices/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/)
