# LeetCode 1861: Rotating the Box

**LeetCode Problem #1861 — Rotating the Box**
Solve LeetCode Rotating the Box using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rotating the Box |
| LeetCode | #1861 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` matrix of characters `boxGrid` representing a side-view of a box. Each cell of the box is one of the following:

A stone `'#'` 
 A stationary obstacle `'*'` 
 Empty `'.'`

The box is rotated **90 degrees clockwise**, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity **does not** affect the obstacles' positions, and the inertia from the box's rotation **does not **affect the stones' horizontal positions.

It is **guaranteed** that each stone in `boxGrid` rests on an obstacle, another stone, or the bottom of the box.

Return *an *`n x m`* matrix representing the box after the rotation described above*.

## Constraints
- `m == boxGrid.length`
- `n == boxGrid[i].length`
- `1 <= m, n <= 500`
- `boxGrid[i][j]` is either `'#'`, `'*'`, or `'.'`.

## Examples
### Example 1
- **Input:** `boxGrid = [["#",".","#"]]`
- **Output:** `[["."],
 ["#"],
 ["#"]]`

### Example 2
- **Input:** `boxGrid = [["#",".","*","."],
 ["#","#","*","."]]`
- **Output:** `[["#","."],
 ["#","#"],
 ["*","*"],
 [".","."]]`

### Example 3
- **Input:** `boxGrid = [["#","#","*",".","*","."],
 ["#","#","#","*",".","."],
 ["#","#","#",".","#","."]]`
- **Output:** `[[".","#","#"],
 [".","#","#"],
 ["#","#","*"],
 ["#","*","."],
 ["#",".","*"],
 ["#",".","."]]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
1. **Apply Gravity (rightward):** Before rotating, simulate gravity in each row by moving stones as far right as possible, stopping at obstacles or the edge.
2. **Rotate 90° Clockwise:** Create a new matrix where `result[j][m-1-i] = box[i][j]`.

Time complexity is $O(M \times N)$ and space complexity is $O(M \times N)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `boxGrid = [["#",".","#"]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["."],
 ["#"],
 ["#"]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        int m = boxGrid.size();
        int n = boxGrid[0].size();

        // 1. Let stones fall to the right
        for (int i = 0; i < m; i++) {
            int empty = n - 1;

            for (int j = n - 1; j >= 0; j--) {
                if (boxGrid[i][j] == '*') {
                    empty = j - 1;
                }
                else if (boxGrid[i][j] == '#') {
                    boxGrid[i][j] = '.';
                    boxGrid[i][empty] = '#';
                    empty--;
                }
            }
        }

        // 2. Rotate 90 degrees clockwise
        vector<vector<char>> result(n, vector<char>(m));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result[j][m - 1 - i] = boxGrid[i][j];
            }
        }

        return result;
    }
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
- [1914. Cyclically Rotating a Grid](../../2001-2500/2043-cyclically-rotating-a-grid/)
- [1263. Minimum Moves to Move a Box to Their Target Location](../../1001-1500/1389-minimum-moves-to-move-a-box-to-their-target-location/)
- [1742. Maximum Number of Balls in a Box](../../1501-2000/1844-maximum-number-of-balls-in-a-box/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotating-the-box/)
