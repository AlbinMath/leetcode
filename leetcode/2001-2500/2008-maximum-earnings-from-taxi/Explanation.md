# LeetCode 2008: Maximum Earnings From Taxi

**LeetCode Problem #2008 — Maximum Earnings From Taxi**
Solve LeetCode Maximum Earnings From Taxi using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Earnings From Taxi |
| LeetCode | #2008 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` points on a road you are driving your taxi on. The `n` points on the road are labeled from `1` to `n` in the direction you are going, and you want to drive from point `1` to point `n` to make money by picking up passengers. You cannot change the direction of the taxi.

The passengers are represented by a **0-indexed** 2D integer array `rides`, where `rides[i] = [start_i, end_i, tip_i]` denotes the `i^th` passenger requesting a ride from point `start_i` to point `end_i` who is willing to give a `tip_i` dollar tip.

For** each **passenger `i` you pick up, you **earn** `end_i - start_i + tip_i` dollars. You may only drive at most one passenger at a time.

Given `n` and `rides`, return *the **maximum** number of dollars you can earn by picking up the passengers optimally.*

**Note:** You may drop off a passenger and pick up a different passenger at the same point.

## Constraints
- `1 <= n <= 10^5`
- `1 <= rides.length <= 3 * 10^4`
- `rides[i].length == 3`
- `1 <= start_i < end_i <= n`
- `1 <= tip_i <= 10^5`

## Examples
### Example 1
- **Input:** `n = 5, rides = [ [2,5,4] ,[1,5,1]]`
- **Output:** `7`
- **Explanation:** We can pick up passenger 0 to earn 5 - 2 + 4 = 7 dollars.

### Example 2
- **Input:** `n = 20, rides = [[1,6,1], [3,10,2] , [10,12,3] ,[11,12,2],[12,15,2], [13,18,1] ]`
- **Output:** `20`
- **Explanation:** We will pick up the following passengers:
- Drive passenger 1 from point 3 to point 10 for a profit of 10 - 3 + 2 = 9 dollars.
- Drive passenger 2 from point 10 to point 12 for a profit of 12 - 10 + 3 = 5 dollars.
- Drive passenger 5 from point 13 to point 18 for a profit of 18 - 13 + 1 = 6 dollars.
We earn 9 + 5 + 6 = 20 dollars in total.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Earnings From Taxi**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, rides = [ [2,5,4] ,[1,5,1]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** We can pick up passenger 0 to earn 5 - 2 + 4 = 7 dollars.

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
from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        by_end = [[] for _ in range(n + 1)]
        for s, e, t in rides:
            by_end[e].append((s, e - s + t))

        dp = [0] * (n + 1)
        for p in range(1, n + 1):
            dp[p] = dp[p - 1]
            for s, earn in by_end[p]:
                dp[p] = max(dp[p], dp[s] + earn)

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
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)
- [1423. Maximum Points You Can Obtain from Cards](../../1001-1500/1423-maximum-points-you-can-obtain-from-cards/)
- [1707. Maximum XOR With an Element From Array](../../1501-2000/1707-maximum-xor-with-an-element-from-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-earnings-from-taxi/)
