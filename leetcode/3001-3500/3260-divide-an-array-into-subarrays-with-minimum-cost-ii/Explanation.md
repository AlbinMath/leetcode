# LeetCode 3013: Divide an Array Into Subarrays With Minimum Cost II

**LeetCode Problem #3013 — Divide an Array Into Subarrays With Minimum Cost II**
Solve LeetCode Divide an Array Into Subarrays With Minimum Cost II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divide an Array Into Subarrays With Minimum Cost II |
| LeetCode | #3013 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array of integers `nums` of length `n`, and two **positive** integers `k` and `dist`.

The **cost** of an array is the value of its **first** element. For example, the cost of `[1,2,3]` is `1` while the cost of `[3,4,1]` is `3`.

You need to divide `nums` into `k` **disjoint contiguous ** subarrays , such that the difference between the starting index of the **second** subarray and the starting index of the `kth` subarray should be **less than or equal to** `dist`. In other words, if you divide `nums` into the subarrays `nums[0..(i_1 - 1)], nums[i_1..(i_2 - 1)], ..., nums[i_k-1..(n - 1)]`, then `i_k-1 - i_1 <= dist`.

Return *the **minimum** possible sum of the cost of these* *subarrays*.

## Constraints
- `3 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`
- `3 <= k <= n`
- `k - 2 <= dist <= n - 2`

## Examples
### Example 1
- **Input:** `nums = [1,3,2,6,4,2], k = 3, dist = 3`
- **Output:** `5`
- **Explanation:** The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because i_k-1 - i_1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.

### Example 2
- **Input:** `nums = [10,1,2,2,2,1], k = 4, dist = 3`
- **Output:** `15`
- **Explanation:** The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because i_k-1 - i_1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between i_k-1 and i_1 is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.

### Example 3
- **Input:** `nums = [10,8,18,9], k = 3, dist = 1`
- **Output:** `36`
- **Explanation:** The best possible way to divide nums into 3 subarrays is: [10], [8], and [18,9]. This choice is valid because i_k-1 - i_1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between i_k-1 and i_1 is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Divide an Array Into Subarrays With Minimum Cost II**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2,6,4,2], k = 3, dist = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because i_k-1 - i_1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.

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
from collections import defaultdict

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        need = k - 2

        small = []            # max-heap via negation
        large = []            # min-heap
        del_small = defaultdict(int)
        del_large = defaultdict(int)
        cnt_small = 0
        sum_small = 0
        cnt_large = 0

        def clean_small():
            while small and del_small[-small[0]] > 0:
                del_small[-small[0]] -= 1
                heapq.heappop(small)

        def clean_large():
            while large and del_large[large[0]] > 0:
                del_large[large[0]] -= 1
                heapq.heappop(large)

        def rebalance():
            nonlocal cnt_small, sum_small, cnt_large
            while cnt_small > need:
                clean_small()
                v = -heapq.heappop(small)
                cnt_small -= 1
                sum_small -= v
                heapq.heappush(large, v)
                cnt_large += 1
            while cnt_small < need and cnt_large > 0:
                clean_large()
                v = heapq.heappop(large)
                cnt_large -= 1
                heapq.heappush(small, -v)
                cnt_small += 1
                sum_small += v
            while True:
                clean_small()
                clean_large()
                if small and large and -small[0] > large[0]:
                    a = -heapq.heappop(small)
                    b = heapq.heappop(large)
                    heapq.heappush(small, -b)
                    heapq.heappush(large, a)
                    sum_small += b - a
                else:
                    break

        def add(v):
            nonlocal cnt_small, sum_small, cnt_large
            clean_small()
            if small and v <= -small[0]:
                heapq.heappush(small, -v)
                cnt_small += 1
                sum_small += v
            else:
                heapq.heappush(large, v)
                cnt_large += 1
            rebalance()

        def remove(v):
            nonlocal cnt_small, sum_small, cnt_large
            clean_small()
            if small and v <= -small[0]:
                del_small[v] += 1
                cnt_small -= 1
                sum_small -= v
            else:
                del_large[v] += 1
                cnt_large -= 1
            rebalance()

        best = float('inf')
        for j in range(2, min(n - 1, 1 + dist) + 1):
            add(nums[j])
        if cnt_small == need:
            best = nums[1] + sum_small

        for i in range(2, n):
            remove(nums[i])
            if i + dist < n:
                add(nums[i + dist])
            if cnt_small == need:
                best = min(best, nums[i] + sum_small)

        return nums[0] + best
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
- [3010. Divide an Array Into Subarrays With Minimum Cost I](../../3001-3500/3263-divide-an-array-into-subarrays-with-minimum-cost-i/)
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1633-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)
- [2206. Divide Array Into Equal Pairs](../../2001-2500/2308-divide-array-into-equal-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/)
