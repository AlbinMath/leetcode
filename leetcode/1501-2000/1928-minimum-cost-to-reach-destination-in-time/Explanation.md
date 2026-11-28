# LeetCode 1928: Minimum Cost to Reach Destination in Time

**LeetCode Problem #1928 — Minimum Cost to Reach Destination in Time**
Solve LeetCode Minimum Cost to Reach Destination in Time using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Reach Destination in Time |
| LeetCode | #1928 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a country of `n` cities numbered from `0` to `n - 1` where **all the cities are connected** by bi-directional roads. The roads are represented as a 2D integer array `edges` where `edges[i] = [x_i, y_i, time_i]` denotes a road between cities `x_i` and `y_i` that takes `time_i` minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

Each time you pass through a city, you must pay a passing fee. This is represented as a **0-indexed** integer array `passingFees` of length `n` where `passingFees[j]` is the amount of dollars you must pay when you pass through city `j`.

In the beginning, you are at city `0` and want to reach city `n - 1` in `maxTime`** minutes or less**. The **cost** of your journey is the **summation of passing fees** for each city that you passed through at some moment of your journey (**including** the source and destination cities).

Given `maxTime`, `edges`, and `passingFees`, return *the **minimum cost** to complete your journey, or *`-1`* if you cannot complete it within *`maxTime`* minutes*.

## Constraints
- `1 <= maxTime <= 1000`
- `n == passingFees.length`
- `2 <= n <= 1000`
- `n - 1 <= edges.length <= 1000`
- `0 <= x_i, y_i <= n - 1`
- `1 <= time_i <= 1000`
- `1 <= passingFees[j] <= 1000`
- The graph may contain multiple edges between two nodes.
- The graph does not contain self loops.

## Examples
### Example 1
- **Input:** `maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]`
- **Output:** `11`
- **Explanation:** The path to take is 0 -> 1 -> 2 -> 5, which takes 30 minutes and has $11 worth of passing fees.

### Example 2
- **Input:** `maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]`
- **Output:** `48`
- **Explanation:** The path to take is 0 -> 3 -> 4 -> 5, which takes 26 minutes and has $48 worth of passing fees.
You cannot take path 0 -> 1 -> 2 -> 5 since it would take too long.

### Example 3
- **Input:** `maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]`
- **Output:** `-1`
- **Explanation:** There is no way to reach city 5 from city 0 within 25 minutes.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Cost to Reach Destination in Time**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** The path to take is 0 -> 1 -> 2 -> 5, which takes 30 minutes and has $11 worth of passing fees.

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
import heapq
from collections import defaultdict

class Solution:
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        g = defaultdict(list)
        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))

        d = [[float('inf')] * n for _ in range(maxTime + 1)]
        d[0][0] = passingFees[0]
        q = [(passingFees[0], 0, 0)]

        while q:
            cost, t, u = heapq.heappop(q)
            if u == n - 1:
                return cost
            if cost > d[t][u]:
                continue
            for v, w in g[u]:
                nt = t + w
                nc = cost + passingFees[v]
                if nt <= maxTime and nc < d[nt][v]:
                    d[nt][v] = nc
                    heapq.heappush(q, (nc, nt, v))

        return -1
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
- [2045. Second Minimum Time to Reach Destination](../../2001-2500/2045-second-minimum-time-to-reach-destination/)
- [3604. Minimum Time to Reach Destination in Directed Graph](../../3501-4000/3604-minimum-time-to-reach-destination-in-directed-graph/)
- [3341. Find Minimum Time to Reach Last Room I](../../3001-3500/3341-find-minimum-time-to-reach-last-room-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/)
