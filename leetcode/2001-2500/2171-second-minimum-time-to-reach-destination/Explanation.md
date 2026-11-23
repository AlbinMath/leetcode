# LeetCode 2045: Second Minimum Time to Reach Destination

**LeetCode Problem #2045 — Second Minimum Time to Reach Destination**
Solve LeetCode Second Minimum Time to Reach Destination using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Second Minimum Time to Reach Destination |
| LeetCode | #2045 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A city is represented as a **bi-directional connected** graph with `n` vertices where each vertex is labeled from `1` to `n` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [u_i, v_i]` denotes a bi-directional edge between vertex `u_i` and vertex `v_i`. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself. The time taken to traverse any edge is `time` minutes.

Each vertex has a traffic signal which changes its color from **green** to **red** and vice versa every `change` minutes. All signals change **at the same time**. You can enter a vertex at **any time**, but can leave a vertex **only when the signal is green**. You **cannot wait **at a vertex if the signal is **green**.

The **second minimum value** is defined as the smallest value** strictly larger **than the minimum value.

For example the second minimum value of `[2, 3, 4]` is `3`, and the second minimum value of `[2, 2, 4]` is `4`.

Given `n`, `edges`, `time`, and `change`, return *the **second minimum time** it will take to go from vertex *`1`* to vertex *`n`.

**Notes:**

You can go through any vertex **any** number of times, **including** `1` and `n`. 
 You can assume that when the journey **starts**, all signals have just turned **green**.

## Constraints
- `2 <= n <= 10^4`
- `n - 1 <= edges.length <= min(2 * 10^4, n * (n - 1) / 2)`
- `edges[i].length == 2`
- `1 <= u_i, v_i <= n`
- `u_i != v_i`
- There are no duplicate edges.
- Each vertex can be reached directly or indirectly from every other vertex.
- `1 <= time, change <= 10^3`

## Examples
### Example 1
- **Input:** `n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5`
- **Output:** `13`
- **Explanation:** The figure on the left shows the given graph.
The blue path in the figure on the right is the minimum time path.
The time taken is:
- Start at 1, time elapsed=0
- 1 -> 4: 3 minutes, time elapsed=3
- 4 -> 5: 3 minutes, time elapsed=6
Hence the minimum time needed is 6 minutes.

The red path shows the path to get the second minimum time.
- Start at 1, time elapsed=0
- 1 -> 3: 3 minutes, time elapsed=3
- 3 -> 4: 3 minutes, time elapsed=6
- Wait at 4 for 4 minutes, time elapsed=10
- 4 -> 5: 3 minutes, time elapsed=13
Hence the second minimum time is 13 minutes.

### Example 2
- **Input:** `n = 2, edges = [[1,2]], time = 3, change = 2`
- **Output:** `11`
- **Explanation:** The minimum time path is 1 -> 2 with time = 3 minutes.
The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Second Minimum Time to Reach Destination**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The figure on the left shows the given graph.
The blue path in the figure on the right is the minimum time path.
The time taken is:
- Start at 1, time elapsed=0
- 1 -> 4: 3 minutes, time elapsed=3
- 4 -> 5: 3 minutes, time elapsed=6
Hence the minimum time needed is 6 minutes.

The red path shows the path to get the second minimum time.
- Start at 1, time elapsed=0
- 1 -> 3: 3 minutes, time elapsed=3
- 3 -> 4: 3 minutes, time elapsed=6
- Wait at 4 for 4 minutes, time elapsed=10
- 4 -> 5: 3 minutes, time elapsed=13
Hence the second minimum time is 13 minutes.

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
from collections import deque

class Solution:
    def secondMinimum(self, n, edges, time, change):
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        d = [[float('inf')] * 2 for _ in range(n + 1)]
        d[1][0] = 0
        q = deque([(1, 0)])

        while q:
            u, t = q.popleft()
            if u == n and t == d[n][1]:
                return t

            nt = t
            if (nt // change) % 2:
                nt = (nt // change + 1) * change
            nt += time

            for v in g[u]:
                if nt < d[v][0]:
                    d[v][0] = nt
                    q.append((v, nt))
                elif d[v][0] < nt < d[v][1]:
                    d[v][1] = nt
                    q.append((v, nt))

        return -1
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
- [1928. Minimum Cost to Reach Destination in Time](../../2001-2500/2040-minimum-cost-to-reach-destination-in-time/)
- [3604. Minimum Time to Reach Destination in Directed Graph](../../3501-4000/3916-minimum-time-to-reach-destination-in-directed-graph/)
- [3341. Find Minimum Time to Reach Last Room I](../../3501-4000/3627-find-minimum-time-to-reach-last-room-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/second-minimum-time-to-reach-destination/)
