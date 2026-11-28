# LeetCode 3049: Earliest Second to Mark Indices II

**LeetCode Problem #3049 — Earliest Second to Mark Indices II**
Solve LeetCode Earliest Second to Mark Indices II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Earliest Second to Mark Indices II |
| LeetCode | #3049 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two **1-indexed** integer arrays, `nums` and, `changeIndices`, having lengths `n` and `m`, respectively.

Initially, all indices in `nums` are unmarked. Your task is to mark **all** indices in `nums`.

In each second, `s`, in order from `1` to `m` (**inclusive**), you can perform **one** of the following operations:

Choose an index `i` in the range `[1, n]` and **decrement** `nums[i]` by `1`. 
 Set `nums[changeIndices[s]]` to any **non-negative** value. 
 Choose an index `i` in the range `[1, n]`, where `nums[i]` is **equal** to `0`, and **mark** index `i`. 
 Do nothing.

Return *an integer denoting the **earliest second** in the range *`[1, m]`* when **all** indices in *`nums`* can be marked by choosing operations optimally, or *`-1`* if it is impossible.*

## Constraints
- `1 <= n == nums.length <= 5000`
- `0 <= nums[i] <= 10^9`
- `1 <= m == changeIndices.length <= 5000`
- `1 <= changeIndices[i] <= n`

## Examples
### Example 1
- **Input:** `nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]`
- **Output:** `6`
- **Explanation:** In this example, we have 7 seconds. The following operations can be performed to mark all indices:
Second 1: Set nums[changeIndices[1]] to 0. nums becomes [0,2,3].
Second 2: Set nums[changeIndices[2]] to 0. nums becomes [0,2,0].
Second 3: Set nums[changeIndices[3]] to 0. nums becomes [0,0,0].
Second 4: Mark index 1, since nums[1] is equal to 0.
Second 5: Mark index 2, since nums[2] is equal to 0.
Second 6: Mark index 3, since nums[3] is equal to 0.
Now all indices have been marked.
It can be shown that it is not possible to mark all indices earlier than the 6th second.
Hence, the answer is 6.

### Example 2
- **Input:** `nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2]`
- **Output:** `7`
- **Explanation:** In this example, we have 8 seconds. The following operations can be performed to mark all indices:
Second 1: Mark index 1, since nums[1] is equal to 0.
Second 2: Mark index 2, since nums[2] is equal to 0.
Second 3: Decrement index 4 by one. nums becomes [0,0,1,1].
Second 4: Decrement index 4 by one. nums becomes [0,0,1,0].
Second 5: Decrement index 3 by one. nums becomes [0,0,0,0].
Second 6: Mark index 3, since nums[3] is equal to 0.
Second 7: Mark index 4, since nums[4] is equal to 0.
Now all indices have been marked.
It can be shown that it is not possible to mark all indices earlier than the 7th second.
Hence, the answer is 7.

### Example 3
- **Input:** `nums = [1,2,3], changeIndices = [1,2,3]`
- **Output:** `-1`
- **Explanation:** In this example, it can be shown that it is impossible to mark all indices, as we don't have enough seconds. 
Hence, the answer is -1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Earliest Second to Mark Indices II**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** In this example, we have 7 seconds. The following operations can be performed to mark all indices:
Second 1: Set nums[changeIndices[1]] to 0. nums becomes [0,2,3].
Second 2: Set nums[changeIndices[2]] to 0. nums becomes [0,2,0].
Second 3: Set nums[changeIndices[3]] to 0. nums becomes [0,0,0].
Second 4: Mark index 1, since nums[1] is equal to 0.
Second 5: Mark index 2, since nums[2] is equal to 0.
Second 6: Mark index 3, since nums[3] is equal to 0.
Now all indices have been marked.
It can be shown that it is not possible to mark all indices earlier than the 6th second.
Hence, the answer is 6.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq
from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        base = sum(nums) + n          # cost if every index is handled "plain"

        def can(T: int) -> bool:
            first = {}
            for s in range(T):
                first.setdefault(changeIndices[s], s)

            heap = []                 # values of indices currently chosen to be zeroed
            cnt = 0                   # free seconds to the right, usable as mark seconds
            saved = 0                 # sum of (v - 1) over zeroed indices
            for s in range(T - 1, -1, -1):
                i = changeIndices[s]
                v = nums[i - 1]
                if first[i] != s or v <= 1:
                    cnt += 1
                elif cnt > 0:
                    cnt -= 1
                    heapq.heappush(heap, v)
                    saved += v - 1
                elif heap and heap[0] < v:
                    small = heapq.heapreplace(heap, v)
                    saved += v - small
                    cnt += 1          # fix: freed mark slot + freed set second - new mark slot
                else:
                    cnt += 1
            return base - saved <= T

        if not can(m):
            return -1

        lo, hi = 1, m
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [3048. Earliest Second to Mark Indices I](../../3001-3500/3048-earliest-second-to-mark-indices-i/)
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2089-find-target-indices-after-sorting-array/)
- [2164. Sort Even and Odd Indices Independently](../../2001-2500/2164-sort-even-and-odd-indices-independently/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/earliest-second-to-mark-indices-ii/)
