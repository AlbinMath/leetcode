# LeetCode 1914: Cyclically Rotating a Grid

**LeetCode Problem #1914 — Cyclically Rotating a Grid**
Solve LeetCode Cyclically Rotating a Grid using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cyclically Rotating a Grid |
| LeetCode | #1914 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` integer matrix `grid`​​​, where `m` and `n` are both **even** integers, and an integer `k`.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:

A cyclic rotation of the matrix is done by cyclically rotating **each layer** in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the **counter-clockwise** direction. An example rotation is shown below:

Return *the matrix after applying *`k` *cyclic rotations to it*.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 50`
- Both `m` and `n` are **even** integers.
- `1 <= grid[i][j] <=^ 5000`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `grid = [[40,10],[30,20]], k = 1`
- **Output:** `[[10,20],[40,30]]`
- **Explanation:** The figures above represent the grid at every state.

### Example 2
- **Input:** `grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2`
- **Output:** `[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]`
- **Explanation:** The figures above represent the grid at every state.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
1. **Extract Layers:** For each concentric ring of the grid, extract the elements into a 1D array by traversing the ring clockwise.
2. **Rotate:** Rotate the 1D array by `k % length` positions.
3. **Place Back:** Write the rotated elements back into the corresponding positions in the grid.

Time complexity is $O(M \times N)$ and space complexity is $O(M \times N)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[40,10],[30,20]], k = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[10,20],[40,30]]`.
4. **Verification:** The figures above represent the grid at every state.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        for (int layer = 0; layer < min(m, n) / 2; layer++) {
            vector<int> elements;

            int top = layer;
            int bottom = m - 1 - layer;
            int left = layer;
            int right = n - 1 - layer;

            // Top row
            for (int j = left; j <= right; j++)
                elements.push_back(grid[top][j]);

            // Right column
            for (int i = top + 1; i <= bottom; i++)
                elements.push_back(grid[i][right]);

            // Bottom row
            for (int j = right - 1; j >= left; j--)
                elements.push_back(grid[bottom][j]);

            // Left column
            for (int i = bottom - 1; i > top; i--)
                elements.push_back(grid[i][left]);

            int len = elements.size();
            int shift = k % len;

            int idx = 0;

            // Top row
            for (int j = left; j <= right; j++)
                grid[top][j] = elements[(idx++ + shift) % len];

            // Right column
            for (int i = top + 1; i <= bottom; i++)
                grid[i][right] = elements[(idx++ + shift) % len];

            // Bottom row
            for (int j = right - 1; j >= left; j--)
                grid[bottom][j] = elements[(idx++ + shift) % len];

            // Left column
            for (int i = bottom - 1; i > top; i--)
                grid[i][left] = elements[(idx++ + shift) % len];
        }

        return grid;
    }
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
- [4052. Cyclically Shift Rows and Columns](../../4001-4500/4052-cyclically-shift-rows-and-columns/)
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)
- [1001. Grid Illumination](../../1001-1500/1001-grid-illumination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cyclically-rotating-a-grid/)
