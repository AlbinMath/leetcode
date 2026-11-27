# LeetCode 3321: Find X-Sum of All K-Long Subarrays II

**LeetCode Problem #3321 — Find X-Sum of All K-Long Subarrays II**
Solve LeetCode Find X-Sum of All K-Long Subarrays II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find X-Sum of All K-Long Subarrays II |
| LeetCode | #3321 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums` of `n` integers and two integers `k` and `x`.

The **x-sum** of an array is calculated by the following procedure:

Count the occurrences of all elements in the array. 
 Keep only the occurrences of the top `x` most frequent elements. If two elements have the same number of occurrences, the element with the **bigger** value is considered more frequent. 
 Calculate the sum of the resulting array.

**Note** that if an array has less than `x` distinct elements, its **x-sum** is the sum of the array.

Return an integer array `answer` of length `n - k + 1` where `answer[i]` is the **x-sum** of the subarray `nums[i..i + k - 1]`.

## Constraints
- `nums.length == n`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= x <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,1,2,2,3,4,2,3], k = 6, x = 2`
- **Output:** `[6,10,12]`
- **Explanation:** For subarray `[1, 1, 2, 2, 3, 4]`, only elements 1 and 2 will be kept in the resulting array. Hence, `answer[0] = 1 + 1 + 2 + 2`. 
 For subarray `[1, 2, 2, 3, 4, 2]`, only elements 2 and 4 will be kept in the resulting array. Hence, `answer[1] = 2 + 2 + 2 + 4`. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times. 
 For subarray `[2, 2, 3, 4, 2, 3]`, only elements 2 and 3 are kept in the resulting array. Hence, `answer[2] = 2 + 2 + 2 + 3 + 3`.

### Example 2
- **Input:** `nums = [3,8,7,8,7,5], k = 2, x = 2`
- **Output:** `[11,15,15,15,12]`
- **Explanation:** Since `k == x`, `answer[i]` is equal to the sum of the subarray `nums[i..i + k - 1]`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find X-Sum of All K-Long Subarrays II**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,2,2,3,4,2,3], k = 6, x = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,10,12]`.
4. **Verification:** For subarray `[1, 1, 2, 2, 3, 4]`, only elements 1 and 2 will be kept in the resulting array. Hence, `answer[0] = 1 + 1 + 2 + 2`. 
 For subarray `[1, 2, 2, 3, 4, 2]`, only elements 2 and 4 will be kept in the resulting array. Hence, `answer[1] = 2 + 2 + 2 + 4`. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times. 
 For subarray `[2, 2, 3, 4, 2, 3]`, only elements 2 and 3 are kept in the resulting array. Hence, `answer[2] = 2 + 2 + 2 + 3 + 3`.

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
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = defaultdict(int)
        top = SortedList()    # pairs (count, value), the x largest
        rest = SortedList()   # remaining pairs
        top_sum = 0

        def remove(v):
            nonlocal top_sum
            c = cnt[v]
            if c == 0:
                return
            p = (c, v)
            if p in top:
                top.remove(p)
                top_sum -= c * v
            else:
                rest.remove(p)

        def insert(v):
            nonlocal top_sum
            c = cnt[v]
            if c == 0:
                return
            p = (c, v)
            top.add(p)
            top_sum += c * v

        def rebalance():
            nonlocal top_sum
            # keep top at most x
            while len(top) > x:
                p = top.pop(0)               # smallest of top
                top_sum -= p[0] * p[1]
                rest.add(p)
            # fill top up to x from rest
            while len(top) < x and rest:
                p = rest.pop()               # largest of rest
                top.add(p)
                top_sum += p[0] * p[1]
            # swap while the best of rest beats the worst of top
            while rest and top and rest[-1] > top[0]:
                a = rest.pop()
                b = top.pop(0)
                top.add(a)
                rest.add(b)
                top_sum += a[0] * a[1] - b[0] * b[1]

        def change(v, delta):
            remove(v)
            cnt[v] += delta
            insert(v)
            rebalance()

        res = []
        for i, v in enumerate(nums):
            change(v, 1)
            if i >= k:
                change(nums[i - k], -1)
            if i >= k - 1:
                res.append(top_sum)
        return res
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
- [3318. Find X-Sum of All K-Long Subarrays I](../../3001-3500/3318-find-x-sum-of-all-k-long-subarrays-i/)
- [1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](../../1001-1500/1414-find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2099-find-subsequence-of-length-k-with-the-largest-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/)
