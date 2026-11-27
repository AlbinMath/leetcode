# LeetCode 3510: Minimum Pair Removal to Sort Array II

**LeetCode Problem #3510 — Minimum Pair Removal to Sort Array II**
Solve LeetCode Minimum Pair Removal to Sort Array II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Pair Removal to Sort Array II |
| LeetCode | #3510 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums`, you can perform the following operation any number of times:

Select the **adjacent** pair with the **minimum** sum in `nums`. If multiple such pairs exist, choose the leftmost one. 
 Replace the pair with their sum.

Return the **minimum number of operations** needed to make the array **non-decreasing**.

An array is said to be **non-decreasing** if each element is greater than or equal to its previous element (if it exists).

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [5,2,3,1]`
- **Output:** `2`
- **Explanation:** The pair `(3,1)` has the minimum sum of 4. After replacement, `nums = [5,2,4]`. 
 The pair `(2,4)` has the minimum sum of 6. After replacement, `nums = [5,6]`. 
 

 The array `nums` became non-decreasing in two operations.

### Example 2
- **Input:** `nums = [1,2,2]`
- **Output:** `0`
- **Explanation:** The array `nums` is already sorted.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Pair Removal to Sort Array II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,2,3,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The pair `(3,1)` has the minimum sum of 4. After replacement, `nums = [5,2,4]`. 
 The pair `(2,4)` has the minimum sum of 6. After replacement, `nums = [5,6]`. 
 

 The array `nums` became non-decreasing in two operations.

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
import heapq
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        a = nums[:]
        nxt = list(range(1, n + 1))          # nxt[i] == n means no next
        prv = list(range(-1, n - 1))         # prv[i] == -1 means no prev
        alive = [True] * n

        bad = sum(1 for i in range(n - 1) if a[i] > a[i + 1])
        heap = [(a[i] + a[i + 1], i) for i in range(n - 1)]
        heapq.heapify(heap)

        ops = 0
        while bad > 0:
            s, i = heapq.heappop(heap)
            # validate entry: i alive, has a next, and sum still matches
            if not alive[i]:
                continue
            j = nxt[i]
            if j >= n or not alive[j] or a[i] + a[j] != s:
                continue

            p = prv[i]
            k = nxt[j]

            # remove contributions of old pairs (p,i), (i,j), (j,k)
            if p >= 0 and a[p] > a[i]:
                bad -= 1
            if a[i] > a[j]:
                bad -= 1
            if k < n and a[j] > a[k]:
                bad -= 1

            # merge j into i
            a[i] = s
            alive[j] = False
            nxt[i] = k
            if k < n:
                prv[k] = i

            # add contributions of new pairs (p,i), (i,k)
            if p >= 0 and a[p] > a[i]:
                bad += 1
            if k < n and a[i] > a[k]:
                bad += 1

            # push new candidate pair sums
            if p >= 0:
                heapq.heappush(heap, (a[p] + a[i], p))
            if k < n:
                heapq.heappush(heap, (a[i] + a[k], i))

            ops += 1
        return ops
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
- [3507. Minimum Pair Removal to Sort Array I](../../3501-4000/3507-minimum-pair-removal-to-sort-array-i/)
- [2366. Minimum Replacements to Sort the Array](../../2001-2500/2366-minimum-replacements-to-sort-the-array/)
- [2856. Minimum Array Length After Pair Removals](../../2501-3000/2856-minimum-array-length-after-pair-removals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/)
