# LeetCode 909: Snakes and Ladders

**LeetCode Problem #909 — Snakes and Ladders**
Solve LeetCode Snakes and Ladders using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Snakes and Ladders |
| LeetCode | #909 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to `n^2` in a **Boustrophedon style** starting from the bottom left of the board (i.e. `board[n - 1][0]`) and alternating direction each row.

You start on square `1` of the board. In each move, starting from square `curr`, do the following:

Choose a destination square `next` with a label in the range `[curr + 1, min(curr + 6, n^2)]`.

This choice simulates the result of a standard **6-sided die roll**: i.e., there are always at most 6 destinations, regardless of the size of the board. 
 
 
 If `next` has a snake or ladder, you **must** move to the destination of that snake or ladder. Otherwise, you move to `next`. 
 The game ends when you reach the square `n^2`.

A board square on row `r` and column `c` has a snake or ladder if `board[r][c] != -1`. The destination of that snake or ladder is `board[r][c]`. Squares `1` and `n^2` are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do **not** follow the subsequent snake or ladder.

For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first move, your destination square is `2`. You follow the ladder to square `3`, but do **not** follow the subsequent ladder to `4`.

Return *the least number of dice rolls required to reach the square *`n^2`*. If it is not possible to reach the square, return *`-1`.

## Constraints
- `n == board.length == board[i].length`
- `2 <= n <= 20`
- `board[i][j]` is either `-1` or in the range `[1, n^2]`.
- The squares labeled `1` and `n^2` are not the starting points of any snake or ladder.

## Examples
### Example 1
- **Input:** `board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]`
- **Output:** `4`
- **Explanation:** In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

### Example 2
- **Input:** `board = [[-1,-1],[-1,3]]`
- **Output:** `1`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Snakes and Ladders**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

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
var snakesAndLadders = function(board) {
    const n = board.length;
    const target = n * n;

    // Convert square label to board coordinates
    function getCoordinates(square) {
        const rowFromBottom = Math.floor((square - 1) / n);
        const row = n - 1 - rowFromBottom;

        let col = (square - 1) % n;

        // Rows alternate direction (Boustrophedon)
        if (rowFromBottom % 2 === 1) {
            col = n - 1 - col;
        }

        return [row, col];
    }

    const queue = [[1, 0]]; // [square, dice rolls]
    const visited = new Set([1]);
    let front = 0;

    while (front < queue.length) {
        const [square, rolls] = queue[front++];

        if (square === target) {
            return rolls;
        }

        // Try every possible dice roll
        for (
            let next = square + 1;
            next <= Math.min(square + 6, target);
            next++
        ) {
            const [row, col] = getCoordinates(next);

            // Take at most one snake or ladder
            const destination =
                board[row][col] === -1
                    ? next
                    : board[row][col];

            if (!visited.has(destination)) {
                visited.add(destination);
                queue.push([destination, rolls + 1]);
            }
        }
    }

    return -1;
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
- [48. Rotate Image](../../0001-0500/0048-rotate-image/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)
- [118. Pascal's Triangle](../../0001-0500/0118-pascals-triangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/snakes-and-ladders/)
