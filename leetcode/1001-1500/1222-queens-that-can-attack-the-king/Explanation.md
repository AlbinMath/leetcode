# LeetCode 1222: Queens That Can Attack the King

**LeetCode Problem #1222 — Queens That Can Attack the King**
Solve LeetCode Queens That Can Attack the King using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Queens That Can Attack the King |
| LeetCode | #1222 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
On a **0-indexed** `8 x 8` chessboard, there can be multiple black queens and one white king.

You are given a 2D integer array `queens` where `queens[i] = [xQueen_i, yQueen_i]` represents the position of the `i^th` black queen on the chessboard. You are also given an integer array `king` of length `2` where `king = [xKing, yKing]` represents the position of the white king.

Return *the coordinates of the black queens that can directly attack the king*. You may return the answer in **any order**.

## Constraints
- `1 <= queens.length < 64`
- `queens[i].length == king.length == 2`
- `0 <= xQueen_i, yQueen_i, xKing, yKing < 8`
- All the given positions are **unique**.

## Examples
### Example 1
- **Input:** `queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]`
- **Output:** `[[0,1],[1,0],[3,3]]`
- **Explanation:** The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).

### Example 2
- **Input:** `queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]`
- **Output:** `[[2,2],[3,4],[4,4]]`
- **Explanation:** The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Queens That Can Attack the King**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,1],[1,0],[3,3]]`.
4. **Verification:** The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).

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
var queensAttacktheKing = function(queens, king) {
    // 8x8 board lookup for O(1) queen checks
    const hasQueen = Array.from({ length: 8 }, () => new Uint8Array(8));
    for (const [r, c] of queens) {
        hasQueen[r][c] = 1;
    }

    const attackers = [];
    // Cast rays in all 8 directions starting from the king
    for (let dr = -1; dr <= 1; dr++) {
        for (let dc = -1; dc <= 1; dc++) {
            if (dr === 0 && dc === 0) continue;

            let r = king[0] + dr;
            let c = king[1] + dc;
            while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                if (hasQueen[r][c]) {
                    attackers.push([r, c]);
                    break; // First queen in this direction blocks any behind it
                }
                r += dr;
                c += dc;
            }
        }
    }

    return attackers;
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
- [1160. Find Words That Can Be Formed by Characters](../../1001-1500/1160-find-words-that-can-be-formed-by-characters/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [1725. Number Of Rectangles That Can Form The Largest Square](../../1501-2000/1725-number-of-rectangles-that-can-form-the-largest-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/queens-that-can-attack-the-king/)
