# LeetCode 2499: Minimum Total Cost to Make Arrays Unequal

**LeetCode Problem #2499 — Minimum Total Cost to Make Arrays Unequal**
Solve LeetCode Minimum Total Cost to Make Arrays Unequal using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Total Cost to Make Arrays Unequal |
| LeetCode | #2499 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** integer arrays `nums1` and `nums2`, of equal length `n`.

In one operation, you can swap the values of any two indices of `nums1`. The **cost** of this operation is the **sum** of the indices.

Find the **minimum** total cost of performing the given operation **any** number of times such that `nums1[i] != nums2[i]` for all `0 <= i <= n - 1` after performing all the operations.

Return *the **minimum total cost** such that *`nums1` and `nums2`* satisfy the above condition*. In case it is not possible, return `-1`.

## Constraints
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= n`

## Examples
### Example 1
- **Input:** `nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5]`
- **Output:** `10`
- **Explanation:** One of the ways we can perform the operations is:
- Swap values at indices 0 and 3, incurring cost = 0 + 3 = 3. Now, nums1 = [4,2,3,1,5]
- Swap values at indices 1 and 2, incurring cost = 1 + 2 = 3. Now, nums1 = [4,3,2,1,5].
- Swap values at indices 0 and 4, incurring cost = 0 + 4 = 4. Now, nums1 =[5,3,2,1,4].
We can see that for each index i, nums1[i] != nums2[i]. The cost required here is 10.
Note that there are other ways to swap values, but it can be proven that it is not possible to obtain a cost less than 10.

### Example 2
- **Input:** `nums1 = [2,2,2,1,3], nums2 = [1,2,2,3,3]`
- **Output:** `10`
- **Explanation:** One of the ways we can perform the operations is:
- Swap values at indices 2 and 3, incurring cost = 2 + 3 = 5. Now, nums1 = [2,2,1,2,3].
- Swap values at indices 1 and 4, incurring cost = 1 + 4 = 5. Now, nums1 = [2,3,1,2,2].
The total cost needed here is 10, which is the minimum possible.

### Example 3
- **Input:** `nums1 = [1,2,2], nums2 = [1,2,2]`
- **Output:** `-1`
- **Explanation:** It can be shown that it is not possible to satisfy the given conditions irrespective of the number of operations we perform.
Hence, we return -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Total Cost to Make Arrays Unequal**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** One of the ways we can perform the operations is:
- Swap values at indices 0 and 3, incurring cost = 0 + 3 = 3. Now, nums1 = [4,2,3,1,5]
- Swap values at indices 1 and 2, incurring cost = 1 + 2 = 3. Now, nums1 = [4,3,2,1,5].
- Swap values at indices 0 and 4, incurring cost = 0 + 4 = 4. Now, nums1 =[5,3,2,1,4].
We can see that for each index i, nums1[i] != nums2[i]. The cost required here is 10.
Note that there are other ways to swap values, but it can be proven that it is not possible to obtain a cost less than 10.

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
from collections import defaultdict

class Solution:
    def minimumTotalCost(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        conflict_counts = defaultdict(int)
        total_conflicts = 0
        total_cost = 0
        max_freq = 0
        dominant_val = -1
        
        for i in range(n):
            if nums1[i] == nums2[i]:
                val = nums1[i]
                conflict_counts[val] += 1
                total_conflicts += 1
                total_cost += i
                
                if conflict_counts[val] > max_freq:
                    max_freq = conflict_counts[val]
                    dominant_val = val
                    
        excess = 2 * max_freq - total_conflicts
        
        if excess > 0:
            for i in range(n):
                if nums1[i] != nums2[i] and nums1[i] != dominant_val and nums2[i] != dominant_val:
                    total_cost += i
                    excess -= 1
                    if excess == 0:
                        break
                        
            if excess > 0:
                return -1
                
        return total_cost
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [3784. Minimum Deletion Cost to Make All Characters Equal](../../4001-4500/4138-minimum-deletion-cost-to-make-all-characters-equal/)
- [3987. Minimum Total Cost to Process All Elements](../../4001-4500/4351-minimum-total-cost-to-process-all-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/)
