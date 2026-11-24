# LeetCode 782: Transform to Chessboard

**LeetCode Problem #782 — Transform to Chessboard**
Solve LeetCode Transform to Chessboard using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Transform to Chessboard |
| LeetCode | #782 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `n x n` binary grid `board`. In each move, you can swap any two rows with each other, or any two columns with each other.

Return *the minimum number of moves to transform the board into a **chessboard board***. If the task is impossible, return `-1`.

A **chessboard board** is a board where no `0`'s and no `1`'s are 4-directionally adjacent.

## Constraints
- `n == board.length`
- `n == board[i].length`
- `2 <= n <= 30`
- `board[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]`
- **Output:** `2`
- **Explanation:** One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.

### Example 2
- **Input:** `board = [[0,1],[1,0]]`
- **Output:** `0`
- **Explanation:** Also note that the board with 0 in the top left corner, is also a valid chessboard.

### Example 3
- **Input:** `board = [[1,0],[1,0]]`
- **Output:** `-1`
- **Explanation:** No matter what sequence of moves you make, you cannot end with a valid chessboard.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Transform to Chessboard**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def movesToChessboard(self, board):
        n = len(board)

        # Every row must equal the first row or its complement (same for columns)
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1

        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))

        # Counts of 1s must be balanced
        if not (n // 2 <= row_sum <= (n + 1) // 2):
            return -1
        if not (n // 2 <= col_sum <= (n + 1) // 2):
            return -1

        # Mismatches against the pattern 0101...
        row_diff = sum(board[0][i] != i % 2 for i in range(n))
        col_diff = sum(board[i][0] != i % 2 for i in range(n))

        def calc(diff):
            if n % 2:
                # odd n: only the even mismatch count is achievable
                if diff % 2:
                    diff = n - diff
                return diff // 2
            return min(diff, n - diff) // 2

        return calc(row_diff) + calc(col_diff)
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1331. Rank Transform of an Array](../../1001-1500/1256-rank-transform-of-an-array/)
- [1632. Rank Transform of a Matrix](../../1001-1500/1257-rank-transform-of-a-matrix/)
- [2635. Apply Transform Over Each Element in Array](../../2501-3000/2747-apply-transform-over-each-element-in-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/transform-to-chessboard/)
