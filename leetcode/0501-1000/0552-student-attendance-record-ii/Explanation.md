# LeetCode 552: Student Attendance Record II

**LeetCode Problem #552 — Student Attendance Record II**
Solve LeetCode Student Attendance Record II using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Student Attendance Record II |
| LeetCode | #552 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

`'A'`: Absent. 
 `'L'`: Late. 
 `'P'`: Present.

Any student is eligible for an attendance award if they meet **both** of the following criteria:

The student was absent (`'A'`) for **strictly** fewer than 2 days **total**. 
 The student was **never** late (`'L'`) for 3 or more **consecutive** days.

Given an integer `n`, return *the **number** of possible attendance records of length* `n`* that make a student eligible for an attendance award. The answer may be very large, so return it **modulo** *`10^9 + 7`.

## Constraints
- `1 <= n <= 10^5`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `8`
- **Explanation:** There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

### Example 2
- **Input:** `n = 1`
- **Output:** `3`

### Example 3
- **Input:** `n = 10101`
- **Output:** `183236316`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Student Attendance Record II**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            nd = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    v = dp[a][l]
                    if not v:
                        continue
                    nd[a][0] = (nd[a][0] + v) % MOD          # P
                    if l < 2:
                        nd[a][l + 1] = (nd[a][l + 1] + v) % MOD  # L
                    if a == 0:
                        nd[1][0] = (nd[1][0] + v) % MOD      # A
            dp = nd
        return sum(sum(row) for row in dp) % MOD
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
- [551. Student Attendance Record I](../../0501-1000/0551-student-attendance-record-i/)
- [1894. Find the Student that Will Replace the Chalk](../../1501-2000/1894-find-the-student-that-will-replace-the-chalk/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/student-attendance-record-ii/)
