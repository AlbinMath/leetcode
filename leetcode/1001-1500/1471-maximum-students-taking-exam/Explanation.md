# LeetCode 1349: Maximum Students Taking Exam

**LeetCode Problem #1349 — Maximum Students Taking Exam**
Solve LeetCode Maximum Students Taking Exam using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Students Taking Exam |
| LeetCode | #1349 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a `m * n` matrix `seats` that represent seats distributions in a classroom. If a seat is broken, it is denoted by `'#'` character otherwise it is denoted by a `'.'` character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the **maximum **number of students that can take the exam together without any cheating being possible.

Students must be placed in seats in good condition.

## Constraints
- `seats` contains only characters `'.' and ``'#'.`
- `m == seats.length`
- `n == seats[i].length`
- `1 <= m <= 8`
- `1 <= n <= 8`

## Examples
### Example 1
- **Input:** `seats = [["#",".","#","#",".","#"],
 [".","#","#","#","#","."],
 ["#",".","#","#",".","#"]]`
- **Output:** `4`
- **Explanation:** Teacher can place 4 students in available seats so they don't cheat on the exam.

### Example 2
- **Input:** `seats = [[".","#"],
 ["#","#"],
 ["#","."],
 ["#","#"],
 [".","#"]]`
- **Output:** `3`
- **Explanation:** Place all students in available seats.

### Example 3
- **Input:** `seats = [["#",".","`
- **Output:** `10`
- **Explanation:** Place students in available seats in column 1, 3 and 5.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Students Taking Exam**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `seats = [["#",".","#","#",".","#"],
 [".","#","#","#","#","."],
 ["#",".","#","#",".","#"]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Teacher can place 4 students in available seats so they don't cheat on the exam.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {character[][]} seats
 * @return {number}
 */
var maxStudents = function (seats) {
  const m = seats.length;
  const n = seats[0].length;
  const size = 1 << n;

  const popcount = (x) => {
    let c = 0;
    for (; x; x &= x - 1) c++;
    return c;
  };

  // broken[r] has a bit set for each broken seat in row r
  const broken = seats.map((row) => {
    let b = 0;
    for (let c = 0; c < n; c++) if (row[c] === "#") b |= 1 << c;
    return b;
  });

  let dp = new Array(size).fill(-1);
  dp[0] = 0; // virtual empty row above row 0

  for (let r = 0; r < m; r++) {
    const next = new Array(size).fill(-1);
    for (let cur = 0; cur < size; cur++) {
      if (cur & broken[r]) continue;
      if (cur & (cur >> 1)) continue;
      const cnt = popcount(cur);
      for (let prev = 0; prev < size; prev++) {
        if (dp[prev] < 0) continue;
        if (cur & (prev << 1) || cur & (prev >> 1)) continue;
        next[cur] = Math.max(next[cur], dp[prev] + cnt);
      }
    }
    dp = next;
  }

  return Math.max(...dp);
};
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [855. Exam Room](../../0501-1000/0885-exam-room/)
- [2024. Maximize the Confusion of an Exam](../../2001-2500/2134-maximize-the-confusion-of-an-exam/)
- [3709. Design Exam Scores Tracker](../../4001-4500/4059-design-exam-scores-tracker/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-students-taking-exam/)
