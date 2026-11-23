# LeetCode 2624: Snail Traversal

**LeetCode Problem #2624 — Snail Traversal**
Solve LeetCode Snail Traversal using TypeScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Snail Traversal |
| LeetCode | #2624 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Write code that enhances all arrays such that you can call the `snail(rowsCount, colsCount)` method that transforms the 1D array into a 2D array organised in the pattern known as **snail traversal order**. Invalid input values should output an empty array. If `rowsCount * colsCount !== nums.length`, the input is considered invalid.

**Snail traversal order*** *starts at the top left cell with the first value of the current array. It then moves through the entire first column from top to bottom, followed by moving to the next column on the right and traversing it from bottom to top. This pattern continues, alternating the direction of traversal with each column, until the entire current array is covered. For example, when given the input array `[19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15]` with `rowsCount = 5` and `colsCount = 4`, the desired output matrix is shown below. Note that iterating the matrix following the arrows corresponds to the order of numbers in the original array.

## Constraints
- `0 <= nums.length <= 250`
- `1 <= nums[i] <= 1000`
- `1 <= rowsCount <= 250`
- `1 <= colsCount <= 250`

## Examples
### Example 1
- **Input:** `nums = [19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15]
rowsCount = 5
colsCount = 4`
- **Output:** `[
 [19,17,16,15],
 [10,1,14,4],
 [3,2,12,20],
 [7,5,18,11],
 [9,8,6,13]
]`

### Example 2
- **Input:** `nums = [1,2,3,4]
rowsCount = 1
colsCount = 4`
- **Output:** `[[1, 2, 3, 4]]`

### Example 3
- **Input:** `nums = [1,3]
rowsCount = 2
colsCount = 2`
- **Output:** `[]`
- **Explanation:** 2 multiplied by 2 is 4, and the original array [1,3] has a length of 2; therefore, the input is invalid.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Fills the matrix column by column. Even-indexed columns fill top-to-bottom; odd-indexed columns fill bottom-to-top, creating the snail pattern.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15]
rowsCount = 5
colsCount = 4`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[
 [19,17,16,15],
 [10,1,14,4],
 [3,2,12,20],
 [7,5,18,11],
 [9,8,6,13]
]`.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
Array.prototype.snail = function(
    rowsCount: number,
    colsCount: number
): number[][] {
    const nums = this;

    if (rowsCount * colsCount !== nums.length) {
        return [];
    }

    const result: number[][] = Array.from(
        { length: rowsCount },
        () => Array(colsCount)
    );

    let index = 0;

    for (let col = 0; col < colsCount; col++) {
        if (col % 2 === 0) {
            // Top → Bottom
            for (let row = 0; row < rowsCount; row++) {
                result[row][col] = nums[index++];
            }
        } else {
            // Bottom → Top
            for (let row = rowsCount - 1; row >= 0; row--) {
                result[row][col] = nums[index++];
            }
        }
    }

    return result;
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
- [94. Binary Tree Inorder Traversal](../../0001-0500/0094-binary-tree-inorder-traversal/)
- [102. Binary Tree Level Order Traversal](../../0001-0500/0102-binary-tree-level-order-traversal/)
- [103. Binary Tree Zigzag Level Order Traversal](../../0001-0500/0103-binary-tree-zigzag-level-order-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/snail-traversal/)
