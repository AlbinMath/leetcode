# LeetCode 4109: Count Valid Suffix Sorts II

**LeetCode Problem #4109 — Count Valid Suffix Sorts II**
Solve LeetCode Count Valid Suffix Sorts II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Valid Suffix Sorts II |
| LeetCode | #4109 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays `nums` and `target` of lengths `n` and `m`, respectively, where `n <= m`.

For each index `i`, consider sorting the **suffix** `nums[i..n - 1]` of the original array in **non-increasing order**.

Return an integer array `ans` of length `m - n + 1`, where `ans[k]` is the number of indices `i` for which the resulting array equals `target[k..k + n - 1]`.

A **suffix** of an array is a subarray that begins at any index and extends to its end.

## Constraints
- `n == nums.length`
- `m == target.length`
- `1 <= n <= m <= 10^5`
- `1 <= nums[i], target[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,2,3], target = [2,2,3,2,1,3,2,2]`
- **Output:** `[1,1,0,0,0,1]`
- **Explanation:** Sorting the suffix starting at indices 0, 1, and 2 produces `[3, 2, 2]`, `[2, 3, 2]`, and `[2, 2, 3]`, respectively. 

 
 `k = 0`: `[2, 2, 3]` is produced by `i = 2`. 
 `k = 1`: `[2, 3, 2]` is produced by `i = 1`. 
 `k = 2, 3, 4`: None of the corresponding subarrays can be produced. 
 `k = 5`: `[3, 2, 2]` is produced by `i = 0`. 
 

 Therefore, the answer is `[1, 1, 0, 0, 0, 1]`.

### Example 2
- **Input:** `nums = [5,6,5], target = [5,6,5,5,6,5]`
- **Output:** `[2,1,0,2]`
- **Explanation:** Sorting the suffix starting at index 0 produces `[6, 5, 5]`, while starting at either index 1 or 2 produces `[5, 6, 5]`. 

 
 `k = 0`: `[5, 6, 5]` is produced by `i = 1` and `i = 2`. 
 `k = 1`: `[6, 5, 5]` is produced by `i = 0`. 
 `k = 2`: `[5, 5, 6]` cannot be produced. 
 `k = 3`: `[5, 6, 5]` is produced by `i = 1` and `i = 2`. 
 

 Therefore, the answer is `[2, 1, 0, 2]`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Valid Suffix Sorts II**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,2,3], target = [2,2,3,2,1,3,2,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,1,0,0,0,1]`.
4. **Verification:** Sorting the suffix starting at indices 0, 1, and 2 produces `[3, 2, 2]`, `[2, 3, 2]`, and `[2, 2, 3]`, respectively. 

 
 `k = 0`: `[2, 2, 3]` is produced by `i = 2`. 
 `k = 1`: `[2, 3, 2]` is produced by `i = 1`. 
 `k = 2, 3, 4`: None of the corresponding subarrays can be produced. 
 `k = 5`: `[3, 2, 2]` is produced by `i = 0`. 
 

 Therefore, the answer is `[1, 1, 0, 0, 0, 1]`.

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
import random
from typing import List

class Solution:
    def countSuffix(self, nums: List[int], target: List[int]) -> List[int]:
        n, m = len(nums), len(target)
        M = (1 << 64) - 1
        rnd = {}
        def h(v):
            if v not in rnd:
                rnd[v] = random.getrandbits(64)
            return rnd[v]

        total = 0
        for v in nums:
            total = (total + h(v)) & M
        T = [0] * (m + 1)
        for i, v in enumerate(target):
            T[i + 1] = (T[i] + h(v)) & M
        s = nums + [0] + target
        L = len(s)
        z = [0] * L
        l = r = 0
        for i in range(1, L):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < L and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]
        st = [0] * m
        for p in range(1, m):
            st[p] = st[p - 1] if target[p] <= target[p - 1] else p

        ans = []
        for k in range(m - n + 1):
            if (T[k + n] - T[k]) & M != total:
                ans.append(0)
                continue
            e = k + n - 1
            lo = max(0, st[e] - k)
            hi = min(z[n + 1 + k], n - 1)
            ans.append(max(0, hi - lo + 1))
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
- [3042. Count Prefix and Suffix Pairs I](../../3001-3500/3309-count-prefix-and-suffix-pairs-i/)
- [3045. Count Prefix and Suffix Pairs II](../../3001-3500/3305-count-prefix-and-suffix-pairs-ii/)
- [1359. Count All Valid Pickup and Delivery Options](../../1001-1500/1461-count-all-valid-pickup-and-delivery-options/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-valid-suffix-sorts-ii/)
