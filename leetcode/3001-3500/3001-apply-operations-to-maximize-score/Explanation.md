# LeetCode 2818: Apply Operations to Maximize Score

**LeetCode Problem #2818 — Apply Operations to Maximize Score**
Solve LeetCode Apply Operations to Maximize Score using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apply Operations to Maximize Score |
| LeetCode | #2818 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums` of `n` positive integers and an integer `k`.

Initially, you start with a score of `1`. You have to maximize your score by applying the following operation at most `k` times:

Choose any **non-empty** subarray `nums[l, ..., r]` that you haven't chosen previously. 
 Choose an element `x` of `nums[l, ..., r]` with the highest **prime score**. If multiple such elements exist, choose the one with the smallest index. 
 Multiply your score by `x`.

Here, `nums[l, ..., r]` denotes the subarray of `nums` starting at index `l` and ending at the index `r`, both ends being inclusive.

The **prime score** of an integer `x` is equal to the number of distinct prime factors of `x`. For example, the prime score of `300` is `3` since `300 = 2 * 2 * 3 * 5 * 5`.

Return *the **maximum possible score** after applying at most *`k`* operations*.

Since the answer may be large, return it modulo `10^9 + 7`.

## Constraints
- `1 <= nums.length == n <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= min(n * (n + 1) / 2, 10^9)`

## Examples
### Example 1
- **Input:** `nums = [8,3,9,3,8], k = 2`
- **Output:** `81`
- **Explanation:** To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.

### Example 2
- **Input:** `nums = [19,12,14,6,10,18], k = 3`
- **Output:** `4788`
- **Explanation:** To get a score of 4788, we can apply the following operations: 
- Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
- Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
It can be proven that 4788 is the highest score one can obtain.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Apply Operations to Maximize Score**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [8,3,9,3,8], k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `81`.
4. **Verification:** To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.

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
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        mx = max(nums)

        # distinct prime factor counts via sieve
        omega = [0] * (mx + 1)
        for p in range(2, mx + 1):
            if omega[p] == 0:  # p is prime
                for m in range(p, mx + 1, p):
                    omega[m] += 1

        sc = [omega[x] for x in nums]

        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            # pop strictly smaller scores; remaining top has score >= sc[i]
            while stack and sc[stack[-1]] < sc[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        ans = 1
        for i in sorted(range(n), key=lambda i: -nums[i]):
            cnt = (i - left[i]) * (right[i] - i)
            t = min(cnt, k)
            ans = ans * pow(nums[i], t, MOD) % MOD
            k -= t
            if k == 0:
                break

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
- [2968. Apply Operations to Maximize Frequency Score](../../3001-3500/3196-apply-operations-to-maximize-frequency-score/)
- [2897. Apply Operations on Array to Maximize Sum of Squares](../../3001-3500/3153-apply-operations-on-array-to-maximize-sum-of-squares/)
- [1799. Maximize Score After N Operations](../../1501-2000/1906-maximize-score-after-n-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-operations-to-maximize-score/)
