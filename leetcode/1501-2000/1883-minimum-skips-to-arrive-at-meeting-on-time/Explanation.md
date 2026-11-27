# LeetCode 1883: Minimum Skips to Arrive at Meeting On Time

**LeetCode Problem #1883 — Minimum Skips to Arrive at Meeting On Time**
Solve LeetCode Minimum Skips to Arrive at Meeting On Time using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Skips to Arrive at Meeting On Time |
| LeetCode | #1883 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `hoursBefore`, the number of hours you have to travel to your meeting. To arrive at your meeting, you have to travel through `n` roads. The road lengths are given as an integer array `dist` of length `n`, where `dist[i]` describes the length of the `i^th` road in **kilometers**. In addition, you are given an integer `speed`, which is the speed (in **km/h**) you will travel at.

After you travel road `i`, you must rest and wait for the **next integer hour** before you can begin traveling on the next road. Note that you do not have to rest after traveling the last road because you are already at the meeting.

For example, if traveling a road takes `1.4` hours, you must wait until the `2` hour mark before traveling the next road. If traveling a road takes exactly `2` hours, you do not need to wait.

However, you are allowed to **skip** some rests to be able to arrive on time, meaning you do not need to wait for the next integer hour. Note that this means you may finish traveling future roads at different hour marks.

For example, suppose traveling the first road takes `1.4` hours and traveling the second road takes `0.6` hours. Skipping the rest after the first road will mean you finish traveling the second road right at the `2` hour mark, letting you start traveling the third road immediately.

Return *the **minimum number of skips required** to arrive at the meeting on time, or* `-1`* if it is** impossible***.

## Constraints
- `n == dist.length`
- `1 <= n <= 1000`
- `1 <= dist[i] <= 10^5`
- `1 <= speed <= 10^6`
- `1 <= hoursBefore <= 10^7`

## Examples
### Example 1
- **Input:** `dist = [1,3,2], speed = 4, hoursBefore = 2`
- **Output:** `1`
- **Explanation:** Without skipping any rests, you will arrive in (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 hours.
You can skip the first rest to arrive in ((1/4 + 0 ) + (3/4 + 0)) + (2/4) = 1.5 hours.
Note that the second rest is shortened because you finish traveling the second road at an integer hour due to skipping the first rest.

### Example 2
- **Input:** `dist = [7,3,5,5], speed = 2, hoursBefore = 10`
- **Output:** `2`
- **Explanation:** Without skipping any rests, you will arrive in (7/2 + 1/2) + (3/2 + 1/2) + (5/2 + 1/2) + (5/2) = 11.5 hours.
You can skip the first and third rest to arrive in ((7/2 + 0 ) + (3/2 + 0)) + ((5/2 + 0 ) + (5/2)) = 10 hours.

### Example 3
- **Input:** `dist = [7,3,5,5], speed = 1, hoursBefore = 10`
- **Output:** `-1`
- **Explanation:** It is impossible to arrive at the meeting on time even if you skip all the rests.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Skips to Arrive at Meeting On Time**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `dist = [1,3,2], speed = 4, hoursBefore = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Without skipping any rests, you will arrive in (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 hours.
You can skip the first rest to arrive in ((1/4 + 0 ) + (3/4 + 0)) + (2/4) = 1.5 hours.
Note that the second rest is shortened because you finish traveling the second road at an integer hour due to skipping the first rest.

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
    def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        target = hoursBefore * speed
        
        if sum(dist) > target:
            return -1
            
        INF = float('inf')
        dp = [INF] * n
        dp[0] = 0
        
        for i, d in enumerate(dist):
            if i == n - 1:
                for j in range(i + 1):
                    dp[j] += d
            else:
                for j in range(i + 1, -1, -1):
                    no_skip = ((dp[j] + d + speed - 1) // speed) * speed if dp[j] < INF else INF
                    
                    with_skip = dp[j - 1] + d if j > 0 else INF
                    
                    dp[j] = no_skip if no_skip < with_skip else with_skip
                    
        for j in range(n):
            if dp[j] <= target:
                return j
                
        return -1
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
- [1870. Minimum Speed to Arrive on Time](../../1501-2000/1870-minimum-speed-to-arrive-on-time/)
- [539. Minimum Time Difference](../../0501-1000/0539-minimum-time-difference/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/)
