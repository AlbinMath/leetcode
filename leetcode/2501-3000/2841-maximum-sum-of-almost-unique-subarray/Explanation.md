# LeetCode 2841: Maximum Sum of Almost Unique Subarray

**LeetCode Problem #2841 — Maximum Sum of Almost Unique Subarray**
Solve LeetCode Maximum Sum of Almost Unique Subarray using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of Almost Unique Subarray |
| LeetCode | #2841 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and two positive integers `m` and `k`.

Return *the **maximum sum** out of all **almost unique** subarrays of length *`k`* of* `nums`. If no such subarray exists, return `0`.

A subarray of `nums` is **almost unique** if it contains at least `m` distinct elements.

A subarray is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `1 <= m <= k <= nums.length`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,6,7,3,1,7], m = 3, k = 4`
- **Output:** `18`
- **Explanation:** There are 3 almost unique subarrays of size `k = 4`. These subarrays are [2, 6, 7, 3], [6, 7, 3, 1], and [7, 3, 1, 7]. Among these subarrays, the one with the maximum sum is [2, 6, 7, 3] which has a sum of 18.

### Example 2
- **Input:** `nums = [5,9,9,2,4,5,4], m = 1, k = 3`
- **Output:** `23`
- **Explanation:** There are 5 almost unique subarrays of size k. These subarrays are [5, 9, 9], [9, 9, 2], [9, 2, 4], [2, 4, 5], and [4, 5, 4]. Among these subarrays, the one with the maximum sum is [5, 9, 9] which has a sum of 23.

### Example 3
- **Input:** `nums = [1,2,1,2,1,2,1], m = 3, k = 3`
- **Output:** `0`
- **Explanation:** There are no subarrays of size `k = 3` that contain at least `m = 3` distinct elements in the given array [1,2,1,2,1,2,1]. Therefore, no almost unique subarrays exist, and the maximum sum is 0.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Sum of Almost Unique Subarray**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,6,7,3,1,7], m = 3, k = 4`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** There are 3 almost unique subarrays of size `k = 4`. These subarrays are [2, 6, 7, 3], [6, 7, 3, 1], and [7, 3, 1, 7]. Among these subarrays, the one with the maximum sum is [2, 6, 7, 3] which has a sum of 18.

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
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = defaultdict(int)
        total = 0
        ans = 0
        for i, x in enumerate(nums):
            total += x
            cnt[x] += 1
            if i >= k:
                y = nums[i - k]
                total -= y
                cnt[y] -= 1
                if cnt[y] == 0:
                    del cnt[y]
            if i >= k - 1 and len(cnt) >= m:
                ans = max(ans, total)
        return ans
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
- [918. Maximum Sum Circular Subarray](../../0501-1000/0918-maximum-sum-circular-subarray/)
- [1800. Maximum Ascending Subarray Sum](../../1501-2000/1800-maximum-ascending-subarray-sum/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../../3501-4000/3962-maximum-subarray-sum-after-at-most-k-swaps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/)
