# LeetCode 794: Valid Tic-Tac-Toe State

**LeetCode Problem #794 — Valid Tic-Tac-Toe State**
Solve LeetCode Valid Tic-Tac-Toe State using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Tic-Tac-Toe State |
| LeetCode | #794 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a Tic-Tac-Toe board as a string array `board`, return `true` if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a `3 x 3` array that consists of characters `' '`, `'X'`, and `'O'`. The `' '` character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares `' '`. 
 The first player always places `'X'` characters, while the second player always places `'O'` characters. 
 `'X'` and `'O'` characters are always placed into empty squares, never filled ones. 
 The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal. 
 The game also ends if all squares are non-empty. 
 No more moves can be played if the game is over.

## Constraints
- `board.length == 3`
- `board[i].length == 3`
- `board[i][j]` is either `'X'`, `'O'`, or `' '`.

## Examples
### Example 1
- **Input:** `board = ["O "," "," "]`
- **Output:** `false`
- **Explanation:** The first player always plays "X".

### Example 2
- **Input:** `board = ["XOX"," X "," "]`
- **Output:** `false`
- **Explanation:** Players take turns making moves.

### Example 3
- **Input:** `board = ["XOX","O O","XOX"]`
- **Output:** `true`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Valid Tic-Tac-Toe State**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = ["O "," "," "]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** The first player always plays "X".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var validTicTacToe = function(board) {
    let xCount = 0;
    let oCount = 0;

    for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 3; c++) {
            if (board[r][c] === 'X') xCount++;
            else if (board[r][c] === 'O') oCount++;
        }
    }

    // Turn order check: X moves first, so xCount is either oCount or oCount + 1
    if (xCount !== oCount && xCount !== oCount + 1) {
        return false;
    }

    const hasWon = (p) => {
        for (let i = 0; i < 3; i++) {
            if (board[i][0] === p && board[i][1] === p && board[i][2] === p) return true;
            if (board[0][i] === p && board[1][i] === p && board[2][i] === p) return true;
        }
        return (
            (board[0][0] === p && board[1][1] === p && board[2][2] === p) ||
            (board[0][2] === p && board[1][1] === p && board[2][0] === p)
        );
    };

    const xWins = hasWon('X');
    const oWins = hasWon('O');

    // If X won, the game ended on X's turn
    if (xWins && xCount !== oCount + 1) return false;
    // If O won, the game ended on O's turn
    if (oWins && xCount !== oCount) return false;

    return true;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1275. Find Winner on a Tic Tac Toe Game](../../1001-1500/1400-find-winner-on-a-tic-tac-toe-game/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [20. Valid Parentheses](../../0001-0500/0020-valid-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-tic-tac-toe-state/)
