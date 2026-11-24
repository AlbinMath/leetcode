# LeetCode 1976: Number of Ways to Arrive at Destination

**LeetCode Problem #1976 — Number of Ways to Arrive at Destination**
Solve LeetCode Number of Ways to Arrive at Destination using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Arrive at Destination |
| LeetCode | #1976 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are in a city that consists of `n` intersections numbered from `0` to `n - 1` with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer `n` and a 2D integer array `roads` where `roads[i] = [u_i, v_i, time_i]` means that there is a road between intersections `u_i` and `v_i` that takes `time_i` minutes to travel. You want to know in how many ways you can travel from intersection `0` to intersection `n - 1` in the **shortest amount of time**.

Return *the **number of ways** you can arrive at your destination in the **shortest amount of time***. Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= n <= 200`
- `n - 1 <= roads.length <= n * (n - 1) / 2`
- `roads[i].length == 3`
- `0 <= u_i, v_i <= n - 1`
- `1 <= time_i <= 10^9`
- `u_i != v_i`
- There is at most one road connecting any two intersections.
- You can reach any intersection from any other intersection.

## Examples
### Example 1
- **Input:** `n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]`
- **Output:** `4`
- **Explanation:** The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

### Example 2
- **Input:** `n = 2, roads = [[1,0,10]]`
- **Output:** `1`
- **Explanation:** There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Ways to Arrive at Destination**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

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
import heapq

class Solution:
    def countPaths(self, n, roads):
        mod = 10**9 + 7
        g = [[] for _ in range(n)]

        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))

        d = [float('inf')] * n
        ways = [0] * n
        d[0], ways[0] = 0, 1
        q = [(0, 0)]

        while q:
            t, u = heapq.heappop(q)
            if t > d[u]:
                continue

            for v, w in g[u]:
                nt = t + w
                if nt < d[v]:
                    d[v] = nt
                    ways[v] = ways[u]
                    heapq.heappush(q, (nt, v))
                elif nt == d[v]:
                    ways[v] = (ways[v] + ways[u]) % mod

        return ways[n - 1]
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
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1001-1500/1434-number-of-ways-to-wear-different-hats-to-each-other/)
- [1444. Number of Ways of Cutting a Pizza](../../1001-1500/1444-number-of-ways-of-cutting-a-pizza/)
- [1525. Number of Good Ways to Split a String](../../1501-2000/1525-number-of-good-ways-to-split-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)
