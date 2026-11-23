# LeetCode 3454: Separate Squares II

**LeetCode Problem #3454 — Separate Squares II**
Solve LeetCode Separate Squares II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Separate Squares II |
| LeetCode | #3454 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `squares`. Each `squares[i] = [x_i, y_i, l_i]` represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the **minimum** y-coordinate value of a horizontal line such that the total area covered by squares above the line *equals* the total area covered by squares below the line.

Answers within `10^-5` of the actual answer will be accepted.

**Note**: Squares **may** overlap. Overlapping areas should be counted **only once** in this version.

## Constraints
- `1 <= squares.length <= 5 * 10^4`
- `squares[i] = [x_i, y_i, l_i]`
- `squares[i].length == 3`
- `0 <= x_i, y_i <= 10^9`
- `1 <= l_i <= 10^9`
- The total area of all the squares will not exceed `10^15`.

## Examples
### Example 1
- **Input:** `squares = [[0,0,1],[2,2,1]]`
- **Output:** `1.00000`
- **Explanation:** Any horizontal line between `y = 1` and `y = 2` results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

### Example 2
- **Input:** `squares = [[0,0,2],[1,1,1]]`
- **Output:** `1.00000`
- **Explanation:** Since the blue square overlaps with the red square, it will not be counted again. Thus, the line `y = 1` splits the squares into two equal parts.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Separate Squares II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `squares = [[0,0,1],[2,2,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1.00000`.
4. **Verification:** Any horizontal line between `y = 1` and `y = 2` results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

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
from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = sorted({x for x, _, l in squares} | {x + l for x, _, l in squares})
        idx = {v: i for i, v in enumerate(xs)}
        m = len(xs) - 1  # number of elementary segments
        cnt = [0] * (4 * m)
        ln = [0] * (4 * m)

        def update(node, lo, hi, a, b, v):
            if a >= hi or b <= lo:
                return
            if a <= lo and hi <= b:
                cnt[node] += v
            else:
                mid = (lo + hi) // 2
                update(node * 2, lo, mid, a, b, v)
                update(node * 2 + 1, mid, hi, a, b, v)
            if cnt[node] > 0:
                ln[node] = xs[hi] - xs[lo]
            elif hi - lo == 1:
                ln[node] = 0
            else:
                ln[node] = ln[node * 2] + ln[node * 2 + 1]

        events = []
        for x, y, l in squares:
            a, b = idx[x], idx[x + l]
            events.append((y, 1, a, b))
            events.append((y + l, -1, a, b))
        events.sort()

        # pass 1: total area, recording strips
        strips = []  # (y_start, width, height)
        total = 0
        prev_y = events[0][0]
        for y, v, a, b in events:
            if y > prev_y:
                w = ln[1]
                total += w * (y - prev_y)
                strips.append((prev_y, w, y - prev_y))
                prev_y = y
            update(1, 0, m, a, b, v)

        # pass 2: find the crossing strip (compare 2*acc with total to stay exact)
        acc = 0
        for y0, w, h in strips:
            if w > 0 and 2 * (acc + w * h) >= total:
                return y0 + (total / 2 - acc) / w
            acc += w * h
        return float(prev_y)
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
- [1977. Number of Ways to Separate Numbers](../../2001-2500/2091-number-of-ways-to-separate-numbers/)
- [2553. Separate the Digits in an Array](../../2501-3000/2639-separate-the-digits-in-an-array/)
- [279. Perfect Squares](../../0001-0500/0279-perfect-squares/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/separate-squares-ii/)
