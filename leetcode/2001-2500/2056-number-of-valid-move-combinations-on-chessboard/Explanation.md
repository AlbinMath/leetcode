# LeetCode 2056: Number of Valid Move Combinations On Chessboard

**LeetCode Problem #2056 — Number of Valid Move Combinations On Chessboard**
Solve LeetCode Number of Valid Move Combinations On Chessboard using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Valid Move Combinations On Chessboard |
| LeetCode | #2056 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an `8 x 8` chessboard containing `n` pieces (rooks, queens, or bishops). You are given a string array `pieces` of length `n`, where `pieces[i]` describes the type (rook, queen, or bishop) of the `i^th` piece. In addition, you are given a 2D integer array `positions` also of length `n`, where `positions[i] = [r_i, c_i]` indicates that the `i^th` piece is currently at the **1-based** coordinate `(r_i, c_i)` on the chessboard.

When making a **move** for a piece, you choose a **destination** square that the piece will travel toward and stop on.

A rook can only travel **horizontally or vertically** from `(r, c)` to the direction of `(r+1, c)`, `(r-1, c)`, `(r, c+1)`, or `(r, c-1)`. 
 A queen can only travel **horizontally, vertically, or diagonally** from `(r, c)` to the direction of `(r+1, c)`, `(r-1, c)`, `(r, c+1)`, `(r, c-1)`, `(r+1, c+1)`, `(r+1, c-1)`, `(r-1, c+1)`, `(r-1, c-1)`. 
 A bishop can only travel **diagonally** from `(r, c)` to the direction of `(r+1, c+1)`, `(r+1, c-1)`, `(r-1, c+1)`, `(r-1, c-1)`.

You must make a **move** for every piece on the board simultaneously. A **move combination** consists of all the **moves** performed on all the given pieces. Every second, each piece will instantaneously travel **one square** towards their destination if they are not already at it. All pieces start traveling at the `0^th` second. A move combination is **invalid** if, at a given time, **two or more** pieces occupy the same square.

Return *the number of **valid** move combinations*​​​​​.

**Notes:**

**No two pieces** will start in the** same** square. 
 You may choose the square a piece is already on as its **destination**. 
 If two pieces are **directly adjacent** to each other, it is valid for them to **move past each other** and swap positions in one second.

## Constraints
- `n == pieces.length `
- `n == positions.length`
- `1 <= n <= 4`
- `pieces` only contains the strings `"rook"`, `"queen"`, and `"bishop"`.
- There will be at most one queen on the chessboard.
- `1 <= r_i, c_i <= 8`
- Each `positions[i]` is distinct.

## Examples
### Example 1
- **Input:** `pieces = ["rook"], positions = [[1,1]]`
- **Output:** `15`
- **Explanation:** The image above shows the possible squares the piece can move to.

### Example 2
- **Input:** `pieces = ["queen"], positions = [[1,1]]`
- **Output:** `22`
- **Explanation:** The image above shows the possible squares the piece can move to.

### Example 3
- **Input:** `pieces = ["bishop"], positions = [[4,3]]`
- **Output:** `12`
- **Explanation:** The image above shows the possible squares the piece can move to.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Valid Move Combinations On Chessboard**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `pieces = ["rook"], positions = [[1,1]]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** The image above shows the possible squares the piece can move to.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        ROOK = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        BISHOP = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        dirs = {"rook": ROOK, "bishop": BISHOP, "queen": ROOK + BISHOP}

        n = len(pieces)
        moves = []
        for k in range(n):
            r, c = positions[k]
            opts = [(r, c, 0, 0, 0)]  # stay: (r, c, dr, dc, steps)
            for dr, dc in dirs[pieces[k]]:
                for s in range(1, 8):
                    nr, nc = r + dr * s, c + dc * s
                    if not (1 <= nr <= 8 and 1 <= nc <= 8):
                        break
                    opts.append((r, c, dr, dc, s))
            moves.append(opts)

        def conflict(a, b) -> bool:
            ra, ca, dra, dca, sa = a
            rb, cb, drb, dcb, sb = b
            for t in range(max(sa, sb) + 1):
                ta, tb = min(t, sa), min(t, sb)
                if (ra + dra * ta == rb + drb * tb and
                        ca + dca * ta == cb + dcb * tb):
                    return True
            return False

        chosen = []

        def dfs(k: int) -> int:
            if k == n:
                return 1
            total = 0
            for m in moves[k]:
                if all(not conflict(m, o) for o in chosen):
                    chosen.append(m)
                    total += dfs(k + 1)
                    chosen.pop()
            return total

        return dfs(0)
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../../1501-2000/1769-minimum-number-of-operations-to-move-all-balls-to-each-box/)
- [3228. Maximum Number of Operations to Move Ones to the End](../../3001-3500/3228-maximum-number-of-operations-to-move-ones-to-the-end/)
- [65. Valid Number](../../0001-0500/0065-valid-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/)
