# LeetCode 3143: Maximum Points Inside the Square

**LeetCode Problem #3143 — Maximum Points Inside the Square**
Solve LeetCode Maximum Points Inside the Square using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Points Inside the Square |
| LeetCode | #3143 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D** **array `points` and a string `s` where, `points[i]` represents the coordinates of point `i`, and `s[i]` represents the **tag** of point `i`.

A **valid** square is a square centered at the origin `(0, 0)`, has edges parallel to the axes, and **does not** contain two points with the same tag.

Return the **maximum** number of points contained in a **valid** square.

A point is considered to be inside the square if it lies on or within the square's boundaries. 
 The side length of the square can be zero.

## Constraints
- `1 <= s.length, points.length <= 10^5`
- `points[i].length == 2`
- `-10^9 <= points[i][0], points[i][1] <= 10^9`
- `s.length == points.length`
- `points` consists of distinct coordinates.
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"`
- **Output:** `2`
- **Explanation:** The square of side length 4 covers two points `points[0]` and `points[1]`.

### Example 2
- **Input:** `points = [[1,1],[-2,-2],[-2,2]], s = "abb"`
- **Output:** `1`
- **Explanation:** The square of side length 2 covers one point, which is `points[0]`.

### Example 3
- **Input:** `points = [[1,1],[-1,-1],[2,-2]], s = "ccd"`
- **Output:** `0`
- **Explanation:** It's impossible to make any valid squares centered at the origin such that it covers only one point among `points[0]` and `points[1]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Points Inside the Square**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The square of side length 4 covers two points `points[0]` and `points[1]`.

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
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        INF = float('inf')
        first = [INF] * 26
        second = [INF] * 26

        ds = []
        for (x, y), ch in zip(points, s):
            d = max(abs(x), abs(y))
            ds.append(d)
            k = ord(ch) - 97
            if d < first[k]:
                second[k] = first[k]
                first[k] = d
            elif d < second[k]:
                second[k] = d

        limit = min(second) - 1
        return sum(1 for d in ds if d <= limit)
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
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](../../1001-1500/1292-maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)
- [1423. Maximum Points You Can Obtain from Cards](../../1001-1500/1423-maximum-points-you-can-obtain-from-cards/)
- [1453. Maximum Number of Darts Inside of a Circular Dartboard](../../1001-1500/1453-maximum-number-of-darts-inside-of-a-circular-dartboard/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-points-inside-the-square/)
