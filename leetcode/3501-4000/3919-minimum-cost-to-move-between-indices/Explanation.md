# LeetCode 3919: Minimum Cost to Move Between Indices

**LeetCode Problem #3919 — Minimum Cost to Move Between Indices**
Solve LeetCode Minimum Cost to Move Between Indices using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Move Between Indices |
| LeetCode | #3919 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` where `nums` is ** strictly increasing **.

For each index `x`, let `closest(x)` be the **adjacent** index `y` such that `abs(nums[x] - nums[y])` is **minimized**. If both **adjacent** indices exist and give the same difference, choose the **smaller** index.

From any index `x`, you can move in two ways:

To any index `y` with cost `abs(nums[x] - nums[y])`, or 
 To `closest(x)` with cost 1.

You are also given a 2D integer array `queries`, where each `queries[i] = [l_i, r_i]`.

For each query, calculate the **minimum total cost** to move from index `l_i` to index `r_i`.

Return an integer array `ans`, where `ans[i]` is the answer for the `i^th` query.

The **absolute difference** between two values `x` and `y` is defined as `abs(x - y)`.

## Constraints
- `2 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is strictly increasing
- `1 <= queries.length <= 10^5`
- `queries[i] = [l_i, r_i]`​​​​​​​
- `0 <= l_i, r_i < nums.length`

## Examples
### Example 1
- **Input:** `nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]`
- **Output:** `[6,2,5]`
- **Explanation:** ​​​​​​​​​​​​​​​​​​​​ 

 
 The closest indices are `[1, 0, 1]` respectively. 
 For `[0, 2]`, the path `0 &rarr; 1 &rarr; 2` uses a closest move from index 0 to 1 with cost 1 and a move from index 1 to 2 with cost `|-2 - 3| = 5`, giving total `1 + 5 = 6`. 
 For `[2, 0]`, the path `2 &rarr; 1 &rarr; 0` uses two closest moves from index 2 to 1 and from index 1 to 0, each with cost 1, giving total 2. 
 For `[1, 2]`, the direct move from index 1 to index 2 has cost `|-2 - 3| = 5`, which is optimal. 
 

 Thus, `ans = [6, 2, 5]`.

### Example 2
- **Input:** `nums = [0,2,3,9], queries = [[3,0],[1,2],[2,0]]`
- **Output:** `[4,1,3]`
- **Explanation:** The closest indices are `[1, 2, 1, 2]` respectively. 
 For `[3, 0]`, the path `3 &rarr; 2 &rarr; 1 &rarr; 0` uses closest moves from index 3 to 2 and from 2 to 1, each with cost 1, and a move from 1 to 0 with cost `|2 - 0| = 2`, giving total `1 + 1 + 2 = 4`. 
 For `[1, 2]`, the closest move from index 1 to 2 has cost 1. 
 For `[2, 0]`, the path `2 &rarr; 1 &rarr; 0` uses a closest move from index 2 to 1 with cost 1 and a move from 1 to 0 with cost `|2 - 0| = 2`, giving total `1 + 2 = 3`. 
 

 Thus, `ans = [4, 1, 3]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost to Move Between Indices**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,2,5]`.
4. **Verification:** ​​​​​​​​​​​​​​​​​​​​ 

 
 The closest indices are `[1, 0, 1]` respectively. 
 For `[0, 2]`, the path `0 &rarr; 1 &rarr; 2` uses a closest move from index 0 to 1 with cost 1 and a move from index 1 to 2 with cost `|-2 - 3| = 5`, giving total `1 + 5 = 6`. 
 For `[2, 0]`, the path `2 &rarr; 1 &rarr; 0` uses two closest moves from index 2 to 1 and from index 1 to 0, each with cost 1, giving total 2. 
 For `[1, 2]`, the direct move from index 1 to index 2 has cost `|-2 - 3| = 5`, which is optimal. 
 

 Thus, `ans = [6, 2, 5]`.

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
    def minCost(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        def closest(i):
            if i == 0:
                return 1
            if i == n - 1:
                return n - 2
            return i - 1 if nums[i] - nums[i - 1] <= nums[i + 1] - nums[i] else i + 1

        PR = [0] * n
        for i in range(n - 1):
            step = 1 if closest(i) == i + 1 else nums[i + 1] - nums[i]
            PR[i + 1] = PR[i] + step

        PL = [0] * n
        for i in range(1, n):
            step = 1 if closest(i) == i - 1 else nums[i] - nums[i - 1]
            PL[i] = PL[i - 1] + step

        ans = []
        for l, r in queries:
            if l <= r:
                ans.append(PR[r] - PR[l])
            else:
                ans.append(PL[l] - PL[r])
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
- [1217. Minimum Cost to Move Chips to The Same Position](../../1001-1500/1217-minimum-cost-to-move-chips-to-the-same-position/)
- [1000. Minimum Cost to Merge Stones](../../0501-1000/1000-minimum-cost-to-merge-stones/)
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1130-minimum-cost-tree-from-leaf-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-move-between-indices/)
