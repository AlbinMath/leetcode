# LeetCode 957: Prison Cells After N Days

**LeetCode Problem #957 — Prison Cells After N Days**
Solve LeetCode Prison Cells After N Days using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Prison Cells After N Days |
| LeetCode | #957 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `8` prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied. 
 Otherwise, it becomes vacant.

**Note** that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array `cells` where `cells[i] == 1` if the `i^th` cell is occupied and `cells[i] == 0` if the `i^th` cell is vacant, and you are given an integer `n`.

Return the state of the prison after `n` days (i.e., `n` such changes described above).

## Constraints
- `cells.length == 8`
- `cells[i]` is either `0` or `1`.
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `cells = [0,1,0,1,1,0,0,1], n = 7`
- **Output:** `[0,0,1,1,0,0,0,0]`
- **Explanation:** The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

### Example 2
- **Input:** `cells = [1,0,0,1,0,0,1,0], n = 1000000000`
- **Output:** `[0,0,1,1,1,1,1,0]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Prison Cells After N Days**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `cells = [0,1,0,1,1,0,0,1], n = 7`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,0,1,1,0,0,0,0]`.
4. **Verification:** The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

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
from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        state = 0
        for i, c in enumerate(cells):
            state |= c << i

        def step(x: int) -> int:
            return ~((x << 1) ^ (x >> 1)) & 0b01111110

        seen = {}
        day = 0
        while day < n:
            if state in seen:
                cycle = day - seen[state]
                n = day + (n - day) % cycle
                if day == n:
                    break
                seen.clear()   # avoid re-triggering the cycle shortcut
            seen[state] = day
            state = step(state)
            day += 1

        return [(state >> i) & 1 for i in range(8)]
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
- [1553. Minimum Number of Days to Eat N Oranges](../../1501-2000/1676-minimum-number-of-days-to-eat-n-oranges/)
- [1799. Maximize Score After N Operations](../../1501-2000/1906-maximize-score-after-n-operations/)
- [3179. Find the N-th Value After K Seconds](../../3001-3500/3422-find-the-n-th-value-after-k-seconds/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/prison-cells-after-n-days/)
