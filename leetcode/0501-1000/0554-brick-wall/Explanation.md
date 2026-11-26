# LeetCode 554: Brick Wall

**LeetCode Problem #554 — Brick Wall**
Solve LeetCode Brick Wall using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Brick Wall |
| LeetCode | #554 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a rectangular brick wall in front of you with `n` rows of bricks. The `i^th` row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array `wall` that contains the information about the wall, return *the minimum number of crossed bricks after drawing such a vertical line*.

## Constraints
- `n == wall.length`
- `1 <= n <= 10^4`
- `1 <= wall[i].length <= 10^4`
- `1 <= sum(wall[i].length) <= 2 * 10^4`
- `sum(wall[i])` is the same for each row `i`.
- `1 <= wall[i][j] <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]`
- **Output:** `2`

### Example 2
- **Input:** `wall = [[1],[1],[1]]`
- **Output:** `3`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Brick Wall**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

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
from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = defaultdict(int)
        
        for row in wall:
            prefix_width = 0
            for brick in row[:-1]:
                prefix_width += brick
                edge_counts[prefix_width] += 1
                
        max_aligned_edges = max(edge_counts.values(), default=0)
        return len(wall) - max_aligned_edges
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
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [27. Remove Element](../../0001-0500/0027-remove-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/brick-wall/)
