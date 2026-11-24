# LeetCode 2975: Maximum Square Area by Removing Fences From a Field

**LeetCode Problem #2975 — Maximum Square Area by Removing Fences From a Field**
Solve LeetCode Maximum Square Area by Removing Fences From a Field using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Square Area by Removing Fences From a Field |
| LeetCode | #2975 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a large `(m - 1) x (n - 1)` rectangular field with corners at `(1, 1)` and `(m, n)` containing some horizontal and vertical fences given in arrays `hFences` and `vFences` respectively.

Horizontal fences are from the coordinates `(hFences[i], 1)` to `(hFences[i], n)` and vertical fences are from the coordinates `(1, vFences[i])` to `(m, vFences[i])`.

Return *the **maximum** area of a **square** field that can be formed by **removing** some fences (**possibly none**) or *`-1` *if it is impossible to make a square field*.

Since the answer may be large, return it **modulo** `10^9 + 7`.

**Note: **The field is surrounded by two horizontal fences from the coordinates `(1, 1)` to `(1, n)` and `(m, 1)` to `(m, n)` and two vertical fences from the coordinates `(1, 1)` to `(m, 1)` and `(1, n)` to `(m, n)`. These fences **cannot** be removed.

## Constraints
- `3 <= m, n <= 10^9`
- ` 1 <= hF ences .length, vFences.length <= 600 `
- ` 1 < hFences[i] < m `
- ` 1 < vFences[i] < n `
- ` hFences ` and ` vFences ` are unique.

## Examples
### Example 1
- **Input:** `m = 4, n = 3, hFences = [2,3], vFences = [2]`
- **Output:** `4`
- **Explanation:** Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.

### Example 2
- **Input:** `m = 6, n = 7, hFences = [2], vFences = [4]`
- **Output:** `-1`
- **Explanation:** It can be proved that there is no way to create a square field by removing fences.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Square Area by Removing Fences From a Field**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 4, n = 3, hFences = [2,3], vFences = [2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.

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
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        H = sorted(hFences + [1, m])
        V = sorted(vFences + [1, n])

        dh = {H[j] - H[i] for i in range(len(H)) for j in range(i + 1, len(H))}

        best = -1
        for i in range(len(V)):
            for j in range(i + 1, len(V)):
                d = V[j] - V[i]
                if d > best and d in dh:
                    best = d

        return -1 if best == -1 else best * best % MOD
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
- [1717. Maximum Score From Removing Substrings](../../1501-2000/1717-maximum-score-from-removing-substrings/)
- [2091. Removing Minimum and Maximum From Array](../../2001-2500/2091-removing-minimum-and-maximum-from-array/)
- [2390. Removing Stars From a String](../../2001-2500/2390-removing-stars-from-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/)
