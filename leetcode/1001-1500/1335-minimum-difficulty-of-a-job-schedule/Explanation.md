# LeetCode 1335: Minimum Difficulty of a Job Schedule

**LeetCode Problem #1335 — Minimum Difficulty of a Job Schedule**
Solve LeetCode Minimum Difficulty of a Job Schedule using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Difficulty of a Job Schedule |
| LeetCode | #1335 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
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
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Difficulty of a Job Schedule**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `jobDifficulty = [6,5,4,3,2,1], d = 2`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7

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
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [1235. Maximum Profit in Job Scheduling](../../1001-1500/1235-maximum-profit-in-job-scheduling/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [76. Minimum Window Substring](../../0001-0500/0076-minimum-window-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)
