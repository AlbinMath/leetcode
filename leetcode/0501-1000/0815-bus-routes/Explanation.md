# LeetCode 815: Bus Routes

**LeetCode Problem #815 — Bus Routes**
Solve LeetCode Bus Routes using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Bus Routes |
| LeetCode | #815 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `routes` representing bus routes where `routes[i]` is a bus route that the `i^th` bus repeats forever.

For example, if `routes[0] = [1, 5, 7]`, this means that the `0^th` bus travels in the sequence `1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ...` forever.

You will start at the bus stop `source` (You are not on any bus initially), and you want to go to the bus stop `target`. You can travel between bus stops by buses only.

Return *the least number of buses you must take to travel from *`source`* to *`target`. Return `-1` if it is not possible.

## Constraints
- `1 <= routes.length <= 500`.
- `1 <= routes[i].length <= 10^5`
- All the values of `routes[i]` are **unique**.
- `sum(routes[i].length) <= 10^5`
- `0 <= routes[i][j] < 10^6`
- `0 <= source, target < 10^6`

## Examples
### Example 1
- **Input:** `routes = [[1,2,7],[3,6,7]], source = 1, target = 6`
- **Output:** `2`
- **Explanation:** The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

### Example 2
- **Input:** `routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12`
- **Output:** `-1`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Bus Routes**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `routes = [[1,2,7],[3,6,7]], source = 1, target = 6`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

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
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        g = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                g[stop].append(i)

        q, seen = deque([(source, 0)]), {source}
        buses = set()

        while q:
            stop, cnt = q.popleft()
            for bus in g[stop]:
                if bus in buses:
                    continue
                buses.add(bus)
                for nxt in routes[bus]:
                    if nxt == target:
                        return cnt + 1
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, cnt + 1))
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
- [1204. Last Person to Fit in the Bus](../../1001-1500/1204-last-person-to-fit-in-the-bus/)
- [1466. Reorder Routes to Make All Paths Lead to the City Zero](../../1001-1500/1466-reorder-routes-to-make-all-paths-lead-to-the-city-zero/)
- [1575. Count All Possible Routes](../../1501-2000/1575-count-all-possible-routes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/bus-routes/)
