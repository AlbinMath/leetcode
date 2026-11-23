# LeetCode 3873: Maximum Points Activated with One Addition

**LeetCode Problem #3873 — Maximum Points Activated with One Addition**
Solve LeetCode Maximum Points Activated with One Addition using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Points Activated with One Addition |
| LeetCode | #3873 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the `i^th` point. All coordinates in `points` are **distinct**.

If a point is **activated**, then all points that have the **same** x-coordinate **or** y-coordinate become **activated** as well.

Activation continues until no additional points can be activated.

You may add **one additional** point at any integer coordinate `(x, y)` not already present in `points`. Activation begins by **activating** this **newly added point**.

Return an integer denoting the **maximum** number of points that can be activated, including the newly added point.

## Constraints
- `1 <= points.length <= 10^5`
- `points[i] = [x_i, y_i]`
- `-10^9 <= x_i, y_i <= 10^9`
- `points` contains all **distinct** coordinates.

## Examples
### Example 1
- **Input:** `points = [[1,1],[1,2],[2,2]]`
- **Output:** `4`
- **Explanation:** Adding and activating a point such as `(1, 3)` causes activations: 

 
 `(1, 3)` shares `x = 1` with `(1, 1)` and `(1, 2)` -> `(1, 1)` and `(1, 2)` become activated. 
 `(1, 2)` shares `y = 2` with `(2, 2)` -> `(2, 2)` becomes activated. 
 

 Thus, the activated points are `(1, 3)`, `(1, 1)`, `(1, 2)`, `(2, 2)`, so 4 points in total. We can show this is the maximum activated.

### Example 2
- **Input:** `points = [[2,2],[1,1],[3,3]]`
- **Output:** `3`
- **Explanation:** Adding and activating a point such as `(1, 2)` causes activations: 

 
 `(1, 2)` shares `x = 1` with `(1, 1)` -> `(1, 1)` becomes activated. 
 `(1, 2)` shares `y = 2` with `(2, 2)` -> `(2, 2)` becomes activated. 
 

 Thus, the activated points are `(1, 2)`, `(1, 1)`, `(2, 2)`, so 3 points in total. We can show this is the maximum activated.

### Example 3
- **Input:** `points = [[2,3],[2,2],[1,1],[4,5]]`
- **Output:** `4`
- **Explanation:** Adding and activating a point such as `(2, 1)` causes activations: 

 
 `(2, 1)` shares `x = 2` with `(2, 3)` and `(2, 2)` -> `(2, 3)` and `(2, 2)` become activated. 
 `(2, 1)` shares `y = 1` with `(1, 1)` -> `(1, 1)` becomes activated. 
 

 Thus, the activated points are `(2, 1)`, `(2, 3)`, `(2, 2)`, `(1, 1)`, so 4 points in total.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Points Activated with One Addition**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,1],[1,2],[2,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Adding and activating a point such as `(1, 3)` causes activations: 

 
 `(1, 3)` shares `x = 1` with `(1, 1)` and `(1, 2)` -> `(1, 1)` and `(1, 2)` become activated. 
 `(1, 2)` shares `y = 2` with `(2, 2)` -> `(2, 2)` becomes activated. 
 

 Thus, the activated points are `(1, 3)`, `(1, 1)`, `(1, 2)`, `(2, 2)`, so 4 points in total. We can show this is the maximum activated.

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
        self.size = [1] * n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.size[rx] < self.size[ry]:
                rx, ry = ry, rx
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]


class Solution:
    def maxActivated(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)

        # Map each coordinate to the index of the first point seen with that coordinate
        x_first = {}
        y_first = {}

        for i, (x, y) in enumerate(points):
            if x in x_first:
                dsu.union(i, x_first[x])
            else:
                x_first[x] = i

            if y in y_first:
                dsu.union(i, y_first[y])
            else:
                y_first[y] = i

        # Collect component sizes for all unique roots
        comp_sizes = [dsu.size[i] for i in range(n) if dsu.parent[i] == i]
        comp_sizes.sort(reverse=True)

        if len(comp_sizes) >= 2:
            return comp_sizes[0] + comp_sizes[1] + 1
        return comp_sizes[0] + 1
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
- [1423. Maximum Points You Can Obtain from Cards](../../1501-2000/1538-maximum-points-you-can-obtain-from-cards/)
- [1610. Maximum Number of Visible Points](../../1501-2000/1733-maximum-number-of-visible-points/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-points-activated-with-one-addition/)
