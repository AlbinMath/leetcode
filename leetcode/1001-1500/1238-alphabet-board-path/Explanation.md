# LeetCode 1138: Alphabet Board Path

**LeetCode Problem #1138 — Alphabet Board Path**
Solve LeetCode Alphabet Board Path using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Alphabet Board Path |
| LeetCode | #1138 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
On an alphabet board, we start at position `(0, 0)`, corresponding to character `board[0][0]`.

Here, `board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]`, as shown in the diagram below.

We may make the following moves:

`'U'` moves our position up one row, if the position exists on the board; 
 `'D'` moves our position down one row, if the position exists on the board; 
 `'L'` moves our position left one column, if the position exists on the board; 
 `'R'` moves our position right one column, if the position exists on the board; 
 `'!'` adds the character `board[r][c]` at our current position `(r, c)` to the answer.

(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to `target` in the minimum number of moves. You may return any path that does so.

## Constraints
- `1 <= target.length <= 100`
- `target` consists only of English lowercase letters.

## Examples
### Example 1
- **Input:** `target = "leet"`
- **Output:** `"DDR!UURRR!!DDD!"`

### Example 2
- **Input:** `target = "code"`
- **Output:** `"RR!DDRR!UUL!R!"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Alphabet Board Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = "leet"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"DDR!UURRR!!DDD!"`.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = []
        r = c = 0

        for ch in target:
            idx = ord(ch) - ord('a')
            nr, nc = divmod(idx, 5)

            if nr < r:
                res.append('U' * (r - nr))
            if nc < c:
                res.append('L' * (c - nc))
            if nr > r:
                res.append('D' * (nr - r))
            if nc > c:
                res.append('R' * (nc - c))

            res.append('!')
            r, c = nr, nc

        return ''.join(res)
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [71. Simplify Path](../../0001-0500/0071-simplify-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/alphabet-board-path/)
