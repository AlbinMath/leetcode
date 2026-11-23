# LeetCode 3242: Design Neighbor Sum Service

**LeetCode Problem #3242 — Design Neighbor Sum Service**
Solve LeetCode Design Neighbor Sum Service using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Neighbor Sum Service |
| LeetCode | #3242 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a `n x n` 2D array `grid` containing **distinct** elements in the range `[0, n^2 - 1]`.

Implement the `NeighborSum` class:

`NeighborSum(int [][]grid)` initializes the object. 
 `int adjacentSum(int value)` returns the **sum** of elements which are adjacent neighbors of `value`, that is either to the top, left, right, or bottom of `value` in `grid`. 
 `int diagonalSum(int value)` returns the **sum** of elements which are diagonal neighbors of `value`, that is either to the top-left, top-right, bottom-left, or bottom-right of `value` in `grid`.

## Constraints
- `3 <= n == grid.length == grid[0].length <= 10`
- `0 <= grid[i][j] <= n^2 - 1`
- All `grid[i][j]` are distinct.
- `value` in `adjacentSum` and `diagonalSum` will be in the range `[0, n^2 - 1]`.
- At most `2 * n^2` calls will be made to `adjacentSum` and `diagonalSum`.

## Examples
### Example 1
- **Input:** ``
- **Output:** `[null, 6, 16, 16, 4]`

### Example 2
- **Input:** ``
- **Output:** `[null, 23, 45]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Design Neighbor Sum Service**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with ``.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 6, 16, 16, 4]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var NeighborSum = function(grid) {
    this.grid = grid;
    this.n = grid.length;
    this.pos = new Array(this.n * this.n);
    
    for (let r = 0; r < this.n; r++) {
        for (let c = 0; c < this.n; c++) {
            this.pos[grid[r][c]] = [r, c];
        }
    }
};
NeighborSum.prototype._sumNeighbors = function(value, dirs) {
    const [r, c] = this.pos[value];
    let total = 0;
    
    for (const [dr, dc] of dirs) {
        const nr = r + dr;
        const nc = c + dc;
        if (nr >= 0 && nr < this.n && nc >= 0 && nc < this.n) {
            total += this.grid[nr][nc];
        }
    }
    return total;
};
NeighborSum.prototype.adjacentSum = function(value) {
    return this._sumNeighbors(value, [[-1, 0], [1, 0], [0, -1], [0, 1]]);
};
NeighborSum.prototype.diagonalSum = function(value) {
    return this._sumNeighbors(value, [[-1, -1], [-1, 1], [1, -1], [1, 1]]);
};
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
- [1515. Best Position for a Service Centre](../../1501-2000/1638-best-position-for-a-service-centre/)
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)
- [355. Design Twitter](../../0001-0500/0355-design-twitter/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-neighbor-sum-service/)
