# LeetCode 773: Sliding Puzzle

**LeetCode Problem #773 — Sliding Puzzle**
Solve LeetCode Sliding Puzzle using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sliding Puzzle |
| LeetCode | #773 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
On an `2 x 3` board, there are five tiles labeled from `1` to `5`, and an empty square represented by `0`. A **move** consists of choosing `0` and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is `[[1,2,3],[4,5,0]]`.

Given the puzzle board `board`, return *the least number of moves required so that the state of the board is solved*. If it is impossible for the state of the board to be solved, return `-1`.

## Constraints
- `board.length == 2`
- `board[i].length == 3`
- `0 <= board[i][j] <= 5`
- Each value `board[i][j]` is **unique**.

## Examples
### Example 1
- **Input:** `board = [[1,2,3],[4,0,5]]`
- **Output:** `1`
- **Explanation:** Swap the 0 and the 5 in one move.

### Example 2
- **Input:** `board = [[1,2,3],[5,4,0]]`
- **Output:** `-1`
- **Explanation:** No number of moves will make the board solved.

### Example 3
- **Input:** `board = [[4,1,2],[5,0,3]]`
- **Output:** `5`
- **Explanation:** 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Sliding Puzzle**, we observe the problem requirements and utilize the **Sliding Window** technique. We maintain a contiguous window defined by `left` and `right` pointers. The right pointer expands the window by adding incoming elements, while the left pointer advances to restore window invariants whenever duplicates or constraint limits are exceeded.

## Algorithm
1. Initialize `left = 0` and window tracking data structures.
2. Expand `right` pointer over input elements.
3. Contract `left` pointer when window invariants are breached.
4. Update global best metric for valid window intervals.
5. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [[1,2,3],[4,0,5]]`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Swap the 0 and the 5 in one move.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start = ''.join(map(str, sum(board, [])))
        target = "123450"
        moves = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        q = deque([(start, 0)])
        seen = {start}

        while q:
            s, steps = q.popleft()
            if s == target:
                return steps
            i = s.index('0')
            for j in moves[i]:
                t = list(s)
                t[i], t[j] = t[j], t[i]
                nxt = ''.join(t)
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, steps + 1))
        return -1
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [1178. Number of Valid Words for Each Puzzle](../../1001-1500/1282-number-of-valid-words-for-each-puzzle/)
- [1307. Verbal Arithmetic Puzzle](../../1001-1500/1429-verbal-arithmetic-puzzle/)
- [239. Sliding Window Maximum](../../0001-0500/0239-sliding-window-maximum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sliding-puzzle/)
