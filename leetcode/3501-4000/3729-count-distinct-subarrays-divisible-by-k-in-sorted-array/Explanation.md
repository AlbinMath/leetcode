# LeetCode 3729: Count Distinct Subarrays Divisible by K in Sorted Array

**LeetCode Problem #3729 — Count Distinct Subarrays Divisible by K in Sorted Array**
Solve LeetCode Count Distinct Subarrays Divisible by K in Sorted Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Distinct Subarrays Divisible by K in Sorted Array |
| LeetCode | #3729 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` **sorted** in **non-descending** order and a positive integer `k`.

A ** subarray ** of `nums` is **good** if the sum of its elements is **divisible** by `k`.

Return an integer denoting the number of **distinct** **good** subarrays of `nums`.

Subarrays are **distinct** if their sequences of values are. For example, there are 3 **distinct** subarrays in `[1, 1, 1]`, namely `[1]`, `[1, 1]`, and `[1, 1, 1]`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `nums` is sorted in non-descending order.
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3], k = 3`
- **Output:** `3`
- **Explanation:** The good subarrays are `[1, 2]`, `[3]`, and `[1, 2, 3]`. For example, `[1, 2, 3]` is good because the sum of its elements is `1 + 2 + 3 = 6`, and `6 % k = 6 % 3 = 0`.

### Example 2
- **Input:** `nums = [2,2,2,2,2,2], k = 6`
- **Output:** `2`
- **Explanation:** The good subarrays are `[2, 2, 2]` and `[2, 2, 2, 2, 2, 2]`. For example, `[2, 2, 2]` is good because the sum of its elements is `2 + 2 + 2 = 6`, and `6 % k = 6 % 6 = 0`. 

 Note that `[2, 2, 2]` is counted only once.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Distinct Subarrays Divisible by K in Sorted Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], k = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The good subarrays are `[1, 2]`, `[3]`, and `[1, 2, 3]`. For example, `[1, 2, 3]` is good because the sum of its elements is `1 + 2 + 3 = 6`, and `6 % k = 6 % 3 = 0`.

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
from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        pre = 0
        total = 0
        for v in nums:
            pre = (pre + v) % k
            total += cnt[pre]
            cnt[pre] += 1

        n = len(nums)
        i = 0
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            L = j - i
            s = k // gcd(nums[i] % k, k)   # gcd(0, k) = k, so s = 1
            m = L // s
            total -= m * (L + 1) - s * m * (m + 1) // 2
            total += m
            i = j
        return total
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
- [2183. Count Array Pairs Divisible by K](../../2001-2500/2183-count-array-pairs-divisible-by-k/)
- [3859. Count Subarrays With K Distinct Integers](../../3501-4000/3859-count-subarrays-with-k-distinct-integers/)
- [1497. Check If Array Pairs Are Divisible by k](../../1001-1500/1497-check-if-array-pairs-are-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/)
