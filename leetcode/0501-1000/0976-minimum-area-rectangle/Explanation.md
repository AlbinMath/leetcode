# LeetCode 939: Minimum Area Rectangle

**LeetCode Problem #939 — Minimum Area Rectangle**
Solve LeetCode Minimum Area Rectangle using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Area Rectangle |
| LeetCode | #939 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of points in the **X-Y** plane `points` where `points[i] = [x_i, y_i]`.

Return *the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes*. If there is not any such rectangle, return `0`.

## Constraints
- `1 <= points.length <= 500`
- `points[i].length == 2`
- `0 <= x_i, y_i <= 4 * 10^4`
- All the given points are **unique**.

## Examples
### Example 1
- **Input:** `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`
- **Output:** `4`

### Example 2
- **Input:** `points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]`
- **Output:** `2`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Area Rectangle**, we observe the problem requirements and utilize the **Math & Logic** technique. By maintaining a **Primitive Types**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Primitive Types** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.

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

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        cols = defaultdict(list)
        for x, y in points:
            cols[x].append(y)

        last = {}                      # (y1, y2) -> most recent x containing both
        best = float('inf')
        for x in sorted(cols):
            ys = sorted(cols[x])
            for i in range(len(ys)):
                for j in range(i + 1, len(ys)):
                    pair = (ys[i], ys[j])
                    if pair in last:
                        best = min(best, (x - last[pair]) * (ys[j] - ys[i]))
                    last[pair] = x
        return 0 if best == float('inf') else best
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
- [963. Minimum Area Rectangle II](../../1001-1500/1003-minimum-area-rectangle-ii/)
- [223. Rectangle Area](../../0001-0500/0223-rectangle-area/)
- [850. Rectangle Area II](../../0501-1000/0880-rectangle-area-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-area-rectangle/)
