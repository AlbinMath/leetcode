# LeetCode 3795: Minimum Subarray Length With Distinct Sum At Least K

**LeetCode Problem #3795 — Minimum Subarray Length With Distinct Sum At Least K**
Solve LeetCode Minimum Subarray Length With Distinct Sum At Least K using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Subarray Length With Distinct Sum At Least K |
| LeetCode | #3795 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

Return the **minimum** length of a ** subarray ** whose sum of the **distinct** values present in that subarray (each value counted once) is **at least** `k`. If no such subarray exists, return -1.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,2,3,1], k = 4`
- **Output:** `2`
- **Explanation:** The subarray `[2, 3]` has distinct elements `{2, 3}` whose sum is `2 + 3 = 5`, which is ​​​​​​​at least `k = 4`. Thus, the answer is 2.

### Example 2
- **Input:** `nums = [3,2,3,4], k = 5`
- **Output:** `2`
- **Explanation:** The subarray `[3, 2]` has distinct elements `{3, 2}` whose sum is `3 + 2 = 5`, which is ​​​​​​​at least `k = 5`. Thus, the answer is 2.

### Example 3
- **Input:** `nums = [5,5,4], k = 5`
- **Output:** `1`
- **Explanation:** The subarray `[5]` has distinct elements `{5}` whose sum is `5`, which is at least `k = 5`. Thus, the answer is 1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Subarray Length With Distinct Sum At Least K**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,2,3,1], k = 4`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The subarray `[2, 3]` has distinct elements `{2, 3}` whose sum is `2 + 3 = 5`, which is ​​​​​​​at least `k = 4`. Thus, the answer is 2.

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
from collections import defaultdict

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        dsum = 0
        l = 0
        best = float('inf')
        for r, x in enumerate(nums):
            if cnt[x] == 0:
                dsum += x
            cnt[x] += 1
            while dsum >= k:
                best = min(best, r - l + 1)
                y = nums[l]
                cnt[y] -= 1
                if cnt[y] == 0:
                    dsum -= y
                l += 1
        return -1 if best == float('inf') else best
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
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2001-2500/2461-maximum-sum-of-distinct-subarrays-with-length-k/)
- [3381. Maximum Subarray Sum With Length Divisible by K](../../3001-3500/3381-maximum-subarray-sum-with-length-divisible-by-k/)
- [3473. Sum of K Subarrays With Length at Least M](../../3001-3500/3473-sum-of-k-subarrays-with-length-at-least-m/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/)
