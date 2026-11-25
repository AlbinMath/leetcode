# LeetCode 3048: Earliest Second to Mark Indices I

**LeetCode Problem #3048 — Earliest Second to Mark Indices I**
Solve LeetCode Earliest Second to Mark Indices I using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Earliest Second to Mark Indices I |
| LeetCode | #3048 |
| Difficulty | Medium |
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
 If `nums[changeIndices[s]]` is **equal** to `0`, **mark** the index `changeIndices[s]`. 
 Do nothing.

Return *an integer denoting the **earliest second** in the range *`[1, m]`* when **all** indices in *`nums`* can be marked by choosing operations optimally, or *`-1`* if it is impossible.*

## Constraints
- `1 <= n == nums.length <= 2000`
- `0 <= nums[i] <= 10^9`
- `1 <= m == changeIndices.length <= 2000`
- `1 <= changeIndices[i] <= n`

## Examples
### Example 1
- **Input:** `nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]`
- **Output:** `8`
- **Explanation:** In this example, we have 8 seconds. The following operations can be performed to mark all indices:
Second 1: Choose index 1 and decrement nums[1] by one. nums becomes [1,2,0].
Second 2: Choose index 1 and decrement nums[1] by one. nums becomes [0,2,0].
Second 3: Choose index 2 and decrement nums[2] by one. nums becomes [0,1,0].
Second 4: Choose index 2 and decrement nums[2] by one. nums becomes [0,0,0].
Second 5: Mark the index changeIndices[5], which is marking index 3, since nums[3] is equal to 0.
Second 6: Mark the index changeIndices[6], which is marking index 2, since nums[2] is equal to 0.
Second 7: Do nothing.
Second 8: Mark the index changeIndices[8], which is marking index 1, since nums[1] is equal to 0.
Now all indices have been marked.
It can be shown that it is not possible to mark all indices earlier than the 8th second.
Hence, the answer is 8.

### Example 2
- **Input:** `nums = [1,3], changeIndices = [1,1,1,2,1,1,1]`
- **Output:** `6`
- **Explanation:** In this example, we have 7 seconds. The following operations can be performed to mark all indices:
Second 1: Choose index 2 and decrement nums[2] by one. nums becomes [1,2].
Second 2: Choose index 2 and decrement nums[2] by one. nums becomes [1,1].
Second 3: Choose index 2 and decrement nums[2] by one. nums becomes [1,0].
Second 4: Mark the index changeIndices[4], which is marking index 2, since nums[2] is equal to 0.
Second 5: Choose index 1 and decrement nums[1] by one. nums becomes [0,0].
Second 6: Mark the index changeIndices[6], which is marking index 1, since nums[1] is equal to 0.
Now all indices have been marked.
It can be shown that it is not possible to mark all indices earlier than the 6th second.
Hence, the answer is 6.

### Example 3
- **Input:** `nums = [0,1], changeIndices = [2,2,2]`
- **Output:** `-1`
- **Explanation:** In this example, it is impossible to mark all indices because index 1 isn't in changeIndices.
Hence, the answer is -1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Earliest Second to Mark Indices I**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** In this example, we have 8 seconds. The following operations can be performed to mark all indices:
Second 1: Choose index 1 and decrement nums[1] by one. nums becomes [1,2,0].
Second 2: Choose index 1 and decrement nums[1] by one. nums becomes [0,2,0].
Second 3: Choose index 2 and decrement nums[2] by one. nums becomes [0,1,0].
Second 4: Choose index 2 and decrement nums[2] by one. nums becomes [0,0,0].
Second 5: Mark the index changeIndices[5], which is marking index 3, since nums[3] is equal to 0.
Second 6: Mark the index changeIndices[6], which is marking index 2, since nums[2] is equal to 0.
Second 7: Do nothing.
Second 8: Mark the index changeIndices[8], which is marking index 1, since nums[1] is equal to 0.
Now all indices have been marked.
It can be shown that it is not possible to mark all indices earlier than the 8th second.
Hence, the answer is 8.

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
from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)

        def can(T: int) -> bool:
            last = {}
            for s in range(T):
                last[changeIndices[s]] = s
            if len(last) < n:
                return False

            free = 0
            for s in range(T):
                i = changeIndices[s]
                if last[i] == s:
                    if free < nums[i - 1]:
                        return False
                    free -= nums[i - 1]
                else:
                    free += 1
            return True

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
- [3049. Earliest Second to Mark Indices II](../../3001-3500/3049-earliest-second-to-mark-indices-ii/)
- [1900. The Earliest and Latest Rounds Where Players Compete](../../1501-2000/1900-the-earliest-and-latest-rounds-where-players-compete/)
- [3633. Earliest Finish Time for Land and Water Rides I](../../3501-4000/3633-earliest-finish-time-for-land-and-water-rides-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/earliest-second-to-mark-indices-i/)
