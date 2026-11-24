# LeetCode 1889: Minimum Space Wasted From Packaging

**LeetCode Problem #1889 — Minimum Space Wasted From Packaging**
Solve LeetCode Minimum Space Wasted From Packaging using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Space Wasted From Packaging |
| LeetCode | #1889 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have `n` packages that you are trying to place in boxes, **one package in each box**. There are `m` suppliers that each produce boxes of **different sizes** (with infinite supply). A package can be placed in a box if the size of the package is **less than or equal to** the size of the box.

The package sizes are given as an integer array `packages`, where `packages[i]` is the **size** of the `i^th` package. The suppliers are given as a 2D integer array `boxes`, where `boxes[j]` is an array of **box sizes** that the `j^th` supplier produces.

You want to choose a **single supplier** and use boxes from them such that the **total wasted space **is **minimized**. For each package in a box, we define the space **wasted** to be `size of the box - size of the package`. The **total wasted space** is the sum of the space wasted in **all** the boxes.

For example, if you have to fit packages with sizes `[2,3,5]` and the supplier offers boxes of sizes `[4,8]`, you can fit the packages of size-`2` and size-`3` into two boxes of size-`4` and the package with size-`5` into a box of size-`8`. This would result in a waste of `(4-2) + (4-3) + (8-5) = 6`.

Return *the **minimum total wasted space** by choosing the box supplier **optimally**, or *`-1` if it is **impossible** to fit all the packages inside boxes. Since the answer may be **large**, return it **modulo **`10^9 + 7`.

## Constraints
- `n == packages.length`
- `m == boxes.length`
- `1 <= n <= 10^5`
- `1 <= m <= 10^5`
- `1 <= packages[i] <= 10^5`
- `1 <= boxes[j].length <= 10^5`
- `1 <= boxes[j][k] <= 10^5`
- `sum(boxes[j].length) <= 10^5`
- The elements in `boxes[j]` are **distinct**.

## Examples
### Example 1
- **Input:** `packages = [2,3,5], boxes = [[4,8],[2,8]]`
- **Output:** `6`
- **Explanation:** : It is optimal to choose the first supplier, using two size-4 boxes and one size-8 box.
The total waste is (4-2) + (4-3) + (8-5) = 6.

### Example 2
- **Input:** `packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]`
- **Output:** `-1`
- **Explanation:** There is no box that the package of size 5 can fit in.

### Example 3
- **Input:** `packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]`
- **Output:** `9`
- **Explanation:** It is optimal to choose the third supplier, using two size-5 boxes, two size-10 boxes, and two size-14 boxes.
The total waste is (5-3) + (5-5) + (10-8) + (10-10) + (14-11) + (14-12) = 9.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Space Wasted From Packaging**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `packages = [2,3,5], boxes = [[4,8],[2,8]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** : It is optimal to choose the first supplier, using two size-4 boxes and one size-8 box.
The total waste is (4-2) + (4-3) + (8-5) = 6.

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
from bisect import bisect_right
from typing import List

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10**9 + 7
        packages.sort()
        n = len(packages)
        total_pkg = sum(packages)
        max_pkg = packages[-1]

        best = float('inf')
        for supplier in boxes:
            supplier.sort()
            if supplier[-1] < max_pkg:
                continue

            used = 0
            prev = 0
            for b in supplier:
                idx = bisect_right(packages, b)
                if idx > prev:
                    used += b * (idx - prev)
                    prev = idx
                if prev == n:
                    break

            best = min(best, used - total_pkg)

        return -1 if best == float('inf') else best % MOD
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
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1130-minimum-cost-tree-from-leaf-values/)
- [2091. Removing Minimum and Maximum From Array](../../2001-2500/2091-removing-minimum-and-maximum-from-array/)
- [3858. Minimum Bitwise OR From Grid](../../3501-4000/3858-minimum-bitwise-or-from-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-space-wasted-from-packaging/)
