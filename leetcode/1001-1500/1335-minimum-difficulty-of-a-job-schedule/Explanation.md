# LeetCode 1335: Minimum Difficulty of a Job Schedule

**LeetCode Problem #1335 — Minimum Difficulty of a Job Schedule**
Solve LeetCode Minimum Difficulty of a Job Schedule using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Difficulty of a Job Schedule |
| LeetCode | #1335 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You want to schedule a list of jobs in `d` days. Jobs are dependent (i.e To work on the `i^th` job, you have to finish all the jobs `j` where `0 <= j < i`).

You have to finish **at least** one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the `d` days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array `jobDifficulty` and an integer `d`. The difficulty of the `i^th` job is `jobDifficulty[i]`.

Return *the minimum difficulty of a job schedule*. If you cannot find a schedule for the jobs return `-1`.

## Constraints
- `1 <= jobDifficulty.length <= 300`
- `0 <= jobDifficulty[i] <= 1000`
- `1 <= d <= 10`

## Examples
### Example 1
- **Input:** `jobDifficulty = [6,5,4,3,2,1], d = 2`
- **Output:** `7`
- **Explanation:** First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7

### Example 2
- **Input:** `jobDifficulty = [9,9,9], d = 4`
- **Output:** `-1`
- **Explanation:** If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

### Example 3
- **Input:** `jobDifficulty = [1,1,1], d = 3`
- **Output:** `3`
- **Explanation:** The schedule is one job per day. total difficulty will be 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Difficulty of a Job Schedule**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `jobDifficulty = [6,5,4,3,2,1], d = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
            
        dp = [float('inf')] * (n + 1)
        curr_max = 0
        for i in range(1, n + 1):
            curr_max = max(curr_max, jobDifficulty[i - 1])
            dp[i] = curr_max
            
        for day in range(2, d + 1):
            next_dp = [float('inf')] * (n + 1)
            for i in range(day, n + 1):
                max_diff = 0
                for j in range(i - 1, day - 2, -1):
                    max_diff = max(max_diff, jobDifficulty[j])
                    next_dp[i] = min(next_dp[i], dp[j] + max_diff)
            dp = next_dp
            
        return dp[n]
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [207. Course Schedule](../../0001-0500/0207-course-schedule/)
- [210. Course Schedule II](../../0001-0500/0210-course-schedule-ii/)
- [630. Course Schedule III](../../0501-1000/0630-course-schedule-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)
