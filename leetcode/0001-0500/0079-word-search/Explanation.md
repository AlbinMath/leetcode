# LeetCode 79: Word Search

**LeetCode Problem #79 — Word Search**
Solve LeetCode Word Search using JavaScript, PHP and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Word Search |
| LeetCode | #79 |
| Difficulty | Medium |
| Language | JavaScript, PHP |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Constraints
- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

## Examples
### Example 1
- **Input:** `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"`
- **Output:** `true`

### Example 2
- **Input:** `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"`
- **Output:** `true`

### Example 3
- **Input:** `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"`
- **Output:** `false`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Word Search**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
JavaScript, PHP

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)


### JavaScript
```javascript
var exist = function(board, word) {
    const rows = board.length;
    const cols = board[0].length;

    function dfs(r, c, index) {
        // All characters matched
        if (index === word.length) {
            return true;
        }

        // Out of bounds or character doesn't match
        if (
            r < 0 || r >= rows ||
            c < 0 || c >= cols ||
            board[r][c] !== word[index]
        ) {
            return false;
        }

        // Mark the cell as visited
        const temp = board[r][c];
        board[r][c] = "#";

        // Explore four adjacent cells
        const found =
            dfs(r + 1, c, index + 1) ||
            dfs(r - 1, c, index + 1) ||
            dfs(r, c + 1, index + 1) ||
            dfs(r, c - 1, index + 1);

        // Restore the original character
        board[r][c] = temp;

        return found;
    }

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (dfs(r, c, 0)) {
                return true;
            }
        }
    }

    return false;
};
```

### PHP
```php
class Solution {
    function exist($board, $word) {
        $rows = count($board);
        $cols = count($board[0]);

        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {

                if ($this->dfs($board, $word, $r, $c, 0, $rows, $cols)) {
                    return true;
                }
            }
        }

        return false;
    }

    function dfs(&$board, $word, $row, $col, $index, $rows, $cols) {

        // All characters matched
        if ($index == strlen($word)) {
            return true;
        }

        // Out of bounds
        if ($row < 0 || $row >= $rows ||
            $col < 0 || $col >= $cols) {
            return false;
        }

        // Current character doesn't match
        if ($board[$row][$col] != $word[$index]) {
            return false;
        }

        // Mark as visited
        $temp = $board[$row][$col];
        $board[$row][$col] = '#';

        // Search four directions
        $found =
            $this->dfs($board, $word, $row + 1, $col, $index + 1, $rows, $cols) ||
            $this->dfs($board, $word, $row - 1, $col, $index + 1, $rows, $cols) ||
            $this->dfs($board, $word, $row, $col + 1, $index + 1, $rows, $cols) ||
            $this->dfs($board, $word, $row, $col - 1, $index + 1, $rows, $cols);

        // Restore cell
        $board[$row][$col] = $temp;

        return $found;
    }
}
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
- [212. Word Search II](../../0001-0500/0212-word-search-ii/)
- [58. Length of Last Word](../../0001-0500/0058-length-of-last-word/)
- [126. Word Ladder II](../../0001-0500/0126-word-ladder-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/word-search/)
