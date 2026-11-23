# LeetCode 48: Rotate Image

**LeetCode Problem #48 — Rotate Image**
Solve LeetCode Rotate Image using C++, JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n²) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rotate Image |
| LeetCode | #48 |
| Difficulty | Medium |
| Language | C++, JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n²) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image **in-place** , which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

## Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Examples
### Example 1
- **Input:** `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `[[7,4,1],[8,5,2],[9,6,3]]`

### Example 2
- **Input:** `matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]`
- **Output:** `[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code performs the rotation in two elegant steps:

1. **Transpose the Matrix:** Swap `matrix[i][j]` with `matrix[j][i]` for all elements above the main diagonal (`j > i`). This converts rows into columns. After transposing, `[[1,2,3],[4,5,6],[7,8,9]]` becomes `[[1,4,7],[2,5,8],[3,6,9]]`.
2. **Reverse Each Row:** Reverse every row of the transposed matrix. After reversing, `[[1,4,7],[2,5,8],[3,6,9]]` becomes `[[7,4,1],[8,5,2],[9,6,3]]`, which is the 90-degree clockwise rotation.

This is mathematically equivalent to a 90° clockwise rotation because: Rotate90°(M) = Reverse(Transpose(M)). Time complexity is $O(N^2)$ and space complexity is $O(1)$ since everything is done in-place.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[1,2,3],[4,5,6],[7,8,9]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[7,4,1],[8,5,2],[9,6,3]]`.

## Complexity Analysis
- **Time Complexity:** O(n²) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
C++, JavaScript

## Source Code
- [solution.cpp](./solution.cpp)
- [solution.js](./solution.js)


### C++
```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        // Step 1: Transpose the matrix
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        // Step 2: Reverse every row
        for (int i = 0; i < n; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
```

### JavaScript
```javascript
var rotate = function(matrix) {
    const n = matrix.length;

    // Step 1: Transpose the matrix
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            [matrix[i][j], matrix[j][i]] =
                [matrix[j][i], matrix[i][j]];
        }
    }

    // Step 2: Reverse each row
    for (let i = 0; i < n; i++) {
        matrix[i].reverse();
    }
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
- [61. Rotate List](../../0001-0500/0061-rotate-list/)
- [189. Rotate Array](../../0001-0500/0189-rotate-array/)
- [396. Rotate Function](../../0001-0500/0396-rotate-function/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotate-image/)
