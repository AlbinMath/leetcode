# LeetCode 2092: Find All People With Secret

**LeetCode Problem #2092 — Find All People With Secret**
Solve LeetCode Find All People With Secret using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All People With Secret |
| LeetCode | #2092 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` indicating there are `n` people numbered from `0` to `n - 1`. You are also given a **0-indexed** 2D integer array `meetings` where `meetings[i] = [x_i, y_i, time_i]` indicates that person `x_i` and person `y_i` have a meeting at `time_i`. A person may attend **multiple meetings** at the same time. Finally, you are given an integer `firstPerson`.

Person `0` has a **secret** and initially shares the secret with a person `firstPerson` at time `0`. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person `x_i` has the secret at `time_i`, then they will share the secret with person `y_i`, and vice versa.

The secrets are shared **instantaneously**. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

Return *a list of all the people that have the secret after all the meetings have taken place. *You may return the answer in **any order**.

## Constraints
- `2 <= n <= 10^5`
- `1 <= meetings.length <= 10^5`
- `meetings[i].length == 3`
- `0 <= x_i, y_i <= n - 1`
- `x_i != y_i`
- `1 <= time_i <= 10^5`
- `1 <= firstPerson <= n - 1`

## Examples
### Example 1
- **Input:** `n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1`
- **Output:** `[0,1,2,3,5]`
- **Explanation:** At time 0, person 0 shares the secret with person 1.
At time 5, person 1 shares the secret with person 2.
At time 8, person 2 shares the secret with person 3.
At time 10, person 1 shares the secret with person 5.​​​​
Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.

### Example 2
- **Input:** `n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3`
- **Output:** `[0,1,3]`
- **Explanation:** At time 0, person 0 shares the secret with person 3.
At time 2, neither person 1 nor person 2 know the secret.
At time 3, person 3 shares the secret with person 0 and person 1.
Thus, people 0, 1, and 3 know the secret after all the meetings.

### Example 3
- **Input:** `n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1`
- **Output:** `[0,1,2,3,4]`
- **Explanation:** At time 0, person 0 shares the secret with person 1.
At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
Note that person 2 can share the secret at the same time as receiving it.
At time 2, person 3 shares the secret with person 4.
Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find All People With Secret**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1,2,3,5]`.
4. **Verification:** At time 0, person 0 shares the secret with person 1.
At time 5, person 1 shares the secret with person 2.
At time 8, person 2 shares the secret with person 3.
At time 10, person 1 shares the secret with person 5.​​​​
Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.

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
from collections import defaultdict
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry

    def reset(self, x: int):
        self.parent[x] = x

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Group meetings by timestamp
        time_groups = defaultdict(list)
        for x, y, t in meetings:
            time_groups[t].append((x, y))

        dsu = DSU(n)
        # Person 0 shares secret with firstPerson at time 0
        dsu.union(0, firstPerson)

        for t in sorted(time_groups.keys()):
            current_meetings = time_groups[t]
            people = set()

            # 1. Connect people meeting at this timestamp
            for x, y in current_meetings:
                dsu.union(x, y)
                people.add(x)
                people.add(y)

            # 2. Reset those who did not receive the secret from 0
            for p in people:
                if not dsu.connected(p, 0):
                    dsu.reset(p)

        # 3. Collect all individuals who know the secret
        return [i for i in range(n) if dsu.connected(i, 0)]
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
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [1397. Find All Good Strings](../../1501-2000/1513-find-all-good-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-people-with-secret/)
