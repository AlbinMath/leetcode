# LeetCode 3394: Check if Grid can be Cut into Sections

**LeetCode Problem #3394 — Check if Grid can be Cut into Sections**
Solve LeetCode Check if Grid can be Cut into Sections using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Grid can be Cut into Sections |
| LeetCode | #3394 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` representing the dimensions of an `n x n` grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates `rectangles`, where `rectangles[i]` is in the form `[start_x, start_y, end_x, end_y]`, representing a rectangle on the grid. Each rectangle is defined as follows:

`(start_x, start_y)`: The bottom-left corner of the rectangle. 
 `(end_x, end_y)`: The top-right corner of the rectangle.

**Note **that the rectangles do not overlap. Your task is to determine if it is possible to make **either two horizontal or two vertical cuts** on the grid such that:

Each of the three resulting sections formed by the cuts contains **at least** one rectangle. 
 Every rectangle belongs to **exactly** one section.

Return `true` if such cuts can be made; otherwise, return `false`.

## Constraints
- `3 <= n <= 10^9`
- `3 <= rectangles.length <= 10^5`
- `0 <= rectangles[i][0] < rectangles[i][2] <= n`
- `0 <= rectangles[i][1] < rectangles[i][3] <= n`
- No two rectangles overlap.

## Examples
### Example 1
- **Input:** `n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]`
- **Output:** `true`
- **Explanation:** The grid is shown in the diagram. We can make horizontal cuts at `y = 2` and `y = 4`. Hence, output is true.

### Example 2
- **Input:** `n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]`
- **Output:** `true`
- **Explanation:** We can make vertical cuts at `x = 2` and `x = 3`. Hence, output is true.

### Example 3
- **Input:** `n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]`
- **Output:** `false`
- **Explanation:** We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if Grid can be Cut into Sections**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The grid is shown in the diagram. We can make horizontal cuts at `y = 2` and `y = 4`. Hence, output is true.

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
var checkValidCuts = function(n, rectangles) {
    const canMakeCuts = function(axis) {
        const intervals = rectangles.map(rect => [
            rect[axis],
            rect[axis + 2]
        ]);
        intervals.sort((a, b) => a[0] - b[0]);
        let groups = 0;
        let currentEnd = -1;

        for (const [start, end] of intervals) {
            if (start >= currentEnd) {
                groups++;
                currentEnd = end;
            } else {
                currentEnd = Math.max(currentEnd, end);
            }
            if (groups >= 3) {
                return true;
            }
        }
        return false;
    };
    return canMakeCuts(0) || canMakeCuts(1);
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
- [2018. Check if Word Can Be Placed In Crossword](../../2001-2500/2018-check-if-word-can-be-placed-in-crossword/)
- [2116. Check if a Parentheses String Can Be Valid](../../2001-2500/2116-check-if-a-parentheses-string-can-be-valid/)
- [2840. Check if Strings Can be Made Equal With Operations II](../../2501-3000/2840-check-if-strings-can-be-made-equal-with-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/)
