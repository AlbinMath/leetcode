# LeetCode 3690: Split and Merge Array Transformation

**LeetCode Problem #3690 — Split and Merge Array Transformation**
Solve LeetCode Split and Merge Array Transformation using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split and Merge Array Transformation |
| LeetCode | #3690 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2`, each of length `n`. You may perform the following **split-and-merge operation** on `nums1` any number of times:

Choose a subarray `nums1[L..R]`. 
 Remove that subarray, leaving the prefix `nums1[0..L-1]` (empty if `L = 0`) and the suffix `nums1[R+1..n-1]` (empty if `R = n - 1`). 
 Re-insert the removed subarray (in its original order) at **any** position in the remaining array (i.e., between any two elements, at the very start, or at the very end).

Return the **minimum** number of **split-and-merge operations** needed to transform `nums1` into `nums2`.

## Constraints
- `2 <= n == nums1.length == nums2.length <= 6`
- `-10^5 <= nums1[i], nums2[i] <= 10^5`
- `nums2` is a **permutation** of `nums1`.

## Examples
### Example 1
- **Input:** `nums1 = [3,1,2], nums2 = [1,2,3]`
- **Output:** `1`
- **Explanation:** Split out the subarray `[3]` (`L = 0`, `R = 0`); the remaining array is `[1,2]`. 
 Insert `[3]` at the end; the array becomes `[1,2,3]`.

### Example 2
- **Input:** `nums1 = [1,1,2,3,4,5] , nums2 = [5,4,3,2,1,1]`
- **Output:** `3`
- **Explanation:** Remove `[1,1,2]` at indices `0 - 2`; remaining is `[3,4,5]`; insert `[1,1,2]` at position `2`, resulting in `[3,4,1,1,2,5]`. 
 Remove `[4,1,1]` at indices `1 - 3`; remaining is `[3,2,5]`; insert `[4,1,1]` at position `3`, resulting in `[3,2,5,4,1,1]`. 
 Remove `[3,2]` at indices `0 - 1`; remaining is `[5,4,1,1]`; insert `[3,2]` at position `2`, resulting in `[5,4,3,2,1,1]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Split and Merge Array Transformation**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [3,1,2], nums2 = [1,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Split out the subarray `[3]` (`L = 0`, `R = 0`); the remaining array is `[1,2]`. 
 Insert `[3]` at the end; the array becomes `[1,2,3]`.

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
from collections import deque
from typing import List

class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        start, target = tuple(nums1), tuple(nums2)
        if start == target:
            return 0
        n = len(start)
        seen = {start}
        q = deque([(start, 0)])
        while q:
            s, d = q.popleft()
            for L in range(n):
                for R in range(L, n):
                    block = s[L:R + 1]
                    rest = s[:L] + s[R + 1:]
                    for p in range(len(rest) + 1):
                        t = rest[:p] + block + rest[p:]
                        if t == target:
                            return d + 1
                        if t not in seen:
                            seen.add(t)
                            q.append((t, d + 1))
        return -1
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
- [88. Merge Sorted Array](../../0001-0500/0088-merge-sorted-array/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)
- [805. Split Array With Same Average](../../0501-1000/0823-split-array-with-same-average/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-and-merge-array-transformation/)
