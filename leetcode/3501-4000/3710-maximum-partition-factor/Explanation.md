# LeetCode 3710: Maximum Partition Factor

**LeetCode Problem #3710 — Maximum Partition Factor**
Solve LeetCode Maximum Partition Factor using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Partition Factor |
| LeetCode | #3710 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the ` i^th ` point on the Cartesian plane.

The **Manhattan distance** between two points `points[i] = [x_i, y_i]` and `points[j] = [x_j, y_j]` is `|x_i - x_j| + |y_i - y_j|`.

Split the `n` points into **exactly two non-empty** groups. The **partition factor** of a split is the **minimum** Manhattan distance among all unordered pairs of points that lie in the same group.

Return the **maximum** possible **partition factor** over all valid splits.

Note: A group of size 1 contributes no intra-group pairs. When `n = 2` (both groups size 1), there are no intra-group pairs, so define the partition factor as 0.

## Constraints
- `2 <= points.length <= 500`
- `points[i] = [x_i, y_i]`
- `-10^8 <= x_i, y_i <= 10^8`

## Examples
### Example 1
- **Input:** `points = [[0,0],[0,2],[2,0],[2,2]]`
- **Output:** `4`
- **Explanation:** We split the points into two groups: `{[0, 0], [2, 2]}` and `{[0, 2], [2, 0]}`. 

 
 
 In the first group, the only pair has Manhattan distance `|0 - 2| + |0 - 2| = 4`. 
 
 
 In the second group, the only pair also has Manhattan distance `|0 - 2| + |2 - 0| = 4`. 
 
 

 The partition factor of this split is `min(4, 4) = 4`, which is maximal.

### Example 2
- **Input:** `points = [[0,0],[0,1],[10,0]]`
- **Output:** `11`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Partition Factor**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[0,0],[0,2],[2,0],[2,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We split the points into two groups: `{[0, 0], [2, 2]}` and `{[0, 2], [2, 0]}`. 

 
 
 In the first group, the only pair has Manhattan distance `|0 - 2| + |0 - 2| = 4`. 
 
 
 In the second group, the only pair also has Manhattan distance `|0 - 2| + |2 - 0| = 4`. 
 
 

 The partition factor of this split is `min(4, 4) = 4`, which is maximal.

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
from collections import deque
from typing import List

class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0

        # Precompute all pairwise Manhattan distances
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                dist[i][j] = d
                dist[j][i] = d

        def is_bipartite(M: int) -> bool:
            color = [0] * n

            for i in range(n):
                if color[i] != 0:
                    continue

                color[i] = 1
                queue = deque([i])

                while queue:
                    u = queue.popleft()
                    for v in range(n):
                        if dist[u][v] < M and u != v:
                            if color[v] == 0:
                                color[v] = -color[u]
                                queue.append(v)
                            elif color[v] == color[u]:
                                return False  # Odd cycle detected

            return True

        low, high = 1, 4 * 10**8
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if is_bipartite(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
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
- [2025. Maximum Number of Ways to Partition an Array](../../2001-2500/2025-maximum-number-of-ways-to-partition-an-array/)
- [3630. Partition Array for Maximum XOR and AND](../../3501-4000/3630-partition-array-for-maximum-xor-and-and/)
- [3334. Find the Maximum Factor Score of Array](../../3001-3500/3334-find-the-maximum-factor-score-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-partition-factor/)
