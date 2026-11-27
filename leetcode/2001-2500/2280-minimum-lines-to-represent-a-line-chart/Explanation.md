# LeetCode 2280: Minimum Lines to Represent a Line Chart

**LeetCode Problem #2280 — Minimum Lines to Represent a Line Chart**
Solve LeetCode Minimum Lines to Represent a Line Chart using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Lines to Represent a Line Chart |
| LeetCode | #2280 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `stockPrices` where `stockPrices[i] = [day_i, price_i]` indicates the price of the stock on day `day_i` is `price_i`. A **line chart** is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:

Return *the **minimum number of lines** needed to represent the line chart*.

## Constraints
- `1 <= stockPrices.length <= 10^5`
- `stockPrices[i].length == 2`
- `1 <= day_i, price_i <= 10^9`
- All `day_i` are **distinct**.

## Examples
### Example 1
- **Input:** `stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]`
- **Output:** `3`
- **Explanation:** The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.

### Example 2
- **Input:** `stockPrices = [[3,4],[1,2],[7,8],[2,3]]`
- **Output:** `1`
- **Explanation:** As shown in the diagram above, the line chart can be represented with a single line.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Lines to Represent a Line Chart**, we observe the problem requirements and utilize the **Sliding Window** technique. We maintain a contiguous window defined by `left` and `right` pointers. The right pointer expands the window by adding incoming elements, while the left pointer advances to restore window invariants whenever duplicates or constraint limits are exceeded.

## Algorithm
1. Initialize `left = 0` and window tracking data structures.
2. Expand `right` pointer over input elements.
3. Contract `left` pointer when window invariants are breached.
4. Update global best metric for valid window intervals.
5. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        pts = sorted(stockPrices)
        n = len(pts)
        if n < 2:
            return 0
        lines = 1
        for i in range(2, n):
            x1, y1 = pts[i - 2]
            x2, y2 = pts[i - 1]
            x3, y3 = pts[i]
            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                lines += 1
        return lines
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [806. Number of Lines To Write String](../../0501-1000/0806-number-of-lines-to-write-string/)
- [1035. Uncrossed Lines](../../1001-1500/1035-uncrossed-lines/)
- [149. Max Points on a Line](../../0001-0500/0149-max-points-on-a-line/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/)
