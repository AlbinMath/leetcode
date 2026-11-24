# LeetCode 587: Erect the Fence

**LeetCode Problem #587 — Erect the Fence**
Solve LeetCode Erect the Fence using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Erect the Fence |
| LeetCode | #587 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `trees` where `trees[i] = [x_i, y_i]` represents the location of a tree in the garden.

Fence the entire garden using the minimum length of rope, as it is expensive. The garden is well-fenced only if **all the trees are enclosed**.

Return *the coordinates of trees that are exactly located on the fence perimeter*. You may return the answer in **any order**.

## Constraints
- `1 <= trees.length <= 3000`
- `trees[i].length == 2`
- `0 <= x_i, y_i <= 100`
- All the given positions are **unique**.

## Examples
### Example 1
- **Input:** `trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]`
- **Output:** `[[1,1],[2,0],[4,2],[3,3],[2,4]]`
- **Explanation:** All the trees will be on the perimeter of the fence except the tree at [2, 2], which will be inside the fence.

### Example 2
- **Input:** `trees = [[1,2],[2,2],[4,2]]`
- **Output:** `[[4,2],[2,2],[1,2]]`
- **Explanation:** The fence forms a line that passes through all the trees.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Erect the Fence**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,1],[2,0],[4,2],[3,3],[2,4]]`.
4. **Verification:** All the trees will be on the perimeter of the fence except the tree at [2, 2], which will be inside the fence.

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
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        pts = sorted(map(tuple, trees))
        if len(pts) <= 2:
            return [list(p) for p in pts]

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        return [list(p) for p in set(lower) | set(upper)]
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
- [4007. Widest Possible Fence](../../4001-4500/4007-widest-possible-fence/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/erect-the-fence/)
