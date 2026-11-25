# LeetCode 2120: Execution of All Suffix Instructions Staying in a Grid

**LeetCode Problem #2120 — Execution of All Suffix Instructions Staying in a Grid**
Solve LeetCode Execution of All Suffix Instructions Staying in a Grid using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Execution of All Suffix Instructions Staying in a Grid |
| LeetCode | #2120 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an `n x n` grid, with the top-left cell at `(0, 0)` and the bottom-right cell at `(n - 1, n - 1)`. You are given the integer `n` and an integer array `startPos` where `startPos = [start_row, start_col]` indicates that a robot is initially at cell `(start_row, start_col)`.

You are also given a **0-indexed** string `s` of length `m` where `s[i]` is the `i^th` instruction for the robot: `'L'` (move left), `'R'` (move right), `'U'` (move up), and `'D'` (move down).

The robot can begin executing from any `i^th` instruction in `s`. It executes the instructions one by one towards the end of `s` but it stops if either of these conditions is met:

The next instruction will move the robot off the grid. 
 There are no more instructions left to execute.

Return *an array* `answer` *of length* `m` *where* `answer[i]` *is **the number of instructions** the robot can execute if the robot **begins executing from** the* `i^th` *instruction in* `s`.

## Constraints
- `m == s.length`
- `1 <= n, m <= 500`
- `startPos.length == 2`
- `0 <= start_row, start_col < n`
- `s` consists of `'L'`, `'R'`, `'U'`, and `'D'`.

## Examples
### Example 1
- **Input:** `n = 3, startPos = [0,1], s = "RRDDLU"`
- **Output:** `[1,5,4,3,1,0]`
- **Explanation:** Starting from startPos and beginning execution from the i^th instruction:
- 0^th: "

### Example 2
- **Input:** `n = 2, startPos = [1,1], s = "LURD"`
- **Output:** `[4,1,0,0]`
- **Explanation:** - 0^th: "

### Example 3
- **Input:** `n = 1, startPos = [0,0], s = "LRUD"`
- **Output:** `[0,0,0,0]`
- **Explanation:** No matter which instruction the robot begins execution from, it would move off the grid.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Execution of All Suffix Instructions Staying in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, startPos = [0,1], s = "RRDDLU"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,5,4,3,1,0]`.
4. **Verification:** Starting from startPos and beginning execution from the i^th instruction:
- 0^th: "

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
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        delta = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        m = len(s)
        ans = []

        for i in range(m):
            r, c = startPos
            count = 0
            for j in range(i, m):
                dr, dc = delta[s[j]]
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    break
                r, c = nr, nc
                count += 1
            ans.append(count)

        return ans
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
- [30. Substring with Concatenation of All Words](../../0001-0500/0030-substring-with-concatenation-of-all-words/)
- [432. All O`one Data Structure](../../0001-0500/0432-all-oone-data-structure/)
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/)
