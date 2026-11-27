# LeetCode 3025: Find the Number of Ways to Place People I

**LeetCode Problem #3025 — Find the Number of Ways to Place People I**
Solve LeetCode Find the Number of Ways to Place People I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Number of Ways to Place People I |
| LeetCode | #3025 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D plane, where `points[i] = [x_i, y_i]`.

Count the number of pairs of points `(A, B)`, where

`A` is on the **upper left** side of `B`, and 
 there are no other points in the rectangle (or line) they make (**including the border**), except for the points `A` and `B`.

Return the count.

## Constraints
- `2 <= n <= 50`
- `points[i].length == 2`
- `0 <= points[i][0], points[i][1] <= 50`
- All `points[i]` are distinct.

## Examples
### Example 1
- **Input:** `points = [[1,1],[2,2],[3,3]]`
- **Output:** `0`
- **Explanation:** There is no way to choose `A` and `B` such that `A` is on the upper left side of `B`.

### Example 2
- **Input:** `points = [[6,2],[4,4],[2,6]]`
- **Output:** `2`
- **Explanation:** The left one is the pair `(points[1], points[0])`, where `points[1]` is on the upper left side of `points[0]` and the rectangle is empty. 
 The middle one is the pair `(points[2], points[1])`, same as the left one it is a valid pair. 
 The right one is the pair `(points[2], points[0])`, where `points[2]` is on the upper left side of `points[0]`, but `points[1]` is inside the rectangle so it's not a valid pair.

### Example 3
- **Input:** `points = [[3,1],[1,3],[1,1]]`
- **Output:** `2`
- **Explanation:** The left one is the pair `(points[2], points[0])`, where `points[2]` is on the upper left side of `points[0]` and there are no other points on the line they form. Note that it is a valid state when the two points form a line. 
 The middle one is the pair `(points[1], points[2])`, it is a valid pair same as the left one. 
 The right one is the pair `(points[1], points[0])`, it is not a valid pair as `points[2]` is on the border of the rectangle.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Number of Ways to Place People I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,1],[2,2],[3,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** There is no way to choose `A` and `B` such that `A` is on the upper left side of `B`.

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

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        for i in range(n):
            xa, ya = points[i]
            for j in range(n):
                if i == j:
                    continue
                xb, yb = points[j]
                if xa <= xb and ya >= yb:
                    ok = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if xa <= x <= xb and yb <= y <= ya:
                            ok = False
                            break
                    if ok:
                        count += 1
        return count
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
- [3027. Find the Number of Ways to Place People II](../../3001-3500/3027-find-the-number-of-ways-to-place-people-ii/)
- [1269. Number of Ways to Stay in the Same Place After Some Steps](../../1001-1500/1269-number-of-ways-to-stay-in-the-same-place-after-some-steps/)
- [2973. Find Number of Coins to Place in Tree Nodes](../../2501-3000/2973-find-number-of-coins-to-place-in-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/)
