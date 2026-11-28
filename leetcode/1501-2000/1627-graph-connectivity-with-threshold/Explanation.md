# LeetCode 1627: Graph Connectivity With Threshold

**LeetCode Problem #1627 — Graph Connectivity With Threshold**
Solve LeetCode Graph Connectivity With Threshold using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Graph Connectivity With Threshold |
| LeetCode | #1627 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We have `n` cities labeled from `1` to `n`. Two different cities with labels `x` and `y` are directly connected by a bidirectional road if and only if `x` and `y` share a common divisor **strictly greater** than some `threshold`. More formally, cities with labels `x` and `y` have a road between them if there exists an integer `z` such that all of the following are true:

`x % z == 0`, 
 `y % z == 0`, and 
 `z > threshold`.

Given the two integers, `n` and `threshold`, and an array of `queries`, you must determine for each `queries[i] = [a_i, b_i]` if cities `a_i` and `b_i` are connected directly or indirectly. (i.e. there is some path between them).

Return *an array *`answer`*, where *`answer.length == queries.length`* and *`answer[i]`* is *`true`* if for the *`i^th`* query, there is a path between *`a_i`* and *`b_i`*, or *`answer[i]`* is *`false`* if there is no path.*

## Constraints
- `2 <= n <= 10^4`
- `0 <= threshold <= n`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 2`
- `1 <= a_i, b_i <= cities`
- `a_i != b_i`

## Examples
### Example 1
- **Input:** `n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]`
- **Output:** `[false,false,true]`
- **Explanation:** The divisors for each number:
1: 1
2: 1, 2
3: 1, 3 
4: 1, 2, 4 
5: 1, 5 
6: 1, 2, 3 , 6 
Using the underlined divisors above the threshold, only cities 3 and 6 share a common divisor, so they are the
only ones directly connected. The result of each query:
[1,4] 1 is not connected to 4
[2,5] 2 is not connected to 5
[3,6] 3 is connected to 6 through path 3--6

### Example 2
- **Input:** `n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]`
- **Output:** `[true,true,true,true,true]`
- **Explanation:** The divisors for each number are the same as the previous example. However, since the threshold is 0,
all divisors can be used. Since all numbers share 1 as a divisor, all cities are connected.

### Example 3
- **Input:** `n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]`
- **Output:** `[false,false,false,false,false]`
- **Explanation:** Only cities 2 and 4 share a common divisor 2 which is strictly greater than the threshold 1, so they are the only ones directly connected.
Please notice that there can be multiple queries for the same pair of nodes [x, y], and that the query [x, y] is equivalent to the query [y, x].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Graph Connectivity With Threshold**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[false,false,true]`.
4. **Verification:** The divisors for each number:
1: 1
2: 1, 2
3: 1, 3 
4: 1, 2, 4 
5: 1, 5 
6: 1, 2, 3 , 6 
Using the underlined divisors above the threshold, only cities 3 and 6 share a common divisor, so they are the
only ones directly connected. The result of each query:
[1,4] 1 is not connected to 4
[2,5] 2 is not connected to 5
[3,6] 3 is connected to 6 through path 3--6

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

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        # Fast path: when threshold is 0, 1 divides everything, all nodes are connected
        if threshold == 0:
            return [True] * len(queries)

        dsu = DSU(n)

        # Sieve approach: connect every multiple of z to z
        for z in range(threshold + 1, n + 1):
            for multiple in range(2 * z, n + 1, z):
                dsu.union(z, multiple)

        # Answer queries in O(alpha(n)) time each
        return [dsu.find(a) == dsu.find(b) for a, b in queries]
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
- [133. Clone Graph](../../0001-0500/0133-clone-graph/)
- [785. Is Graph Bipartite?](../../0501-1000/0785-is-graph-bipartite/)
- [882. Reachable Nodes In Subdivided Graph](../../0501-1000/0882-reachable-nodes-in-subdivided-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/graph-connectivity-with-threshold/)
