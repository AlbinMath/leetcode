# LeetCode 2271: Maximum White Tiles Covered by a Carpet

**LeetCode Problem #2271 — Maximum White Tiles Covered by a Carpet**
Solve LeetCode Maximum White Tiles Covered by a Carpet using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum White Tiles Covered by a Carpet |
| LeetCode | #2271 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `tiles` where `tiles[i] = [l_i, r_i]` represents that every tile `j` in the range `l_i <= j <= r_i` is colored white.

You are also given an integer `carpetLen`, the length of a single carpet that can be placed **anywhere**.

Return *the **maximum** number of white tiles that can be covered by the carpet*.

## Constraints
- `1 <= tiles.length <= 5 * 10^4`
- `tiles[i].length == 2`
- `1 <= l_i <= r_i <= 10^9`
- `1 <= carpetLen <= 10^9`
- The `tiles` are **non-overlapping**.

## Examples
### Example 1
- **Input:** `tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10`
- **Output:** `9`
- **Explanation:** Place the carpet starting on tile 10. 
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.

### Example 2
- **Input:** `tiles = [[10,11],[1,1]], carpetLen = 2`
- **Output:** `2`
- **Explanation:** Place the carpet starting on tile 10. 
It covers 2 white tiles, so we return 2.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum White Tiles Covered by a Carpet**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** Place the carpet starting on tile 10. 
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.

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
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        
        right = 0
        full_cover = 0
        max_tiles = 0
        
        for left in range(n):
            end_pos = tiles[left][0] + carpetLen - 1
            
            while right < n and tiles[right][1] <= end_pos:
                full_cover += tiles[right][1] - tiles[right][0] + 1
                right += 1
                
            if right < n and tiles[right][0] <= end_pos:
                partial = end_pos - tiles[right][0] + 1
                if full_cover + partial > max_tiles:
                    max_tiles = full_cover + partial
            elif full_cover > max_tiles:
                max_tiles = full_cover
                
            if max_tiles == carpetLen:
                return carpetLen
                
            if left < right:
                full_cover -= tiles[left][1] - tiles[left][0] + 1
            else:
                right = left + 1
                
        return max_tiles
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
- [2209. Minimum White Tiles After Covering With Carpets](../../2001-2500/2209-minimum-white-tiles-after-covering-with-carpets/)
- [2397. Maximum Rows Covered by Columns](../../2001-2500/2397-maximum-rows-covered-by-columns/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/)
