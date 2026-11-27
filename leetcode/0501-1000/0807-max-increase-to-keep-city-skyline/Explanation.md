# LeetCode 807: Max Increase to Keep City Skyline

**LeetCode Problem #807 — Max Increase to Keep City Skyline**
Solve LeetCode Max Increase to Keep City Skyline using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Increase to Keep City Skyline |
| LeetCode | #807 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a city composed of `n x n` blocks, where each block contains a single building shaped like a vertical square prism. You are given a **0-indexed** `n x n` integer matrix `grid` where `grid[r][c]` represents the **height** of the building located in the block at row `r` and column `c`.

A city's **skyline** is the outer contour formed by all the building when viewing the side of the city from a distance. The **skyline** from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of **any number of buildings by any amount** (the amount can be different per building). The height of a `0`-height building can also be increased. However, increasing the height of a building should **not** affect the city's **skyline** from any cardinal direction.

Return *the **maximum total sum** that the height of the buildings can be increased by **without** changing the city's **skyline** from any cardinal direction*.

## Constraints
- `n == grid.length`
- `n == grid[r].length`
- `2 <= n <= 50`
- `0 <= grid[r][c] <= 100`

## Examples
### Example 1
- **Input:** `grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]`
- **Output:** `35`
- **Explanation:** The building heights are shown in the center of the above image.
The skylines when viewed from each cardinal direction are drawn in red.
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
 [7, 4, 7, 7],
 [9, 4, 8, 7],
 [3, 3, 3, 3] ]

### Example 2
- **Input:** `grid = [[0,0,0],[0,0,0],[0,0,0]]`
- **Output:** `0`
- **Explanation:** Increasing the height of any building will result in the skyline changing.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Max Increase to Keep City Skyline**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `35`.
4. **Verification:** The building heights are shown in the center of the above image.
The skylines when viewed from each cardinal direction are drawn in red.
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
 [7, 4, 7, 7],
 [9, 4, 8, 7],
 [3, 3, 3, 3] ]

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxIncreaseKeepingSkyline = function(grid) {
    const n = grid.length;
    const rowMax = new Array(n).fill(0);
    const colMax = new Array(n).fill(0);

    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            const val = grid[r][c];
            if (val > rowMax[r]) rowMax[r] = val;
            if (val > colMax[c]) colMax[c] = val;
        }
    }

    let totalIncrease = 0;
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            totalIncrease += Math.min(rowMax[r], colMax[c]) - grid[r][c];
        }
    }

    return totalIncrease;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](../../1501-2000/1579-remove-max-number-of-edges-to-keep-graph-fully-traversable/)
- [218. The Skyline Problem](../../0001-0500/0218-the-skyline-problem/)
- [3891. Minimum Increase to Maximize Special Indices](../../3501-4000/3891-minimum-increase-to-maximize-special-indices/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-increase-to-keep-city-skyline/)
